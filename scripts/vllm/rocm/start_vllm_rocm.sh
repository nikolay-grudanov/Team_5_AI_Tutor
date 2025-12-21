#!/bin/bash
# scripts/vllm/rocm/start_vllm_rocm.sh
# 
# Запуск vLLM сервера на AMD GPU с ROCm
# Использует официальный Dockerfile.rocm из репозитория vLLM
#
# Требования:
#   - AMD GPU (RDNA 2/3: RX 6000/7000 серии или MI серии)
#   - Podman
#   - ROCm драйвера
#
# Использование: 
#   ./start_vllm_rocm.sh <model_name> <port>
#
# Примеры:
#   ./start_vllm_rocm.sh HunyuanOCR 8000
#   ./start_vllm_rocm.sh Qwen3-VL-8B-Instruct 8001
# 
# Если нужно очистить кэш MIOpen
# CLEAR_MIOPEN_CACHE=true ./scripts/vllm/rocm/start_vllm_rocm.sh HunyuanOCR 8000

set -euo pipefail

# ============================================================================
# Цвета для вывода
# ============================================================================
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# ============================================================================
# Проверка аргументов
# ============================================================================
if [ "$#" -ne 2 ]; then
    echo -e "${RED}❌ Ошибка: Неправильное количество аргументов${NC}"
    echo ""
    echo "Использование:"
    echo "  $0 <MODEL_NAME> <PORT>"
    echo ""
    echo "Примеры:"
    echo "  $0 HunyuanOCR 8000"
    echo "  $0 Qwen2-VL-2B-Instruct 8001"
    echo "  $0 LightOnOCR-1B-1025 8000"
    echo ""
    exit 1
fi

# ============================================================================
# ПРОВЕРКА ЗАВИСИМОСТЕЙ
# ============================================================================

# Проверка наличия podman
if ! command -v podman &> /dev/null; then
    echo -e "${RED}❌ Podman не установлен. Установите Podman и попробуйте снова.${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Podman установлен${NC}"

# ============================================================================
# КОНФИГУРАЦИЯ
# ============================================================================

cd "$(dirname "$0")/../../.."

MODEL_NAME="$1"
PORT="$2"
CONTAINER_NAME="vllm-${MODEL_NAME//\//-}"

MODEL_PATH="$(pwd)/models"
FULL_MODEL_PATH="${MODEL_PATH}/${MODEL_NAME}"
LOG_DIR="$(pwd)/logs"
LOG_FILE="${LOG_DIR}/vllm_${MODEL_NAME//\//-}.log"
CACHE_DIR="$(pwd)/cache"

mkdir -p "$CACHE_DIR"
mkdir -p "$LOG_DIR"

# ============================================================================
# КОНФИГУРАЦИЯ GPU
# ============================================================================
# GPU архитектура
# Узнаем GPU архитектуру выполнив команду на хосте (не в контейнере)
# rocm-smi  --showproductname
# ============================ ROCm System Management Interface ============================
# WARNING: AMD GPU device(s) is/are in a low-power state. Check power control/runtime_status

# ====================================== Product Info ======================================
# GPU[0]		: Card Series: 		AMD Radeon RX 7800 XT
# GPU[0]		: Card Model: 		0x747e
# GPU[0]		: Card Vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
# GPU[0]		: Card SKU: 		D712BP3
# GPU[0]		: Subsystem ID: 	0x0606
# GPU[0]		: Device Rev: 		0xc8
# GPU[0]		: Node ID: 		1
# GPU[0]		: GUID: 		38755
# GPU[0]		: GFX Version: 		gfx1101
# GPU[1]		: Card Series: 		AMD Ryzen 9 9950X 16-Core Processor
# GPU[1]		: Card Model: 		0x13c0
# GPU[1]		: Card Vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
# GPU[1]		: Card SKU: 		RAPHAEL
# GPU[1]		: Subsystem ID: 	0x7e12
# GPU[1]		: Device Rev: 		0xc1
# GPU[1]		: Node ID: 		2
# GPU[1]		: GUID: 		42374
# GPU[1]		: GFX Version: 		gfx1036
# ==========================================================================================
# ================================== End of ROCm SMI Log ===================================

# Находим нужную карту и ее архитектуру

