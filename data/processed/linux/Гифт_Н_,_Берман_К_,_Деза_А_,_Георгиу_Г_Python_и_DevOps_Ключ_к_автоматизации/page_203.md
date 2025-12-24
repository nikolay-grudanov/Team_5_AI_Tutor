---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.17
tokens: 7161
characters: 896
timestamp: 2025-12-24T03:06:04.112481
finish_reason: stop
---

![Пример отображения результатов в формате JSON](https://i.imgur.com/3Q5z5QG.png)

Рис. 6.3. Пример отображения результатов в формате JSON

23. Добавьте в приложение NLP:
• запустите блокнот IPython (https://oreil.ly/c564z);
• включите облачное API обработки естественного языка;
• выполните команду pip install google-cloud-language:

In [1]: from google.cloud import language
   ...: from google.cloud.language import enums
   ...:
   ...: from google.cloud.language import types
In [2]:
In [2]: text = "LeBron James plays for the Cleveland Cavaliers."
   ...: client = language.LanguageServiceClient()
   ...: document = types.Document(
   ...:     content=text,
   ...:     type=enums.Document.Type.PLAIN_TEXT)
   ...: entities = client.analyze_entities(document).entities
In [3]: entities

24. Вот пример API ИИ целиком:

from flask import Flask
from flask import jsonify
import pandas as pd