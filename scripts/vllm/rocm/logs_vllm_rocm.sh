#!/bin/bash
# scripts/vllm/rocm/logs_vllm_rocm.sh
#
# Просмотр логов vLLM контейнеров для AMD ROCm
#
# Использование:
#   ./logs_vllm_rocm.sh                    # Логи последнего запущенного
#   ./logs_vllm_rocm.sh vllm-HunyuanOCR    # Логи конкретного контейнера
#   ./logs_vllm_rocm.sh --list             # Список всех vLLM контейнеров
#   ./logs_vllm_rocm.sh --tail 100         # Последние 100 строк

set -e

# Функция: показать список vLLM контейнеров
show_containers() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "vLLM контейнеры (AMD ROCm):"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if podman ps -a --filter name=vllm- --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -q vllm-; then
        podman ps -a --filter name=vllm- --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    else
        echo "  (нет контейнеров)"
    fi
    echo ""
}

# Обработка --list
if [ "$1" = "--list" ] || [ "$1" = "-l" ]; then
    show_containers
    exit 0
fi

# Обработка --tail
if [ "$1" = "--tail" ]; then
    TAIL_LINES=${2:-50}
    
    if [ -n "$3" ]; then
        # Указан конкретный контейнер
        CONTAINER="$3"
    else
        # Последний запущенный
        CONTAINER=$(podman ps --filter name=vllm- --format "{{.Names}}" | head -1)
        
        if [ -z "$CONTAINER" ]; then
            echo "❌ vLLM контейнеры не запущены"
            echo ""
            show_containers
            exit 1
        fi
    fi
    
    echo "📊 Последние $TAIL_LINES строк логов: $CONTAINER"
    echo ""
    podman logs --tail "$TAIL_LINES" "$CONTAINER"
    exit 0
fi

# Если указано имя контейнера
if [ -n "$1" ]; then
    CONTAINER="$1"
    
    # Проверка существования контейнера
    if ! podman ps -a --filter name="^${CONTAINER}$" --format "{{.Names}}" | grep -q "^${CONTAINER}$"; then
        echo "❌ Контейнер '$CONTAINER' не найден"
        echo ""
        show_containers
        exit 1
    fi
    
    # Проверка запущен ли контейнер
    if ! podman ps --filter name="^${CONTAINER}$" --format "{{.Names}}" | grep -q "^${CONTAINER}$"; then
        echo "⚠️  Контейнер '$CONTAINER' остановлен"
        echo "Показываю последние логи..."
        echo ""
        podman logs --tail 50 "$CONTAINER"
        exit 0
    fi
    
    echo "📊 Логи контейнера (live): $CONTAINER"
    echo "   Нажмите Ctrl+C для выхода"
    echo ""
    podman logs -f "$CONTAINER"
else
    # Автоматический выбор последнего запущенного контейнера
    CONTAINER=$(podman ps --filter name=vllm- --format "{{.Names}}" | head -1)
    
    if [ -z "$CONTAINER" ]; then
        echo "❌ vLLM контейнеры не запущены"
        echo ""
        
        # Показать последние логи остановленных контейнеров
        STOPPED=$(podman ps -a --filter name=vllm- --filter status=exited --format "{{.Names}}" | head -1)
        
        if [ -n "$STOPPED" ]; then
            echo "Последний остановленный контейнер: $STOPPED"
            echo "Показываю последние 50 строк логов..."
            echo ""
            podman logs --tail 50 "$STOPPED"
        else
            show_containers
        fi
        
        exit 1
    fi
    
    echo "📊 Логи последнего запущенного контейнера: $CONTAINER"
    echo "   Нажмите Ctrl+C для выхода"
    echo ""
    podman logs -f "$CONTAINER"
fi
