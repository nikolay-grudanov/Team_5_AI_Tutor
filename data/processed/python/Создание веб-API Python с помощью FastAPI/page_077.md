---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.42
tokens: 8221
characters: 758
timestamp: 2025-12-24T02:17:43.984164
finish_reason: stop
---

<h1>Packt Todo Application</h1>
</center>
</div>
</nav>
</header>
<div class="container-fluid">
{% block todo_container %}{% endblock %}
</div>
</body>
</html>
</html>

Выделенный код сообщает родительскому шаблону, что блок todo_container будет определяться дочерним шаблоном.
Содержимое дочернего шаблона, содержащего блок todo_container и расширяющего родительский шаблон, будет отображаться там.

6. Чтобы увидеть изменения, активируйте виртуальную среду и запустите приложение:

$ source venv/bin/activate
(venv)$ uvicorn api:app --host=0.0.0.0 --port 8000 --reload

7. Откройте http://127.0.0.1:8000/todo, чтобы просмотреть изменения:

![Домашняя страница приложения Todo](https://example.com/image.png)

Рисунок 4.2 – Домашняя страница приложения Todo