---
source_image: page_493.png
page_number: 493
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.69
tokens: 7129
characters: 716
timestamp: 2025-12-24T03:13:35.018584
finish_reason: stop
---

Создание событийно-управляемых функций Lambda

По окончании работы над функцией-генератором Lambda мы можем создать событийно-управляемую функцию Lambda (потребитель), которая срабатывает асинхронно для каждого сообщения в SQS. Теперь функция Lambda сможет реагировать на каждое сообщение SQS (рис. 15.15).

![Срабатывание при событии SQS](../images/15_15.png)

Рис. 15.15. Срабатывание при событии SQS

Чтение событий Amazon SQS из AWS Lambda

Единственная задача, которую нам осталось решить, — организовать потребление сообщений из SQS, их обработку с помощью нашего API и запись результатов в S3:

import json
import boto3
import botocore
import pandas as pd
import wikipedia
import boto3
from io import StringIO