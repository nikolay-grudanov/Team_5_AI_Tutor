---
source_image: page_460.png
page_number: 460
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.73
tokens: 7197
characters: 1073
timestamp: 2025-12-24T03:12:45.110241
finish_reason: stop
---

lint:
    hadolint Dockerfile
    pylint --disable=R,C,W1203 app.py

all: install lint test

Файл requirements.txt:

Flask==1.0.2
pandas==0.24.2
scikit-learn==0.20.3

Файл app.py:

from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Масштабирование нагрузки"""

    LOG.info(f"Scaling Payload: {payload}")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

# СДЕЛАТЬ: вывести в журнал значение предсказания
@app.route("/predict", methods=['POST'])
def predict():
    """Предсказание с помощью sklearn

    Входные данные имеют следующий вид:
        {
        "CHAS":{
            "0":0
        },
        "RM":{
            "0":6.575