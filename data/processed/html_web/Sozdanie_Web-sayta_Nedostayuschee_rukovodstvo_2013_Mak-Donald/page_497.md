---
source_image: page_497.png
page_number: 497
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.77
tokens: 11676
characters: 1755
timestamp: 2025-12-24T09:48:19.046733
finish_reason: stop
---

Представьте себе, что вы довели до совершенства функцию ShowAlertBox(), так что она выполняет сложную задачу именно тем способом, каким вы хотите, но требует пары десятков строк кода. Для облегчения жизни и вашего HTML-документа вы создаете новый файл для хранения сценария.

Файлы сценариев — всегда обычные текстовые файлы, как правило, у них расширение js (сокращение от JavaScript). Вы помещаете весь ваш код внутрь файла сценария, но не вставляете элемент <script>. Например, вы можете создать файл на JavaScript с именем ShowAlert.js.

function ShowAlertBox()
{
    alert("This function is in an external file.")
}

Теперь сохраните файл и поместите его в ту же папку, что и вашу Web-страницу. На Web-странице определите блок сценария, но не вставляйте его код. Вместо этого добавьте атрибут src и задайте файл сценария, на который хотите сослаться.

<script src="ShowAlert.js">
</script>

Когда браузер дойдет до блока сценария, он запросит файл ShowAlert.js и будет обрабатывать его так, как будто код находится прямо на странице. Далее приведена полная тестовая страница, использующая файл ShowAlert.js. Сценарий в теле страницы вызывает функцию ShowAlertBox().

<!DOCTYPE html>

<html>
<head>
    <title>Show Alert</title>
    <!-- Make all the functions in the ShowAlert.js file available in this page. Notice there's no actual content here. -->
    <script src="ShowAlert.js">
    </script>
</head>

<body>
    <!-- Test out one of the functions. -->
    <script>
        ShowAlertBox()
    </script>
</body>
</html>

Встроенный и внешний сценарии действуют одинаково. Но хранение ваших сценариев в отдельных файлах помогает поддерживать организацию вашего Web-сайта и облегчает повторное применение сценариев на нескольких страницах. На самом