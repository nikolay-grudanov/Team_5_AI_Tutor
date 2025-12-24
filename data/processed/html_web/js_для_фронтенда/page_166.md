---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.91
tokens: 6165
characters: 1283
timestamp: 2025-12-24T10:05:51.453429
finish_reason: stop
---

Вывод результатов тестирования

По умолчанию Jasmine выводит результаты теста на экран, что хорошо при разработке тестов, но не очень хорошо для автоматизированных запусков (в рамках автоматизированного тестирования, когда результаты предназначены для анализа какой-либо программой, а не человеком). Используя параметр -junitreport, вы можете заставить Jasmine выводить результаты тестов в широко используемом формате JUnit XML. По умолчанию все результаты тестов записываются в каталог reports, название файла соответствует названию тестового набора (первый параметр описания метода). Например:

% ls reports
TEST-Sumsuite.xml TEST-SumsuiteFile.xml
% cat reports/TEST-SumsuiteFile.xml
<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
<testsuite name="Sum suite File" errors="0" tests="2" failures="0" time="0.001" timestamp="2014-07-25T15:31:48">
    <testcase classname="Sum suite File" name="Adds By Param!" time="0.001">
    </testcase>
    <testcase classname="Sum suite File" name="Adds By File!" time="0">
    </testcase>
</testsuite>
</testsuites>

Теперь наш вывод готов для импорта во что-то, что понимает этот формат, как будет показано в главе 8. Обратите внимание, число тестов, о которых будет отчитываться Jasmine, — это число функций it, а не число вызовов expect.