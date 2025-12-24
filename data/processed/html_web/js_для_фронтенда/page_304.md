---
source_image: page_304.png
page_number: 304
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.71
tokens: 6236
characters: 1575
timestamp: 2025-12-24T10:08:47.091132
finish_reason: stop
---

JUTE делает снимок экрана браузера после каждого неудачного теста. Если вы хотите создавать снимки экрана после каждого теста, независимо от его результата, используйте опцию --snapshot.

Чтобы указать, в каком браузере должны быть выполнены все тесты, используйте опцию --sel_browser команды jute_submit_test.

Теперь соберем все в месте. Цель вашего make-файла, позволяющая запустить все ваши тесты за один раз через Selenium, может выглядеть так:

selenium_tests:
cd test && find . -name '*.html' -printf '%p?do_coverage=1\n' |
jute_submit_test --sel_host 10.3.4.45 --seleniums 5 --test -

Далее для запуска всех тестов выполните команду make с этой целью:

make selenium_tests

Вывод модульного теста

Все, что остается сделать — заставить Jenkins распознать вывод модульного теста (файлы в формате JUnit XML, которые генерирует JUTE), данные покрытия (которые также генерирует JUTE) и любые другие данные сборки, которые понадобятся Jenkins.

Удобно, что JUTE помещает весь вывод теста в один настраиваемый каталог, который по умолчанию называется output. Этот каталог находится в jute:docRoot, который также является рабочим каталогом Jenkins. Чтобы Jenkins распознал результаты тестов, нужно просто

Post-build Actions

Publish JUnit test result report
Test report XMLs output/**/*-test.xml
Fileset 'includes' setting that specifies the generated raw XML report files, such as 'myproject/target/test-reports/*.xml'. Basedir of the fileset is the workspace root.
Retain long standard output/error

Add post-build action

Рис. 8.11. Публикация вывода JUnit XML в Jenkins