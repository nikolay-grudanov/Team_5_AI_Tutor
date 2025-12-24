---
source_image: page_300.png
page_number: 300
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.18
tokens: 6358
characters: 2051
timestamp: 2025-12-24T10:08:48.424703
finish_reason: stop
---

server_side_unit_tests: setupJUTE
    cd test && find server_side -name '*.js' -exec echo
    '{}?do_coverage=$(DO_COVERAGE)"; l jute_submit_test --v8 --test -
client_side_unit_tests: setupJUTE
    cd test && find client_side -name '*.html' -exec echo
    '{}?do_coverage=$(DO_COVERAGE)"; l jute_submit_test --v8 --test -
unit_tests: server_side_unit_tests client_side_unit_tests
.PHONY: server_side_unit_tests client_side_unit_tests unit_tests
setupJUTE

Этот Makefile использует UglifyJS (https://github.com/mishoo/UglifyJS) для сжатия/оптимизации кода, но вы также можете использовать и другие программы, например YUI Compressor (https://github.com/yui/yuicompressor/issues) и Google Closure Compiler (https://developers.google.com/closure/compiler/). Файл Makefile использует каталоги src и test для исходного кода и тестовых сценариев, соответственно.

Выполнение цели prod (используется по умолчанию) произведет модульное тестирование всего кода и минимизирует весь код, если все тесты будут успешно пройдены. Тесты запускаются через V8, следовательно, вы не нуждаетесь в браузере. Однако, это может не очень подходить для тестирования всего клиентского JavaScript, поэтому вы можете использовать PhantomJS (-phantomjs) или Selenium (-sel_host) для выполнения тестов через реальный браузер.

Вы можете даже использовать «захваченные» браузеры, по крайней мере, один захваченный экземпляром JUTE браузер, запущенный на машине. Обратите внимание, в этом нашем случае мы должны настроить JUTE так, чтобы при запуске Jenkins JUTE "знал", где находится корневой каталог документов, пока Jenkins собирает проект. Если у вас есть выделенное окружение для сборки, вы можете настроить JUTE всегда использовать рабочее пространство Jenkins. Динамическую информацию о покрытии кода можно добавить в качестве параметров команды make:

% make prod DO_COVERAGE=0

Здесь проявляется некоторое волшебство make-файла. Все ваши JS-файлы будут преобразованы в их сжатые версии в дереве каталогов, которое зеркально отражает дерево src в каталог release. Как только