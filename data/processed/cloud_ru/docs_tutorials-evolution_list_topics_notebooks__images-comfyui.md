---
source_image: docs_tutorials-evolution_list_topics_notebooks__images-comfyui.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 119.89
tokens: 8455
characters: 4572
timestamp: 2025-12-24T06:14:14.782797
finish_reason: stop
---

### Генерация изображений с ComfyUI на основе Notebooks

С помощью этого руководства вы научитесь настраивать среду для генерации изображений с помощью ComfyUI, загружать модели с платформы Hugging Face и создавать изображения на основе текстовых промптов.

Вы будете использовать следующие сервисы:

• **Notebooks** — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

• **Object Storage** — объектное S3-хранилище с бесплатным хранением файлов, объемом до 15 ГБ.

• **Hugging Face** — платформа с открытым исходным кодом и сообщество разработчиков, ориентированное на машинное обучение, обработку естественного языка (NLP) и другие области искусственного интеллекта.

• **ComfyUI** — визуальная среда для создания и запуска процессов генерации контента на основе моделей диффузии.

Шаги:

1. Подготовьте среду.
2. Загрузите модель из Hugging Face.
3. Сгенерируйте изображение.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен. Если сервис Notebooks не подключен, оставьте заявку на подключение.

1. Подготовьте среду

1. Для хранения модели создайте бакет в Object Storage, если не сделали этого ранее.
2. Создайте ноутбук со следующими параметрами:
   • Конфигурация — GPU.
   • Образ — Cloud.ru Jupyter ComfyUI.
   • Том — укажите бакет для хранения модели.

2. Загрузите модель из Hugging Face

1. Откройте созданный ноутбук.
2. Выберите тип ноутбука Python 3 .
3. Загрузите модель в бакет S3 или напрямую в ноутбук:

Загрузка модели в бакет Object Storage    Загрузка модели в ноутбук

1. Загрузите модель в бакет S3:
   !wget <model-address>
   -O <bucket-address>

Где:
• <model-address> — адрес модели в репозитории Hugging Face.
• <bucket-address> — адрес бакета в Object Storage.
Пример:
!wget https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/resolve/main/v1-5-pruned-64/mt-43/notebook/comfy_models/v1-5-pruned-emaonly-fp16.safetensors

2. Создайте символьскую ссылку для доступа к модели из ComfyUI:
   ln -s /mnt/s3/notebook/comfy_models/v1-5-pruned-emaonly-fp16.safetensors /comfyui/models/checkpoints/v1-5-pruned-emaonly-fp16.safetensors

3. Сгенерируйте изображение в ComfyUI

1. Перейдите в модуль Comfy UI.
2. В правом верхнем углу откройте шаблоны Рабочий процесс → Посмотреть шаблоны.
3. Выберите шаблон Генерация изображений.

![Интерфейс ComfyUI](https://i.imgur.com/1234567.png)

Интерфейс ComfyUI состоит из нод, которые соединены между собой в единый рабочий процесс. Ноды отвечают за разные этапы генерации изображения. Например, промпт для генерации необходимо ввести в поле ноды Кодирование текста CLIP (Запрос).

![Диаграмма нод ComfyUI](https://i.imgur.com/7654321.png)

4. В поле ноды Кодирование текста CLIP (Запрос) укажите текстовый промпт для генерации изображения.

Пример позитивного промпта:

a highly detailed futuristic humanoid robot
3/4 view
standing in a thoughtful pose while solving a complex problem
intricate mechanical parts
glowing blue circuitry and transparent alloy panels
expressive LED eyes reflecting data streams
ultra realistic skin like polymer texture
subtle steam and dust particles around the joints
soft ambient lighting
depth of field focusing on the robot's face
background: a sprawling megacity of the future with towering neon lit skyscrapers
floating traffic lanes
holographic billboards
misty evening atmosphere
neon pink and cyan color palette
hyper realistic
photorealistic
ultra detailed
8k
award winning concept art
trending on ArtStation

Пример негативного промпта:

low res
blurry
jpeg artifacts
watermark
text
logo
cropping
deformed hands
extra limbs
ugly
poorly drawn
unrealistic anatomy
over exposed
underexposed
flat lighting

5. При необходимости скорректируйте параметры в других нодах.
6. Нажмите Запустить.

Запустится процесс генерации изображения. Если процесс не запустился, обновите страницу и повторите попытку.

Сгенерированное изображение появится в блоке Save Image и будет сохранено в директории /comfyui/output .

Результат

В результате выполнения практической работы вы запустили Notebooks с визуальной средой для запуска генеративных нейронных сетей ComfyUI, подключили объектное хранилище для хранения моделей и сгенерировали первое изображение.

Далее вы можете экспериментировать с другими моделями, добавлять ноды и усложнять рабочий процесс. Подробную информацию о работе с ComfyUI можно узнать в официальной документации.