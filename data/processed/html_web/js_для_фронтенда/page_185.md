---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.01
tokens: 6268
characters: 1802
timestamp: 2025-12-24T10:06:19.243881
finish_reason: stop
---

var reporter = new Y.Test.Reporter(
    "http://www.yourserver.com/path/to/target",
    Y.Test.Format.JUnitXML);
reporter.report(results);
}

Добавьте этот фрагмент кода в конец каждого сценария тестирования, и отчеты о тестировании будут отправлены на ваш сервер в формате XML JUnit, который распознается Hudson/Jenkins и многими другими инструментами сборки. YUI также поддерживает вывод в форматах XML, JSON и TAP. С форматами JSON и XML вы уже знакомы, а формат TAP пришел к нам из мира Perl и также распознается всеми основными инструментами сборки.

Рассмотрим следующий код:

function getResults(data) {
    // Используйте формат JUnitXML для результатов тестирования модулей
    var reporter = new Y.Test.Reporter(
        "http://www.yourserver.com/path/to/target",
        Y.Test.Format.JUnitXML);
    // Получаем и кодируем результаты покрытия
    reporter.addField("coverageResults",
        Y.Test.Runner.getCoverage(Y.Coverage.Format.JSON));
    // Отправляем их
    reporter.report(results);
}

Метод addField объекта reporter позволяет вам передавать произвольные данные обратно на сервер. Таким образом, получается, что мы получаем результаты определения покрытия кода, кодируем эти результаты как JSON и передаем их обратно вместе с результатами модульного тестирования. Обратите внимание на то, что JSON — по большому счету единственный нормальный формат для упаковки информации о покрытии (несмотря на наличие альтернатив); и, кстати, именно в этом формате ожидает данные инструмент создания отчетов о покрытии во фреймворке YUI.

Конечный результат отправляется на наш сервер методом POST и содержит в себе значения параметров results и coverageResults. Соответственно на стороне сервера, после получения, эти два фрагмента данных могут быть сохранены в локальной файловой системе.