GPU_ARCH="gfx1101"

# ============================================================================
# ПРОВЕРКА МОДЕЛИ
# ============================================================================

if [ ! -d "$FULL_MODEL_PATH" ]; then
    echo "❌ Модель не найдена: $FULL_MODEL_PATH"
    echo "Доступные модели:"
    ls -1 "$MODEL_PATH" 2>/dev/null || echo "  (нет)"
    exit 1
fi

# ============================================================================
# ПРОВЕРКА И СБОРКА ОБРАЗА
# ============================================================================

# IMAGE_NAME="localhost/vllm-rocm:latest"

# ГОТОВЫЙ ОБРАЗ ОТ AMD (УЖЕ СКАЧАН!)
IMAGE_NAME="docker.io/rocm/vllm-dev:nightly_main_20251214"

# IMAGE_NAME="localhost/vllm-rocm:debug"

if ! podman images | grep -q "vllm-rocm"; then
    echo ""
    echo "╔════════════════════════════════════════╗"
    echo "║  Образ vllm-rocm не найден             ║"
    echo "║  Начинаю сборку (первый запуск)        ║"
    echo "║  ⏱️  Займёт 15-30 минут                ║"
    echo "╚════════════════════════════════════════╝"
    echo ""
    
    if [ ! -d "/tmp/vllm" ]; then
        echo "📥 Клонирование vLLM..."
        git clone https://github.com/vllm-project/vllm.git /tmp/vllm
    fi
        
    echo "🔨 Сборка образа vLLM для ROCm..."
    echo "   GPU архитектура: $GPU_ARCH"
    
    cd /tmp/vllm
    
    # КРИТИЧНО: --format docker для поддержки ONBUILD директив
    podman build \
        --format docker \
        -f docker/Dockerfile.rocm \
        --build-arg REMOTE_VLLM=0 \
        --build-arg ARG_PYTORCH_ROCM_ARCH="${GPU_ARCH}" \
        --target final \
        -t vllm-rocm:latest \
        . || {
        echo ""
        echo "❌ Ошибка сборки!"
        echo "Проверьте логи выше для деталей"
        exit 1
    }
    
    cd -
    echo -e "${GREEN}✅ Образ vllm-rocm:latest собран для ${GPU_ARCH}!${NC}"
else
    echo -e "${GREEN}✅ Образ vllm-rocm найден${NC}"
fi

# ============================================================================
# ОСТАНОВКА СТАРОГО КОНТЕЙНЕРА
# ============================================================================

echo ""
echo -e "${BLUE}🔄 Подготовка к запуску...${NC}"

# Проверка существования старого контейнера
if podman ps -a --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
    # Проверка запущен ли контейнер
    if podman ps --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        echo "🛑 Остановка запущенного контейнера: $CONTAINER_NAME"
        podman stop "$CONTAINER_NAME" > /dev/null 2>&1
        echo -e "${GREEN}✅ Контейнер остановлен${NC}"
    else
        echo "ℹ️ Контейнер существует (остановлен): $CONTAINER_NAME"
    fi
    
    echo "🗑️ Удаление старого контейнера..."
    podman rm "$CONTAINER_NAME" > /dev/null 2>&1
    echo "     ✅ Контейнер удалён"
else
    echo "ℹ️ Старые контейнеры не найдены (чистый запуск)"
fi


# ============================================================================
# УПРАВЛЕНИЕ MIOpen КЭШЕМ
# ============================================================================

echo ""
echo "🧹 Проверка MIOpen кэша..."
MIOPEN_CACHE="${HOME}/.cache/miopen"

if [ -d "$MIOPEN_CACHE" ]; then
    # Кэш существует
    CACHE_SIZE=$(du -sh "$MIOPEN_CACHE" 2>/dev/null | cut -f1)
    echo "  📂 Кэш найден: $MIOPEN_CACHE ($CACHE_SIZE)"
    
    # Проверяем флаг принудительной очистки
    if [ "$CLEAR_MIOPEN_CACHE" = "true" ]; then
        echo "  🗑️  Флаг CLEAR_MIOPEN_CACHE=true — удаление кэша..."
        rm -rf "$MIOPEN_CACHE"
        echo "     ✅ Кэш удалён (первый запуск будет медленным ~3-5 мин)"
    else
        echo "  ✅ Кэш сохранён (быстрый запуск ~30 сек)"
        echo "     💡 Для очистки: CLEAR_MIOPEN_CACHE=true ./start_vllm_rocm.sh ..."
    fi
