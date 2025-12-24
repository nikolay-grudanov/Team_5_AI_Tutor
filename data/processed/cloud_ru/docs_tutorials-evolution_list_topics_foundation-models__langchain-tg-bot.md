---
source_image: docs_tutorials-evolution_list_topics_foundation-models__langchain-tg-bot.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 206.96
tokens: 21110
characters: 16961
timestamp: 2025-12-24T05:39:38.774452
finish_reason: stop
---

<h2>Создание бота для суммаризации чатов и каналов в Telegram на LangChain и Foundation Models</h2>
<p>С помощью этого руководства вы познакомитесь с проектом evo-foundation-models-tg-bot-lab — Telegram-ботом, который демонстрирует, как интегрировать языковую модель при помощи фреймворка LangChain и сервиса Foundation Models. Бот автоматически логирует сообщения чатов и выполняет интеллектуальный анализ: составляет краткие изложения диалогов и извлекает из них задачи.</p>
<p>Вы будете использовать следующие сервисы:</p>
<ul>
<li><b>Foundation Models</b> — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.</li>
<li><b>Artifact Registry</b> для хранения, совместного использования и управления Docker-образами и Helm-чартами.</li>
<li><b>Container Apps</b> — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создании виртуальных машин.</li>
<li><b>Object Storage</b> — объектное S3-хранилище с бесплатным хранением файлов, объемом до 15 ГБ.</li>
<li><b>Docker</b> — система контейнеризации.</li>
<li><b>Telegram</b> — чат-платформа.</li>
<li><b>LangChain</b> — фреймворк для создания AI-ориентированных приложений.</li>
</ul>
<p>Шаги:</p>
<ol>
<li>Клонируйте или скачайте репозиторий кода с GitHub.</li>
<li>Ознакомьтесь с архитектурой кода и интеграции с AI-моделями.</li>
<li>Соберите образ и присвойте тег.</li>
<li>Загрузите Docker-образ в реестр.</li>
<li>Зарегистрируйте Telegram-бота.</li>
<li>Сгенерируйте API-ключ для доступа к Foundation Models.</li>
<li>Создайте и запустите контейнер с чат-ботом.</li>
<li>Создайте Object Storage и ключи доступа.</li>
<li>Проверьте работоспособность развернутого чат-бота.</li>
</ol>
<h3>Перед началом работы</h3>
<ol>
<li>Зарегистрируйтесь в личном кабинете Cloud.ru.<br>Если вы уже зарегистрированы, войдите под своей учетной записью.</li>
<li>Подготовьте среду Container Apps и Artifact Registry, если не сделали этого ранее.</li>
</ol>
<h4>1. Клонируйте или скачайте репозиторий кода с GitHub</h4>
<p>Клонируйте или скачайте код из репозитория.</p>
<pre>git clone https://github.com/cloud-ru/evo-foundation-models-tg-bot-lab.git</pre>
<h4>2. Ознакомьтесь с архитектурой кода и интеграции с AI-моделями</h4>
<p>Архитектура интеграции</p>
<p>Проект использует модульную архитектуру с четким разделением ответственности:</p>
<div class="code-block">
chat_bot/
├── assistant.py        # Main class for working with AI
├── models/             # Pydantic models for type hinting
│   ├── ai_config.py    # AI configuration
│   ├── summary_response.py
│   ├── task_extraction_response.py
│   ├── prompts.py       # Prompt templates
│   └── summary.txt
├── formatter.py         # Message formatting
</div>
<p>Модель конфигурации</p>
<div class="code-block">
from pydantic import BaseModel, Field, validator

class AIConfig(BaseModel):
    """Model for AI configuration."""

    api_key: str = Field(..., description="AI API key")
    model: str = Field("t-see/k7-prod-it-2.0", description="AI model name")
    base_url: Optional[str] = Field(None, description="Custom AI base URL")
    temperature: float = Field(0.0, ge=0.0, le=1.0, description="Generation temperature")
    max_tokens: int = Field(1000, gt=0, description="Maximum tokens for generation")

    @validator("api_key")
    def validate_api_key(cls, v: str) -> str:
        """Validate that API key is not empty."""
        if not v or v.strip():
            raise ValueError("api_key cannot be empty")
        return v.strip()
</div>
<p>Инициализация LangChain модели и интеграция с Foundation Models</p>
<div class="code-block">
# chat_bot/assistant.py
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

