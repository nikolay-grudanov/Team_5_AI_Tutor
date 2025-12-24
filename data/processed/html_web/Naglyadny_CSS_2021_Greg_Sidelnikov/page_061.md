---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.79
tokens: 7114
characters: 671
timestamp: 2025-12-24T09:21:54.988542
finish_reason: stop
---

6.3. Свойство overflow

При вложении текста в родительский элемент вы можете сделать его прокручиваемым, применив свойство overflow: scroll к родительскому элементу:

![Пример с overflow: scroll](../images/overflow-scroll.png)
Родительский: overflow: scroll;
Дочерний: position: absolute;

![Пример с overflow: auto; height: 24px](../images/overflow-auto-24px.png)
Родительский: overflow: auto; height: 24px;

![Пример с overflow: auto; height: 34px](../images/overflow-auto-34px.png)
Родительский: overflow: auto; height: 34px;

![Пример с overflow: hidden; position: absolute](../images/overflow-hidden.png)
Родительский: overflow: hidden;
Дочерний: position: absolute;