#!/bin/bash
# Только сборка vLLM образа для AMD ROCm (без запуска)

set -e

GPU_ARCH=${1:-"gfx1100"}

echo "🔨 Сборка vLLM образа для AMD ROCm"
echo "   GPU архитектура: $GPU_ARCH"

if [ ! -d "/tmp/vllm" ]; then
    echo "📥 Клонирование vLLM..."
    git clone https://github.com/vllm-project/vllm.git /tmp/vllm
fi

cd /tmp/vllm

podman build \
    --format docker \
    -f docker/Dockerfile.rocm \
    --build-arg REMOTE_VLLM=0 \
    --build-arg ARG_PYTORCH_ROCM_ARCH="${GPU_ARCH}" \
    --target final \
    -t vllm-rocm:latest \
    .

echo "✅ Образ vllm-rocm:latest собран!"
podman images | grep vllm-rocm