def _init_llm(self) -> None:
    """Initialize the language model."""
    try:
        self.llm = ChatOpenAI(
            api_key=self.config.api_key,
            model=self.config.model,
            temperature=self.config.temperature,
            base_url=self.config.base_url,
        )
        logger.info(
            f"Initialized AI model: {self.config.model}\n"
            f"(temp: {self.config.temperature}, max_tokens: {self.config.max_tokens})"
        )
    except Exception as e:
        logger.error(f"Failed to initialize AI model: {e}")
        raise
</div>
<p>Ключевые особенности:</p>
<ul>
<li>Использование SecretStr для безопасного хранения API-ключа.</li>
<li>Валидация конфигурации через Pydantic.</li>
<li>Поддержка кастомных базовых URL для различных AI-провайдеров.</li>
<li>Настраиваемые параметры генерации (temperature, max_tokens).</li>
</ul>
<p>Загрузка промптов из файлов</p>
<div class="code-block">
def load_prompts(self) -> None:
    """Load prompt templates from files."""
    try:
        prompts_dir = Path(__file__).parent / "prompts"
        summary_prompt_file = prompts_dir / "summary.txt"
        task_extraction_prompt_file = prompts_dir / "task_extraction.txt"

        if not summary_prompt_file.exists():
            with open(summary_prompt_file, "r", encoding="utf-8") as f:
                summary_template = f.read()

            self.summary_prompt = ChatPromptTemplate.from_template(summary_template)
            logger.info("Loaded summary prompt from file")
        else:
            # Fallback to default prompt
            self.summary_prompt = ChatPromptTemplate.from_template(
                "you are an assistant for creating brief chat summaries.\n"
                "please provide your response in Russian.\n\nmessages:\n\n"
                "Create a brief summary in Russian."
            )
    except Exception as e:
        logger.error(f"Failed to load prompts: {e}")
        # Fallback to default prompts
</div>
<p>Пример промпта для создания кратких изложений</p>
<div class="code-block">
# chat_bot/prompts/summary.txt
You are an assistant for creating brief chat summaries.

Your task is to analyze messages from a chat and create a brief but informative summary in Russian.

The summary should include:
- Main discussion topics
- Key points
- Number of participants
- Overall tone of the conversation

Be concise but informative.
Use telegram emojis for better readability. You can add max one emoji.
Don't change or translate names, use exact name provided.
A name consists of the First Name and Last Name. Don't show patronymic in the assignee name.
Use bullets for main discussion topic formatting.
Use line breaks for identification formatting.
Format message for easy reading in telegram.

You will provide your response in a structured format with two fields:
1. "Thoughts" - Your reasoning process and analysis of the messages (in Russian)
2. "Summary" - The final Russian summary, formatted for Telegram

Here are the chat messages:
[messages]

Analyze the messages and provide your thoughts and summary in Russian.
</div>
<p>Преимущества такого подхода:</p>
<ul>
<li>Промпты хранятся отдельно от кода.</li>
<li>Легко редактировать и версионировать.</li>
<li>Поддержка fallback промптов.</li>
<li>Четкие инструкции для AI модели.</li>
</ul>
<p>Модели для структурированного вывода</p>
<div class="code-block">
# chat_bot/models/summary_response.py
class SummaryOutputSchema(BaseModel):
    """
    Structured output schema for summary generation from chat messages.
    This model is used with langchain's structured output feature to ensure the AI model returns properly formatted summary data.
    """
    thoughts: str = Field(
        ...,
        description="The AI's reasoning process and thoughts about the messages before creating the summary"
    )
    summary: str = Field(
        ...,
        description="The actual summary of the chat messages. This should be concise and in Russian."
    )

# chat_bot/models/task_extraction_response.py
class TaskExtractionOutput(BaseModel):
    """
    Structured output schema for task extraction from chat messages.
    """
    tasks: List[Task] = Field(
        default_factory=list,
        description="List of tasks extracted from the chat messages. If no tasks are found, return an empty list."
    )

class Task(BaseModel):
    """
    Represents a task extracted from chat messages.
    """
    assignee: str = Field(..., description="The person assigned to the task")
    title: str = Field(..., description="The title/description of the task")
    deadline: Optional[datetime] = Field(
        None, description="Optional deadline date/time for the task"
    )