else
    # Кэш отсутствует
    echo "  ℹ️  Кэш не найден (первый запуск)"
    echo "     ⏳ MIOpen будет компилировать kernels (~3-5 минут)"
    echo "     ✅ Следующие запуски будут быстрыми (~30 сек)"
fi



# ============================================================================
# Конфигурация моделей
# ============================================================================

MAX_LEN=""
MAX_SEQS=""
GPU_MEM=""
ENFORCE_EAGER="false"
ENABLE_PREFIX_CACHING="true"

# Специальные параметры для LightOnOCR
LIMIT_MM_PER_PROMPT=""
MM_PROCESSOR_CACHE_GB=""

case "$MODEL_NAME" in
    "HunyuanOCR")
        MAX_LEN=4096
        MAX_SEQS=1
        GPU_MEM=0.65
        ENFORCE_EAGER="true"
        ENABLE_PREFIX_CACHING="false"
        LIMIT_MM_PER_PROMPT='{"image": 1}'
        MM_PROCESSOR_CACHE_GB=0
        ;;
    
    "Qwen2-VL-2B-Instruct")
        MAX_LEN=16384
        MAX_SEQS=8
        GPU_MEM=0.75
        ENFORCE_EAGER="true"
        ;;
    
    "Qwen3-VL-8B-Instruct")
        MAX_LEN=8192
        MAX_SEQS=2
        GPU_MEM=0.80
        ENFORCE_EAGER="true"
        ;;
    
    "LightOnOCR-1B-1025")
        MAX_LEN=4096
        MAX_SEQS=4
        GPU_MEM=0.60
        ENFORCE_EAGER="true"
        # КРИТИЧНО для LightOnOCR (Pixtral архитектура)
        ENABLE_PREFIX_CACHING="false"
        LIMIT_MM_PER_PROMPT='{"image": 1}'
        MM_PROCESSOR_CACHE_GB="0"
        ;;
    
    "Llama-3.1-Nemotron-Nano-VL-8B-V1")
        MAX_LEN=16384
        MAX_SEQS=4
        GPU_MEM=0.70
        ENFORCE_EAGER="true"
        ;;
    
    *)
        echo -e "${YELLOW}⚠️  Неизвестная модель: $MODEL_NAME${NC}"
        echo "   Используем консервативные настройки"
        MAX_LEN=8192
        MAX_SEQS=8
        GPU_MEM=0.70
        ENFORCE_EAGER="true"
        ;;
esac

# Расчёт batched tokens
MAX_BATCHED_TOKENS=$((MAX_LEN * MAX_SEQS))

# ============================================================================
# Патч config.json для Qwen моделей
# ============================================================================

if [[ "$MODEL_NAME" == *"Qwen"* ]]; then
    CONFIG_FILE="${FULL_MODEL_PATH}/config.json"
    
    if [ -f "$CONFIG_FILE" ]; then
        CURRENT_VALUE=$(grep -o '"max_position_embeddings":[[:space:]]*[0-9]*' "$CONFIG_FILE" | grep -o '[0-9]*')
        
        if [ "$CURRENT_VALUE" != "$MAX_LEN" ]; then
            echo -e "  ${YELLOW}⚙️  Применение патча для Qwen модели...${NC}"
            sed -i "s/\"max_position_embeddings\":[[:space:]]*[0-9]*/\"max_position_embeddings\": $MAX_LEN/" "$CONFIG_FILE"
            echo -e "     ${GREEN}✅ max_position_embeddings: $CURRENT_VALUE → $MAX_LEN${NC}"
        fi
    fi
fi

# ============================================================================
# ВЫВОД ПАРАМЕТРОВ ЗАПУСКА
# ============================================================================

