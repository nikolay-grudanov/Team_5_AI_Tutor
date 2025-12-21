#!/bin/bash
# scripts/vllm/rocm/stop_vllm_rocm.sh
#
# Остановка vLLM контейнеров для AMD ROCm
#
# Использование:
#   ./stop_vllm_rocm.sh                    # Остановить все vLLM контейнеры
#   ./stop_vllm_rocm.sh vllm-HunyuanOCR    # Остановить конкретный контейнер
#   ./stop_vllm_rocm.sh --all              # Остановить и удалить все

set -e

# Функция: остановить контейнер
stop_container() {
    local CONTAINER=$1
    echo "🛑 Остановка: $CONTAINER"
    podman stop "$CONTAINER" 2>/dev/null || true
    podman rm "$CONTAINER" 2>/dev/null || true
    echo "✅ Остановлен: $CONTAINER"
}

# Остановить все vLLM контейнеры
if [ "$1" = "--all" ] || [ -z "$1" ]; then
    CONTAINERS=$(podman ps -a --filter name=vllm- --format "{{.Names}}")
    
    if [ -z "$CONTAINERS" ]; then
        echo "⚠️  vLLM контейнеры не найдены"
        exit 0
    fi
    
    echo "Остановка всех vLLM контейнеров..."
    echo ""
    
    echo "$CONTAINERS" | while read CONTAINER; do
        stop_container "$CONTAINER"
    done
    
    echo ""
    echo "✅ Все vLLM контейнеры остановлены"
else
    CONTAINER_NAME=$1
    
    # Проверка существования
    if ! podman ps -a --filter name="^${CONTAINER_NAME}$" --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        echo "❌ Контейнер '$CONTAINER_NAME' не найден"
        echo ""
        echo "Доступные vLLM контейнеры:"
        podman ps -a --filter name=vllm- --format "  - {{.Names}}\t({{.Status}})"
        exit 1
    fi
    
    stop_container "$CONTAINER_NAME"
fi

echo ""
echo "Оставшиеся vLLM контейнеры:"
podman ps -a --filter name=vllm- --format "table {{.Names}}\t{{.Status}}" || echo "  (нет)"
