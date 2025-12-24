---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.56
tokens: 8105
characters: 433
timestamp: 2025-12-24T02:20:02.505535
finish_reason: stop
---

Далее мы инициируем запрос и тестируем ответы:

```python
response = await default_client.post("/user/signin",
    data=payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"
```

Повторим тест:

(venv) $ pytest tests/test_login.py

![Успешный тестовый прогона для обоих маршрутов](../images/ch08/fig8_4.png)

Рисунок 8.4 – Успешный тестовый прогона для обоих маршрутов