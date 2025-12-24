---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.42
tokens: 8217
characters: 1067
timestamp: 2025-12-24T02:17:43.984424
finish_reason: stop
---

8. Далее давайте напишем шаблон todo в todo.html:

{% extends "home.html" %}

{% block todo_container %}
<main class="container">
    <hr>
    <section class="container-fluid">
        <form method="post">
            <div class="col-auto">
                <div class="input-group mb-3">
                    <input type="text" name="item" value="{{ item }}" class="form-control" placeholder="Purchase Packt's Python workshop course" aria-label="Add a todo" aria-describedby="button-addon2" />
                    <button class="btn btn-outline-primary" type="submit" id="button-addon2" data-mdb-ripple-color="dark">
                        Add Todo
                    </button>
                </div>
            </div>
        </form>
    </section>
    {% if todo %}
        <article class="card container-fluid">
            <br/>
            <h4>Todo ID: {{ todo.id }}</h4>
            <p>
                <strong>
                    Item: {{ todo.item }}
                </strong>
            </p>
        </article>
    {% endif %}
</main>
{% endblock todo %}