---
source_image: page_309.png
page_number: 309
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.89
tokens: 6118
characters: 1024
timestamp: 2025-12-24T10:08:42.485001
finish_reason: stop
---

Рис. 8.16. Настройка Checkstyle в проекте Jenkins

Здесь мы указываем плагину, что искать необходимые файлы нужно в подкаталоге checkstyle нашего рабочего каталога. Нажмите ссылку Build Now и приготовьтесь получить результаты (рис. 8.17).

Рис. 8.17. График Checkstyle на домашней странице проекта Jenkins

Данный график появится на домашней странице вашего проекта. Щелчок по графику покажет историю и все текущие предупреждения, если таковые имеются, в том числе и предупреждения в новой сборке.

JSLint + Jenkins

Процесс интеграции JSLint с Jenkins аналогичен предыдущим интеграциям — для этого вам нужен плагин Violations. Установите его. Кстати, приятно, что он также обрабатывает Checkstyle-файлы. Но об этом мы поговорим позже, а пока вам нужно знать, что плагин Violations требует JSLint вывода в определенном XML-формате, который легко сгенерировать:

<jslint>
    <file name="<full_path_to_file>">
        <issue line="<line #>" reason="<reason>" evidence="<evidence" />
        <issue ... >
    </file>
</jslint>