echo ""
echo "----------------------------------------"
echo "🚀 Запуск vLLM сервера"
echo "----------------------------------------"
echo " Контейнер:        $CONTAINER_NAME"
echo " Модель:           $MODEL_NAME"
echo " Порт:             $PORT"
echo " Max context:      $MAX_LEN токенов"
echo " Batch size:       $MAX_SEQS запросов"
echo " Batched tokens:   $MAX_BATCHED_TOKENS"
echo " GPU memory:       ${GPU_MEM}"
echo " Flash Attention:  ROCm optimized"

# Prefix caching статус
if [ "$ENABLE_PREFIX_CACHING" = "true" ]; then
    echo -e "Prefix caching: ${GREEN}Enabled ✅${NC}"
else
    echo -e "Prefix caching: ${RED}Disabled ❌${NC}"
fi
# Eager mode
if [ "$ENFORCE_EAGER" = "true" ]; then
    echo " Execution mode:   Eager (без CUDA graphs)"
    echo "                   ↳ Исправляет MIOpen ошибки на ROCm"
fi

echo " MM processor cache:   ${MM_PROCESSOR_CACHE_GB} GB"
echo " GPU Architecture:     ${GPU_ARCH}"

echo "----------------------------------------"


# ============================================================================
# ПОСТРОЕНИЕ АРГУМЕНТОВ vLLM
# ============================================================================

# Базовые аргументы
VLLM_ARGS=(
    "--model" "/models/${MODEL_NAME}"
    "--trust-remote-code"
    "--dtype" "bfloat16"
    "--attention-backend" "ROCM_ATTN"
    "--max-model-len" "$MAX_LEN"
    "--max-num-seqs" "$MAX_SEQS"
    "--max-num-batched-tokens" "$MAX_BATCHED_TOKENS"
    "--gpu-memory-utilization" "$GPU_MEM"
    "--disable-log-requests"
    "--port" "$PORT"
)

# Добавляем --enforce-eager для ROCm (если нужно)
if [ "$ENFORCE_EAGER" = "true" ]; then
    VLLM_ARGS+=("--enforce-eager")
    echo ""
    echo "⚠️  ВАЖНО: Режим Eager execution активирован"
    echo "   Это отключает CUDA graphs для совместимости с ROCm"
    echo ""
fi

# Для Qwen-VL принудительно ограничиваем длину контекста
if [[ "$MODEL_NAME" == *"Qwen"* ]]; then
    echo "⚠️  Qwen модель: Применение принудительного ограничения контекста"
    # Переопределяем max_position_embeddings через config
    VLLM_ARGS+=("--max-model-len" "$MAX_LEN")
    echo "   ↳ Контекст ограничен до $MAX_LEN токенов"
fi

# Добавляем limit-mm-per-prompt
VLLM_ARGS+=("--limit-mm-per-prompt" "$LIMIT_MM_PER_PROMPT")

# Добавляем mm-processor-cache-gb
VLLM_ARGS+=("--mm-processor-cache-gb" "$MM_PROCESSOR_CACHE_GB")

# ✅ КРИТИЧНО: Prefix caching
if [ "$ENABLE_PREFIX_CACHING" = "false" ]; then
    # ОТКЛЮЧАЕМ prefix caching для VLM
    # Используем флаг без значения (boolean flag)
    echo "⚠️  Отключаем prefix caching (для VLM моделей)"
    # Внимание: В vLLM 0.13+ используется --no-enable-prefix-caching
    # Но в некоторых версиях это может быть --disable-prefix-caching
    # Проверьте вашу версию: vllm --help | grep prefix
    VLLM_ARGS+=("--no-enable-prefix-caching")
    
    # Для большинства версий:
    # Prefix caching отключен по умолчанию, НО для явности:
    # НЕ добавляем --enable-prefix-caching = отключено!
else
    # Включаем prefix caching (для обычных LLM)
    VLLM_ARGS+=("--enable-prefix-caching")
fi

