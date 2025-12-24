import os

from dotenv import load_dotenv
from openai import OpenAI

# Загружаем .env
load_dotenv()

BASE_URL = os.getenv("VLLM_BASE_URL")
MODEL_NAME = os.getenv("VLLM_MODEL_NAME")
API_KEY = os.getenv("VLLM_API_KEY", "EMPTY")
print("Переменные окружения")
print(10*"=")
print(f"BASE_URL = {BASE_URL}")
print(f"MODEL_NAME = {MODEL_NAME}")
print(f"API_KEY = {API_KEY}")
print("/n")
print(10*"=")
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
)

# Проверяем доступные модели
try:
    models = client.models.list()
    print("/n")
    print("✅ Подключение успешно!")
    print(f"\nДоступные модели:")
    for model in models.data:
        print(f"  - {model.id}")
except Exception as e:
    print("/n")
    print(f"❌ Ошибка подключения: {e}")