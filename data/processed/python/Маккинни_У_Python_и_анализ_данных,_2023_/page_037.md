---
source_image: page_037.png
page_number: 37
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.72
tokens: 7115
characters: 462
timestamp: 2025-12-24T02:40:30.114029
finish_reason: stop
---

Соглашения об импорте
В сообществе Python принят ряд соглашений об именовании наиболее употребительных модулей:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm

Это означает, что np.arange — ссылка на функцию arange в пакете NumPy. Так делается, потому что импорт всех имен из большого пакета, каким является NumPy (from numpy import *), считается среди разработчиков на Python дурным тоном.