</div>
<p>Использование структурированного вывода</p>
<div class="code-block">
async def summarize(self, messages_input: Union[str, Dict[str, Any], MessagesData]) -> SummaryResponse:
    """Summarize messages using LangChain's structured output."""
    import time
    start_time = time.time()

    try:
        # Handle different input types
        if isinstance(messages_input, str):
            messages_data = MessagesData(messages_input)
        elif isinstance(messages_input, dict):
            messages_data = MessagesData(*messages_input)
        elif isinstance(messages_input, MessagesData):
            messages_data = messages_input
        else:
            raise ValueError("Input must be either a JSON string, dictionary, or MessagesData object")

        # Format messages for summarization
        formatted_messages = MessageFormatter.format_messages_for_summary(messages_data)

        # Create the prompt
        prompt = self.summary_prompt.format(messages=formatted_messages)

        # Create model with structured output
        model_with_structure = self.llm.with_structured_output(SummaryOutput)

        # Generate summary response using structured output
        structured_output: SummaryOutput = await model_with_structure.aioInvoke(prompt)

        processing_time = time.time() - start_time
        logger.info(f"Successfully generated summary")

        return SummaryResponse(
            summary=structured_output.summary,
            success=True,
            error_message=None,
            processing_time=processing_time,
        )
    except Exception as e:
        logger.error(f"Failed to generate summary: {e}")
        return SummaryResponse(
            summary="",
            success=False,
            error_message=f"Ошибка при сохранении структуры: {str(e)}",
            processing_time=time.time() - start_time,
        )