# ============================================================================
# ЗАПУСК КОНТЕЙНЕРА
#
# -e HIP_FORCE_DEV_KERNARG=1 
# -e HIP_VISIBLE_DEVICES=0              # Использовать GPU 0
# -e HSA_OVERRIDE_GFX_VERSION=11.0.0    # Для RDNA 3 (RX 7800 XT)
# -e PYTORCH_ROCM_ARCH=gfx1101          # Архитектура RX 7800 XT
# -e VLLM_ATTENTION_BACKEND=ROCM_ATTN   # ROCm оптимизированный attention
#
# -e MIOPEN_DISABLE_CACHE=0             # Включить кэш (быстрее)
# -e MIOPEN_DEBUG_DISABLE_FIND_DB=0     # Использовать Find DB
# -e MIOPEN_FIND_MODE=NORMAL            # Нормальный режим поиска
# -e MIOPEN_LOG_LEVEL=3                 # Уровень логирования
#
# -e HSA_ENABLE_INTERRUPT=0             # Отключить прерывания (меньше hang'ов)
# -e HSA_ENABLE_SDMA=0                  # Отключить SDMA (источник багов RDNA3)
# -e HSA_XNACK=0                        # Отключить XNACK (память)
# -e GPU_MAX_HW_QUEUES=4                # Ограничить очереди GPU
# -e AMD_SERIALIZE_KERNEL=3             # Сериализовать kernel'ы (нет конфликтов)
# -e AMD_SERIALIZE_COPY=3               # Сериализовать копирование
#
# -e PYTORCH_ALLOC_CONF="expandable_segments:False" \ # ✅ MEMORY ALLOCATOR (PyTorch 2.9+)
#
# -e HSA_TOOLS_LIB=/opt/rocm/lib/librocm-debug-agent.so  # Debug agent
#
# ДЛЯ ПАМЯТИ (против OOM):
# -e TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1  # ✅ Flash Attention
# -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True  # ✅ Фрагментация
#
# 📊 TUNABLE OPERATIONS (для лучшей производительности)` \
# -e PYTORCH_TUNABLEOP_ENABLED=1 \
# -e PYTORCH_TUNABLEOP_TUNING=1 \
# ============================================================================

echo ""
echo -e "${BLUE}🐳 Запуск контейнера...${NC}"

podman run -d \
    --name "$CONTAINER_NAME" \
    --network=host \
    --device /dev/kfd \
    --device /dev/dri \
    --ipc=host \
    --cap-add=SYS_PTRACE \
    --security-opt=seccomp=unconfined \
    --security-opt=label=disable \
    -v "${MODEL_PATH}:/models:Z" \
    -e HIP_VISIBLE_DEVICES=0 \
    -e HSA_OVERRIDE_GFX_VERSION=11.0.0 \
    -e PYTORCH_ROCM_ARCH="${GPU_ARCH}" \
    -e SAFETENSORS_FAST_GPU=1 \
    -e VLLM_WORKER_MULTIPROC_METHOD=spawn \
    -e MIOPEN_DISABLE_CACHE=0 \
    -e MIOPEN_DEBUG_DISABLE_FIND_DB=0 \
    -e MIOPEN_FIND_MODE=NORMAL \
    -e MIOPEN_LOG_LEVEL=3 \
    -e HSA_ENABLE_INTERRUPT=0 \
    -e HSA_TOOLS_LIB=/opt/rocm/lib/librocm-debug-agent.so \
    -e HSA_ENABLE_SDMA=0 \
    -e GPU_MAX_HW_QUEUES=4 \
    -e AMD_SERIALIZE_KERNEL=3 \
    -e AMD_SERIALIZE_COPY=3 \
    -e HSA_XNACK=0 \
    -e TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1 \
    -e PYTORCH_ALLOC_CONF="expandable_segments:False" \
    -e PYTORCH_TUNABLEOP_ENABLED=1 \
    "$IMAGE_NAME" \
    python3 -m vllm.entrypoints.openai.api_server "${VLLM_ARGS[@]}"

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}❌ Не удалось запустить контейнер!${NC}"
    echo ""
    echo "Возможные причины:"
    echo "  1. Порт $PORT уже занят"
    echo "  2. Недостаточно VRAM"
    echo "  3. Проблемы с ROCm драйверами"
    echo ""
    echo "Диагностика:"
    echo "  ss -tulpn | grep $PORT          # Проверить порт"
    echo "  rocm-smi                         # Проверить GPU"
    echo "  podman logs $CONTAINER_NAME      # Логи контейнера"
    exit 1
fi

echo -e "${GREEN}✅ Контейнер запущен${NC}"

# ============================================================================
# МОНИТОРИНГ ЗАПУСКА
# ============================================================================

