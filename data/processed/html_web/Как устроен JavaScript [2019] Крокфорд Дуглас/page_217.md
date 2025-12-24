---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.71
tokens: 7449
characters: 2412
timestamp: 2025-12-24T09:59:32.124011
finish_reason: stop
---

Данная страница содержит код на языке JavaScript, который описывает работу тестирования. В коде присутствуют функции `generate_class` и `if (cases)`, а также вложенные блоки условий и циклов. Код выглядит следующим образом:

```javascript
function generate_class(key) {
    if (detail >= 3 || class_fail[key] || class_lost[key]) {
        report += fulfill(
            " {key} pass {pass}{fail}{lost}\n",
            {
                key,
                pass: class_pass[key],
                fail: (
                    class_fail[key]
                    ? " fail " + class_fail[key]
                    : ""
                ),
                lost: (
                    class_lost[key]
                    ? " lost " + class_lost[key]
                    : ""
                )
            }
        );
    }
}

if (cases) {
    while (true) {
        next_case = cases[serials[case_nr]];
        case_nr += 1;
        if (!next_case || (next_case.claim !== now_claim)) {
            if (now_claim) {
                if (detail >= 1) {
                    report += fulfill(
                        ctp,
                        {
                            name: the_case.name,
                            class: (
                                nr_class
                                ? nr_class + " classifications, "
                                : ""
                            ),
                            cases: nr_pass + nr_fail + nr_lost,
                            pass: nr_pass,
                            fail: (
                                nr_fail
                                ? ", " + nr_fail + " fail"
                                : ""
                            ),
```

Код выполняет следующие действия:
1. Функция `generate_class` генерирует строку отчета для класса с ключом `key`, если число деталей (`detail`) больше или равно 3, или если у класса есть неуспешные или утраченные случаи.
2. Если у класса есть неуспешные или утраченные случаи, формируется строка отчета с ключом, количеством успешных, неуспешных и утраченных случаев.
3. В основной части кода происходит обход списка случаев (`cases`), и если текущий случай не соответствует текущему утверждению (`now_claim`), то формируется строка отчета с информацией о классе, количестве успешных, неуспешных и утраченных случаев.

Текст на странице также содержит заголовок раздела: "Как работает тестирование".