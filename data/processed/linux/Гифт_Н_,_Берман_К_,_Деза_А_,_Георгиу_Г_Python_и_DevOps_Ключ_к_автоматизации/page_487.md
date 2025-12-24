---
source_image: page_487.png
page_number: 487
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.20
tokens: 7208
characters: 1159
timestamp: 2025-12-24T03:13:26.848951
finish_reason: stop
---

Наполнение данными Amazon Simple Queue Service с помощью AWS Lambda

Далее необходимо в AWS Cloud9 локально сделать следующее.

1. Создать новую функцию Lambda с помощью Serverless Wizard.
2. Перейти в каталог функции Lambda и установить пакеты на один уровень выше:

pip3 install boto3 --target ../
pip3 install python-json-logger --target ../

Теперь можем проверить локально, а затем и развернуть в облаке следующий код:

'''
Из Dynamo в SQS
'''

import boto3
import json
import sys
import os

DYNAMODB = boto3.resource('dynamodb')
TABLE = "fang"
QUEUE = "producer"
SQS = boto3.client("sqs")

# Настраиваем журналирование
import logging
from pythonjsonlogger import jsonlogger

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
LOG.addHandler(logHandler)

def scan_table(table):
    '''Просматриваем таблицу и возвращаем результат'''
    LOG.info(f"Scanning Table {table}")
    producer_table = DYNAMODB.Table(table)
    response = producer_table.scan()
    items = response['Items']
    LOG.info(f"Found {len(items)} Items")
    return items