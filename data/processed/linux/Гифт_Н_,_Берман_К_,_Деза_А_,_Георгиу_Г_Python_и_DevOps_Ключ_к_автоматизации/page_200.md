---
source_image: page_200.png
page_number: 200
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.12
tokens: 7126
characters: 688
timestamp: 2025-12-24T03:05:50.664902
finish_reason: stop
---

11. Вызовите редактор облачной командной оболочки.

12. Установите нужные пакеты:

pip install -r requirements.txt

В результате этого должен быть установлен Flask:

Flask==1.0.2

13. Запустите Flask локально, в командной оболочке GCP:

python main.py

14. Воспользуйтесь предварительным просмотром (web preview) (рис. 6.2).

![Предварительный просмотр](./images/chapter6_2.png)

Рис. 6.2. Предварительный просмотр

15. Модифицируйте файл main.py:

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Возвращает дружеское HTTP-приветствие."""
    return 'Hello I like to make AI Apps'

@app.route('/name/<value>')
def name(value):