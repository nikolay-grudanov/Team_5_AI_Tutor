---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.56
tokens: 7374
characters: 1432
timestamp: 2025-12-24T03:02:46.701833
finish_reason: stop
---

"Action": "service-prefix:action-name",
    "Resource": "*",
    "Condition": {
        "DateGreaterThan": {"aws:CurrentTime": "2017-07-01T00:00:00Z"},
        "DateLessThan": {"aws:CurrentTime": "2017-12-31T23:59:59Z"}
    }
}

Для извлечения данных из подобного файла можно использовать стандартные методы read и readlines файлового объекта:

In [8]: with open('service-policy.json', 'r') as opened_file:
   ...:     policy = opened_file.readlines()
   ...:
   ...:

Результат нельзя будет применить сразу же, поскольку он будет выглядеть как одна строка или список строк в зависимости от выбранного метода чтения:

In [9]: print(policy)
['{\n',
 '    "Version": "2012-10-17",
\n',
 '    "Statement": {\n',
 '        "Effect": "Allow",
\n',
 '        "Action": "service-prefix:action-name",
\n',
 '        "Resource": "*",
\n',
 '        "Condition": {\n',
 '            "DateGreaterThan": {"aws:CurrentTime": "2017-07-01T00:00:00Z"},
\n',
 '            "DateLessThan": {"aws:CurrentTime": "2017-12-31T23:59:59Z"}\n',
 '        }\n',
 '    }\n']
}

Далее нужно будет произвести синтаксический разбор этой строки (строк) в структуры данных и типы, соответствующие исходному файлу, что может потребовать немалых усилий. Так что намного удобнее будет воспользоваться модулем json:

In [10]: import json
In [11]: with open('service-policy.json', 'r') as opened_file:
   ...:     policy = json.load(opened_file)
   ...:
   ...:
   ...: