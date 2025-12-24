---
source_image: page_191.png
page_number: 191
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.99
tokens: 6228
characters: 1483
timestamp: 2025-12-24T10:06:25.071072
finish_reason: stop
---

покрытии кода нашими имеющимися тестами, мы должны учесть и эти файлы, код которых пройдет как непокрытый и снизит общее агрегированное значение метрики покрытия кода.

Самый простой метод учесть эти скрытые файлы — сделать так, чтобы для всех файлов вашего приложения были созданы тестовые сценарии (тестовые файлы), просто для некоторых файлов тестовые сценарии будут «пустыми». При запуске пустого теста на инструментированном файле со счетчиками покрытия будет сгенерирован вывод LCOV (0%), что означает нулевое покрытие. Теперь можно сохранить и обработать эти LCOV-данные, как обычно, и при этом весь ваш код будет учтен в агрегированной сводке покрытия.

Далее приведен HTML пустого теста, который должны иметь все файлы приложения. Как только будет готов соответствующий не-пустой тестовый сценарий, вы можете удалить этот HTML-файл и заменить его реальным тестом:

<html lang="en">
<body class="yui3-skin-sam">
<div id="log"></div>
<h3>Пустой тест для APP_FILE</h3>
<script src="http://yui.yahooapis.com/3.18.1/build/yui/yui.js">
</script>
<script src="/path/to/coveraged/file/without/tests.js"></script>
<script>
YUI().use('test', function(Y) {
    Y.Test.Runner.add(
        new Y.Test.Suite('no test').add(
            new Y.Test.Case({
                name: 'dummy_NOTESTS'
                , 'testFile': function() {
                    Y.Assert.areEqual(true, true);
                }
            })
        )
    );
    Y.TestRunner.go();
});
</script>
</body>
</html>