#!/bin/bash
set -euo pipefail

echo
echo "╔══════════════════════════════════════════════╗"
echo "║  🔨 Сборка образа с ROCm debug-agent         ║"
echo "╚══════════════════════════════════════════════╝"
echo

if [ ! -f Dockerfile.vllm-rocm-debug ]; then
  echo "❌ Dockerfile.vllm-rocm-debug не найден"; exit 1
fi

IMAGE_NAME="localhost/vllm-rocm-debug"
TAG="7.1-source"

echo "🚀 Начинаем сборку дебаг-образа: ${IMAGE_NAME}:${TAG}"

# Сборка образа
podman build \
    --format docker \
    --platform linux/amd64 \
    -f Dockerfile.vllm-debug \
    -t ${IMAGE_NAME}:${TAG} .

echo ""
echo "✅ Сборка завершена!"
echo "🔍 Проверка архитектуры образа:"
podman image inspect ${IMAGE_NAME}:${TAG} --format '{{.Architecture}}'

echo ""
echo "📝 Для запуска контейнера с поддержкой GPU и дебага используйте:"
echo "podman run -it --rm \\"
echo "  --device=/dev/kfd --device=/dev/dri \\"
echo "  --group-add video --cap-add=SYS_PTRACE \\"
echo "  --security-opt seccomp=unconfined \\"
echo "  ${IMAGE_NAME}:${TAG}"