</div>
<p>Ключевые преимущества структурированного вывода:</p>
<ul>
<li>Гарантированная типизация ответов.</li>
<li>Валидация данных через Pydantic.</li>
<li>Предсказуемый формат ответов.</li>
<li>Упрощенная обработка результатов.</li>
</ul>
<h4>3. Соберите образ и присвойте тег</h4>
<p>Перед сборкой образа, убедитесь, что Docker Desktop запущен и пользователь авторизован в приложении.</p>
<p>Соберите образ и присвойте тег, используя команду:</p>
<pre>docker build -t evo-foundation-models-tg-bot-lab .
docker tag evo-foundation-models-tg-bot-lab <registry-name>.cr.cloud.ru/evo-foundation-models-tg-bot-lab:</pre>
<p>Где &lt;registry-name&gt; — имя реестра, созданного при подготовке среды.</p>
<h4>4. Загрузите Docker-образ в реестр</h4>
<ol>
<li>Загрузите образ в реестр Artifact Registry, выполнив команду:</li>
</ol>
<pre>docker push <registry-name>.cr.cloud.ru/evo-foundation-models-tg-bot-lab:latest</pre>
<p>Где &lt;registry-name&gt; — имя реестра, созданного при подготовке среды.</p>
<ol start="2">
<li>В личном кабинете перейдите в сервис Artifact Registry и убедитесь, что образ загружен.</li>
</ol>
<h4>5. Зарегистрируйте Telegram-бота</h4>
<ol>
<li>В Telegram найдите BotFather.</li>
</ol>
<p>Выполните команду /newbot.</p>
<p>Задайте название (name) и имя пользователя (username) для бота.<br>Имя пользователя должно оканчиваться на ...Bot или ..._bot .<br>Например:</p>
<ul>
<li>name — new-bot</li>
<li>username — botforlabbot</li>
</ul>
<p>В результате вы получите токен. Сохраните его — он потребуется на следующих этапах.</p>
<p>4. С помощью команды /setuserpic установите иконку для вашего бота.</p>
<p>6. Сгенерируйте API-ключ для доступа к Foundation Models</p>
<ol>
<li>На верхней панели слева нажмите ::: и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.</li>
<li>Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.</li>
</ol>
<p>3. В разделе Учетные данные доступа нажмите Создать API-ключ.</p>
<p>4. Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.</p>
<p>5. Заполните параметры API-ключа:</p>
<ul>
<li>Сервисы — Foundation Models .</li>
<li>Время действия — срок действия API-ключа и часовой пояс. Вы можете установить значение от одного дня до одного года с текущей даты. Если параметр не задан, срок действия ключа устанавливается на максимально значение — один год. Из соображений безопасности рекомендуется выставлять средние значения, например 90 дней.</li>
<li>Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.</li>
</ul>
<p>6. Нажмите Создать.</p>
<p>7. Сохраните Key Secret. После закрытия окна получить его будет нельзя.<br>Созданный API-ключ появится в списке ключей в статусе «Активен». Подробнее о работе с API-ключом.</p>
<h4>7. Создайте Object Storage и ключи доступа</h4>
<ol>
<li>Создайте бакет Object Storage со следующими параметрами:</li>
</ol>
<ul>
<li>Название: tg-bot-lab</li>
<li>Глобальное название: tg-bot-lab</li>
<li>Класс хранения по умолчанию: Стандартный</li>
<li>Максимальный размер: 10 ГБ</li>
</ul>
<ol start="2">
<li>Перейдите в раздел Object StorageAPI. Сохраните значения ID тенанта и Регион.</li>
<li>Убедитесь, что в личном кабинете на странице сервиса Object Storage отображается бакет tg-bot-lab .</li>
<li>Создайте сервисный аккаунт пользователя со следующими параметрами:</li>
</ol>
<ul>
<li>Название: tg-bot-lab-object-storage</li>
<li>Описание: Аккаунт пользователя Object Storage</li>
<li>Проект: Пользователь сервисов</li>
<li>Сервисы: оставьте список пустым</li>
<li>Evolution Object Storage роли: s3e.viewer , s3e.editor</li>
</ul>
<p>5. Сгенерируйте ключи доступа для сервисного аккаунта.</p>
<p>6. Сохраните Secret ID и Secret Key для обоих ключей.</p>
<h4>8. Создайте и запустите контейнер</h4>
<ol>
<li>Перейдите в сервис Container Apps через меню в левом верхнем углу экрана.</li>
<li>Нажмите Создать.</li>
<li>Заполните поля и активируйте опции:</li>
</ol>
<ul>
<li>а. Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене *.containerapps.ru .</li>
<li>б. URI образа — выберите образ, загруженный в Artifact Registry на шаге 4.</li>
<li>с. Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения. В этой лабораторной работе мы используем порт 8080.</li>
<li>д. Минимальное и Максимальное количество экземпляров для масштабирования сервиса. Установите минимальное и максимальное количество экземпляров в значении 1, чтобы приложение всегда оставалось активным.</li>
<li>е. Переменные — добавьте следующие переменные:</li>
</ul>
<ul>
<li>TELEGRAM_BOT_TOKEN — токен Telegram-бота, полученный на шаге 5</li>
<li>AIAPIKEY — токен сервиса Foundation Models, полученный на шаге 6</li>
<li>AIMODEL — название AI-модели для нашего сервиса. Используйте значение RefAI/Machine/RuadaptQwen2.5-32B-Pro-Beta</li>
<li>AI_BASE_URL — https://foundation-models.api.cloud.ru/v1/</li>
<li>AI_TEMPERATURE — 0.5</li>
<li>AI_MAX_TOKENS — 1000</li>
<li>OBJECT_STORAGE_BUCKET_NAME — tg-bot-lab . Название бакета, созданного на шаге 7.</li>
<li>OBJECT_STORAGE_ACCESS_KEY_ID — ключ для доступа к бакету Object Storage, полученный на шаге 7</li>
<li>OBJECT_STORAGE_SECRET_ACCESS_KEY — секрет для доступа к бакету Object Storage, полученный на шаге 7</li>
<li>OBJECT_STORAGE_REGION — ru-central-1</li>
<li>OBJECT_STORAGE_ROOT_DIR — chat_logs</li>
<li>OBJECT_STORAGE_ENDPOINT_URL — https://s3.cloud.ru</li>
</ul>
<p>г. Активируйте опцию Автоматическое развертывание, чтобы каждый раз после загрузки в Artifact Registry новой версии образа на стороне Container Apps автоматически создавалась новая ревизия контейнера.</p>
<ol start="4">
<li>Нажмите Создать.</li>
</ol>
<p>Контейнер будет запущен в течение нескольких секунд.</p>
<p>5. Дождитесь, когда контейнер и ревизия перейдут в статус «Выполняется».</p>
<h4>9. Проверьте работоспособность развернутого чат-бота</h4>
<ol>
<li>Добавьте чат-бота в закрытый канал или чат в Telegram с ролью администратор.</li>
<li>Напишите несколько сообщений в канал или чат.</li>
<li>Выполните команду /summary . Дождитесь ответа от чат-бота с суммариацией вашей переписки.</li>
<li>Выполните команду /tasks . Дождитесь ответа от чат-бота со списком задач.</li>
</ol>
<p>Результат</p>
<p>В ходе выполнения практической работы вы получили практический опыт интеграции LLM-моделей из сервиса Foundation Models в Telegram-косистему, освоили приемы безопасной работы с ключами и конфигурацией, а также убедились, что сервис Foundation Models существенно упрощает создание production-ready AI-сервисов.</p>