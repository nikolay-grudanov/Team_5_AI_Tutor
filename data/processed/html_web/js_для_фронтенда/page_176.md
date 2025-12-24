---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.66
tokens: 6205
characters: 1390
timestamp: 2025-12-24T10:06:08.908324
finish_reason: stop
---

Для инструментирования этого файла выполните следующую команду:

% java -jar yuitest_coverage sum.js -o sum_cover.js

В результате преобразования нашего файла будет получен файл с 37 строками! Первые 18 строк — это шаблон, определяющий глобальные переменные и функции, которые использует YUI Test Coverage для отслеживания информации покрытия.

Оставшиеся 19 строк будут такими:

_yuitest_coverage["sum.js"] = {
    lines: {},
    functions: {},
    coveredLines: 0,
    calledLines: 0,
    coveredFunctions: 0,
    calledFunctions: 0,
    path: "/home/trostler/sum.js",
    code: []
};
_yuitest_coverage["sum.js"].code=["function sum(a, b)
{"," return a + b;","}"];
_yuitest_coverage["sum.js"].lines = {"1":0,"2":0};
_yuitest_coverage["sum.js"].functions = {"sum:1":0};
_yuitest_coverage["sum.js"].coveredLines = 2;
_yuitest_coverage["sum.js"].coveredFunctions = 1;
_yuitest_coverline("sum.js", 1); function sum(a, b) {
    _yuitest_coverfunc("sum.js", "sum", 1);
    _yuitest_coverline("sum.js", 2); return a + b;
}

Первый блок строк определяет объект_yuitest_coverage["sum.js"], который будет хранить счетчики строк и функций. В последнем блоке строк определены счетчики строк (есть две счетные строки в файле, строка 1 и строка 2, и одна функция в строке 1, которая называется sum). Изменение счетчиков происходит при каждом вызове yuitest_coverline или _yuitest_coverfunc. Эти функции