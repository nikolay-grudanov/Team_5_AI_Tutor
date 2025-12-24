---
source_image: page_462.png
page_number: 462
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.61
tokens: 7312
characters: 1526
timestamp: 2025-12-24T03:12:53.378316
finish_reason: stop
---

--generator=run-pod/v1\
--image=$dockerpath\
--port=80 --labels app=flaskskearlndemo

# Выводим список модулей Kubernetes
kubectl get pods

# Перенаправление порта контейнера на порт хоста
kubectl port-forward flaskskearlndemo 8000:80

#!/usr/bin/env bash
# Присваиваем образу Docker тег и загружаем его в Docker Hub

# Предполагаем, что все собрано
#docker build --tag=flasksklearn .
dockerpath="noahgift/flasksklearn"

# Аутентификация и создание тега
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag flasksklearn $dockerpath

# Помещаем образ в реестр
docker image push $dockerpath

Наверное, вам интересно, как модель создается, а затем выгружается/загружается. Вот тут (https://oreil.ly/_pHz-) вы можете найти весь блокнот.

Во-первых, импортируем библиотеки для машинного обучения:

import numpy
from numpy import arange
from matplotlib import pyplot
import seaborn as sns
import pandas as pd
from pandas import read_csv
from pandas import set_option
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline