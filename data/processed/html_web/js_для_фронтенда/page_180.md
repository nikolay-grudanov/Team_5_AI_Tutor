---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.79
tokens: 6207
characters: 1497
timestamp: 2025-12-24T10:06:12.280926
finish_reason: stop
---

Давайте рассмотрим базовый код:

var Module = require('module')
    , path = require('path')
    , originalLoader = Module._load
    , coverageBase = '/tmp'
    , COVERAGE_ME = []
;
Module._load = coverageLoader;
// COVERAGE_ME содержит список файлов, для которых нужно сгенерировать
// файлы покрытия
// Эти JS-файлы будут запущены через yuitest-coverage.jar
// Вывод будет сохранен в coverageBase
// Потом будут запущены тесты
// Все вызовы 'require' будут проходить через это:
function coverageLoader(request, parent, isMain) {
    if (COVERAGE_ME[request]) {
        request = PATH.join(coverageBase, path.basename(request));
    }
    return originalLoader(request, parent, isMain);
}
// По окончании просмотрите глобальную переменную _yuitest_coverage

Сначала мы определяем, для каких JavaScript-файлов нужно создать файлы покрытия, а затем мы генерируем файлы покрытия для этих файлов в каталоге /tmp.

После этого мы выполняем наши тесты, используя любой тестировочный фреймворк (платформу тестирования). При выполнении наших тестов все их вызовы require будут пропускаться через функцию coverageLoader. Если запрошен файл, который мы хотим «померять», будет возвращена его версия со счетчиками покрытия кода (так называемый файл покрытия), в противном случае мы обращаемся к обычному загрузчику Node.js, чтобы загрузить запрошенный модуль в обычном режиме.

Когда все тесты будут выполнены, станет доступна глобальная переменная _yuitest_coverage (она будет преобразована в формат LCOV).