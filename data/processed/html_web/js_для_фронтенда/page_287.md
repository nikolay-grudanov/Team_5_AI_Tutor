---
source_image: page_287.png
page_number: 287
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.82
tokens: 6277
characters: 1229
timestamp: 2025-12-24T10:08:25.552475
finish_reason: stop
---

нерированный отчет покрытия. Как уже упоминалось, подключить другой браузер к JUTE можно путем посещения страницы JUTE из этого другого браузера. Тогда панель Status отобразит оба браузера (рис. 8.3). Теперь к JUTE подключены браузеры Chrome и Firefox.

![Панель Status](../images/8_3.png)

Рис. 8.3. Панель Status

Запуск jute_submit_tests приведет к запуску всех тестов параллельно в обоих браузерах, а на панели Results будут отображены результаты для Chrome и для Firefox. Рассмотрим содержимое каталога после запуска теста «toolbar» с двумя подключенными браузерами:

% ls output/toolbar/
cover.json
lcov.info
lcov-report/
Mozilla5_0__Macintosh_Intel_Mac_OS_X_10_6_8__AppleWebKit536_11__KHTML__like_Gecko__Chrome20_0_1132_21_Safari536_11-test.xml
Mozilla5_0__Macintosh_Intel_Mac_OS_X_10_6_8__AppleWebKit536_11__KHTML__like_Gecko__Chrome20_0_1132_21_Safari536_11.txt
Mozilla5_0__Macintosh_Intel_Mac_OS_X_10_6_rv_12_0__Gecko20100101_Firefox12_0-test.xml
Mozilla5_0__Macintosh_Intel_Mac_OS_X_10_6_rv_12_0__Gecko20100101_Firefox12_0.txt

Обратите внимание, что у нас есть только один отчет о покрытии кода, независимо от того, сколько браузеров подключено. Однако, у нас есть два JUnit XML-файла и два вывода отладчика: по одно-