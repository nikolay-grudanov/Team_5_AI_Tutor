---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.81
tokens: 7108
characters: 625
timestamp: 2025-12-24T09:24:55.408929
finish_reason: stop
---

Переменные SASS могут быть назначены любому свойству CSS:

```css
#container {
    content: $text;
}
```

25.5. Вложенные правила

В стандартном CSS доступ к вложенным элементам осуществляется через пробел.

```css
/* Стандартный CSS */
#A {
    color: red;
}
#A #B {
    color: green;
}
#A #B #C p {
    color: blue;
}
```

Приведенный выше код можно выразить с помощью вложенных правил SASSy следующим образом.

```css
/* Вложенные правила */
#A {
    color: red;
    #B {
        color: green;
        #C p {
            color: blue;
        }
    }
}
```

Как видите, данный синтаксис выглядит чище и менее повторяющимся.