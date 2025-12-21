#!/bin/bash
# scripts/vllm/rocm/status_vllm_rocm.sh
#
# Показать статус всех vLLM контейнеров и доступность API

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Статус vLLM (AMD ROCm)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Проверка образа
if podman images | grep -q "vllm-rocm"; then
    echo "✅ Образ vllm-rocm:latest"
    IMAGE_SIZE=$(podman images --format "{{.Size}}" localhost/vllm-rocm:latest)
    echo "   Размер: $IMAGE_SIZE"
else
    echo "❌ Образ vllm-rocm:latest не найден"
    echo "   Запустите: ./scripts/vllm/rocm/build_vllm_rocm.sh"
fi

echo ""
echo "Контейнеры:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Запущенные контейнеры
RUNNING=$(podman ps --filter name=vllm- --format "{{.Names}}" | wc -l)

if [ "$RUNNING" -gt 0 ]; then
    echo "🟢 Запущено: $RUNNING"
    echo ""
    podman ps --filter name=vllm- --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    echo ""
    
    # Проверка доступности API
    echo "API эндпоинты:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    podman ps --filter name=vllm- --format "{{.Names}}" | while read CONTAINER; do
        # Извлечь порт из переменных окружения контейнера
        PORT=$(podman inspect "$CONTAINER" --format '{{range .Config.Env}}{{println .}}{{end}}' | grep -oP '(?<=--port )\d+' || echo "8000")
        
        echo -n "  $CONTAINER (порт $PORT): "
        
        if curl -s --max-time 2 "http://localhost:$PORT/health" > /dev/null 2>&1; then
            echo "✅ Доступен"
            echo "     http://localhost:$PORT/v1/models"
        else
            echo "⚠️  Недоступен (возможно, загрузка модели)"
        fi
    done
else
    echo "⚪ Запущено: 0"
fi

# Остановленные контейнеры
STOPPED=$(podman ps -a --filter name=vllm- --filter status=exited --format "{{.Names}}" | wc -l)

if [ "$STOPPED" -gt 0 ]; then
    echo ""
    echo "🔴 Остановлено: $STOPPED"
    podman ps -a --filter name=vllm- --filter status=exited --format "table {{.Names}}\t{{.Status}}"
fi

