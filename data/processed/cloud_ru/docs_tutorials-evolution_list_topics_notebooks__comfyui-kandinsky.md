---
source_image: docs_tutorials-evolution_list_topics_notebooks__comfyui-kandinsky.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 183.48
tokens: 13074
characters: 6715
timestamp: 2025-12-24T06:10:07.852540
finish_reason: stop
---

### Генерация видео с моделью Kandinsky 5.0 Video Lite в ComfyUI на основе Notebooks

Эта статья полезна?

С помощью этого руководства вы настроите среду для генерации видео в ComfyUI с использованием модели Kandinsky 5.0 Video Lite в сервисе Notebooks.

В результате вы получите практический опыт работы с визуальной средой ComfyUI, управлением моделями и генерацией видео в облаке Cloud.ru Evolution.

Вы будете использовать следующие сервисы:

• **Notebooks** — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
• **Object Storage** — объектное S3-хранилище с бесплатным хранением файлов, объемом до 15 ГБ.
• **Hugging Face** — платформа с открытым исходным кодом и сообщество разработчиков, ориентированное на машинное обучение, обработку естественного языка (NLP) и другие области искусственного интеллекта.
• **ComfyUI** — визуальная среда для создания и запуска процессов генерации контента на основе моделей диффузии.

Шаги:

1. Подготовьте среду.
2. Загрузите модели Kandinsky 5.0 Video Lite.
3. Сгенерируйте видео с моделью Kandinsky 5.0 Video Lite в ComfyUI.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен. Если сервис Notebooks не подключен, оставьте заявку на подключение.
3. Убедитесь, что для сервиса Notebooks установлена квота на GPU. Для расширения квоты обратитесь в техническую поддержку.

1. Подготовьте среду

На этом шаге вы создадите бакет для хранения моделей и ноутбук с GPU и предустановленным ComfyUI. Это обеспечит стабильную и производительную среду для генерации видео.

1. Для хранения модели создайте бакет в Object Storage.
2. Создайте ноутбук со следующими параметрами:
   • Конфигурация — GPU.
   • Образ — Cloud.ru Jupyter ComfyUI Kandinsky 5 Video Lite.
   • Хранилища — укажите бакет, созданный ранее.

2. Загрузите модели Kandinsky 5.0 Video Lite

На этом шаге вы загрузите компоненты модели Kandinsky 5.0 Video Lite в выбранное хранилище — либо в бакет Object Storage, либо локально в ноутбук. Использование бакета позволяет сохранять модели между перезапусками ноутбука.

1. Откройте созданный ноутбук.
2. Запустите терминал.
3. Загрузите модель в бакет S3 или напрямую в ноутбук:

Загрузка модели в бакет Object Storage
Загрузка модели в ноутбук

Выполните скрипт в терминале, предварительно указав название вашего бакета в <bucket_name>:

# Activate the base environment
conda activate base

# Set the path to the bucket, e.g. /mnt/s3/<BUCKET_NAME>/kandinsky/weights
export KS_WEIGHTS_DIR="/mnt/s3/<bucket_name>/kandinsky/weights" COMFY_MODELS_DIR="/comfyui/model"

# Create directory and change into it
mkdir -p $KS_WEIGHTS_DIR && cd $KS_WEIGHTS_DIR

# Download models
python3 /comfyui/custom_models/kandinsky/download_models.py

# Create symbolic links for text_encoder (OpenVQA2.5-ViT-TM-Instruct)
for file in model-00001...5-of-00005.safetensors; do \
    ln -fs "$KS_WEIGHTS_DIR/text_encoder/${file}" "/comfyui/models/text_encoders/text_encoder/" \
done

# Create symbolic links for text_encoder2 (openai/clip-vit-large-patch14)
for file in "tf_model.85","pytorch_model.bin","model.safetensors","flax_model.msgpack"; \
    ln -fs "$KS_WEIGHTS_DIR/text_encoder2/${file}" "/comfyui/models/text_encoders/text_encoder2/"

