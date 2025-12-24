---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.11
tokens: 6190
characters: 1307
timestamp: 2025-12-24T10:03:16.759254
finish_reason: stop
---

Давайте "скорим" его JSLint:

Error:
Problem at line 2 character 5: Missing 'use strict' statement.
return
Problem at line 2 character 11: Expected ';' and instead saw 'a'.
return
Problem at line 3 character 8: Unreachable 'a' after 'return'.
a+b;
Problem at line 3 character 8: Expected 'a' at column 5, not column 8.
a+b;
Problem at line 3 character 9: Missing space between 'a' and '+'.
a+b;
Problem at line 3 character 10: Missing space between '+' and 'b'.
a+b;
Problem at line 3 character 10: Expected an assignment or function call and instead saw an expression.
a+b;

Вау! Четыре строки простейшего кода сгенерировали целых семь ошибок JSLint! Что не так? Прежде всего, отсутствует директива use strict, но самая большая проблема — символ возврата каретки после return. Из-за вставки точки с запятой JavaScript вернет значение undefined из этой функции. JSLint зафиксировал эту ошибку и жалуется на другие пробелы в этой функции.

Пробел важен для удобочитаемости, но в нашем случае (см. код выше) он вызывает ошибку, которую очень трудно обнаружить. Используйте пробелы разумно, как требует JSLint.

Вот как выглядит правильный код:

function sum(a, b) {
    return a + b;
}

Давайте посмотрим еще на один фрагмент, безвредный на первый взгляд:

for (var i = 0; i < a.length; i++)
    a[i] = i * i;