echo ""
echo "⏳ Запуск сервера (загрузка модели ~1-3 мин)..."
sleep 5

# Логи в фоне
podman logs -f "$CONTAINER_NAME" > "$LOG_FILE" 2>&1 &
LOG_PID=$!

# Ожидание готовности с проверкой состояния
ATTEMPTS=0
MAX_ATTEMPTS=180

echo ""
echo "⏳ Ожидание готовности API..."

while [ $ATTEMPTS -lt $MAX_ATTEMPTS ]; do
    # Проверка health endpoint
    if curl -s http://localhost:$PORT/health > /dev/null 2>&1; then
        echo ""
        echo "----------------------------------------"
        echo "✅ Сервер готов!"
        echo "----------------------------------------"
        break
    fi
    
    # Проверка что контейнер всё ещё запущен
    if ! podman ps | grep -q "$CONTAINER_NAME"; then
        echo ""
        echo "----------------------------------------"
        echo "❌ КОНТЕЙНЕР ОСТАНОВИЛСЯ!"
        echo "----------------------------------------"
        echo ""
        echo "Последние 50 строк логов:"
        echo "----------------------------------------"
        podman logs --tail 50 "$CONTAINER_NAME"
        echo "----------------------------------------"
        echo ""
        echo "Полные логи: cat $LOG_FILE"
        kill $LOG_PID 2>/dev/null
        exit 1
    fi
    
    ATTEMPTS=$((ATTEMPTS + 1))
    
    # Прогресс каждые 10 секунд
    if [ $((ATTEMPTS % 10)) -eq 0 ]; then
        echo "  ⏳ Загрузка модели... ($ATTEMPTS/180 сек)"
    fi
    
    sleep 1
done

# Таймаут
if [ $ATTEMPTS -eq $MAX_ATTEMPTS ]; then
    echo ""
    echo "----------------------------------------"
    echo "⚠️  ТАЙМАУТ: Сервер не ответил за 3 минуты"
    echo "----------------------------------------"
    echo ""
    echo "Возможные причины:"
    echo "  - Модель слишком большая для VRAM"
    echo "  - MIOpen всё ещё компилирует kernels (первый запуск)"
    echo "  - Проблемы с ROCm драйверами"
    echo ""
    echo "Проверьте логи:"
    echo "  podman logs $CONTAINER_NAME | tail -100"
    echo "  tail -f $LOG_FILE"
    echo ""
fi

# ============================================================================
# ФИНАЛЬНЫЙ ОТЧЁТ
# ============================================================================

echo ""
echo "----------------------------------------"
echo "📊 ИНФОРМАЦИЯ О СЕРВЕРЕ"
echo "----------------------------------------"
echo "📦 Контейнер:     $CONTAINER_NAME"
echo "🔌 Порт:          $PORT"
echo "🌐  API:           http://localhost:$PORT/v1"
echo "📚 Docs:          http://localhost:$PORT/docs"
echo "❤️ Health:        http://localhost:$PORT/health"
echo ""
echo "📋 Команды управления:"
echo "----------------------------------------"
echo "  Логи (live):    podman logs -f $CONTAINER_NAME"
echo "  Логи (файл):    tail -f $LOG_FILE"
echo "  Статус:         podman ps | grep $CONTAINER_NAME"
echo "  Остановка:      podman stop $CONTAINER_NAME"
echo "  Удаление:       podman rm $CONTAINER_NAME"
echo ""
echo "🧪 Тестовый запрос:"
echo "----------------------------------------"
echo "  curl http://localhost:$PORT/v1/models"
echo "----------------------------------------"
echo ""

# Специальная инструкция для LightOnOCR
if [ "$MODEL_NAME" = "LightOnOCR-1B-1025" ]; then
    echo "💡 ВАЖНО для LightOnOCR:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  В API запросах НЕ используйте текстовый промпт!"
    echo "  Отправляйте ТОЛЬКО изображение в messages:"
    echo ""
    echo '  messages = [{'
    echo '      "role": "user",'
    echo '      "content": [{'
    echo '          "type": "image_url",'
    echo '          "image_url": {"url": "data:image/png;base64,..."}' 
    echo '      }]'
    echo '  }]'
    echo ""
fi