# Create symbolic link for VAE (hunyuvideo-community/HunyuanVideo)
ln -fs "$KS_WEIGHTS_DIR/vae/diffusion_pytorch_model.safetensors" "/comfyui/models/vae/vae/"

# Create symbolic links for Kandinsky5Lite_T2V models
ln -fs "$KS_WEIGHTS_DIR/model/kandinsky5lite_t2v_distilled160step_5s.safetensors" $COMFY_MODEL
ln -fs "$KS_WEIGHTS_DIR/model/kandinsky5lite_t2v_sft_5s.safetensors" $COMFY_MODELS_DIR

3. Сгенерируйте видео с моделью Kandinsky 5.0 Video Lite в ComfyUI

На этом шаге вы запустите рабочий процесс генерации видео в ComfyUI, используя загруженные модели. Вы сможете настроить промпты, запустить генерацию и получить результат.

1. В интерфейсе ноутбука перейдите в модуль Comfy UI.
2. В левом верхнем углу нажмите Рабочий процесс → Посмотреть шаблоны.
3. Выберите один из доступных шаблонов:
   • Kandinsky 5.0 T2V Lite SFT 5s — обеспечивает лучшее качество.
   • Kandinsky 5.0 T2V Lite distill 5s — работает в 6 раз быстрее с минимальной потерей качества.

![Интерфейс ComfyUI с шаблонами](https://i.imgur.com/1.png)

Интерфейс ComfyUI состоит из модулей, которые соединены между собой в единый рабочий процесс. Ноды отвечают за разные этапы генерации изображений и видео.

![Диаграмма нод ComfyUI](https://i.imgur.com/2.png)

4. В поле ноды expand_prompt введите на русском или английском языке текстовый промпт — описание сцены, которую хотите сгенерировать.

Чем детальнее описание, тем точнее результат. Укажите объекты, действия, стиль, освещение.

Пример промпта:

A 1980s Soviet computing lab.
Green glow fills the room from massive mainframes.
A scientist in a white coat watches a monochrome monitor.
In bold, flickering green letters, the words written and pulse at the center of the screen surrounded by reels spin.

5. В поле ноды Kandinsky5TextEncode укажите негативный промпт — элементы, которые нужно исключить из генерации.

Пример негативного промпта:

Static
2D cartoon
2d animation
paintings
images
worst quality
low quality
ugly
deformed
walking backwards

6. Нажмите Запустить.

Запустится процесс генерации видео. Если процесс не запустился, обновите страницу и повторите попытку.

7. Дождитесь завершения генерации.

Причина
Первый запуск может занимать больше времени из-за инициализации GPU и загрузки модели. Последующие запуски будут быстрее.

Чтобы отслеживать процесс, в консоли отладки нажмите Переключить нижнюю панель.

![Консоль отладки ComfyUI](https://i.imgur.com/3.png)

Сгенерированное видео появится в node Сохранить анимированный WEBP и в очереди генерации.

![Сгенерированное видео](https://i.imgur.com/4.png)

Оригинал файла будет сохранен в директории /comfyui/output/.

Причина
ComfyUI поддерживает очередь генерации. Вы можете добавить несколько промптов подряд для непрерывной обработки.

Пример сгенерированного видео:

![Пример сгенерированного видео](https://i.imgur.com/5.png)

Результат

В ходе практической работы вы:
• настроили среду в сервисе Notebooks;
• загрузили модель Kandinsky 5.0 Video Lite;
• освоили работу с ComfyUI;
• использовали GPU-ускорение;
• настроили хранение моделей в облаке;
• сгенерировали видео на основе текстового описания.

Далее вы можете экспериментировать с другими версиями модели Kandinsky 5.0 Video Lite и менять параметры генерации. Подробную информацию о модели Kandinsky 5 можно узнать в официальном репозитории.