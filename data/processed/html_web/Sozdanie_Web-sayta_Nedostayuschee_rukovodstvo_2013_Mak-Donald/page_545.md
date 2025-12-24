---
source_image: page_545.png
page_number: 545
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.47
tokens: 11651
characters: 1544
timestamp: 2025-12-24T09:50:15.963799
finish_reason: stop
---

Создание меню

Начать применение меню Slashdot следует с присоединения к вашей странице таблицы стилей и вставки ссылки на файл JavaScript, управляющий меню. Вам также понадобится коротенький сценарий, создающий меню при загрузке страницы. Все три компонента помещаются в раздел <head> вашей страницы. Далее показано, как они выглядят.

<head>
    <title>Fancy Buttons</title>

    <link rel="stylesheet" type="text/css" href="sdmenu/sdmenu.css" />
    <script src="sdmenu/sdmenu.js"></script>

    <script>
        var myMenu;
        window.onload = function() {
            myMenu = new SDMenu("my_menu");
            myMenu.init();
        };
    </script>
    ...
</head>

Код сценария стандартный. Вы можете копировать его слово в слово на любую страницу, применяющую меню Slashdot. Следует сделать единственное замечание, касающееся имени меню, используемого в сценарии (в данном примере my_menu), оно должно совпадать с ID элемента <div> на вашей странице, содержащего меню.

Возможно, вы захотите вставить в ваш раздел <head> встроенную таблицу стилей или ссылку на другую таблицу стилей. Например, на рис. 16.8 применяются три базовых правила стиля. Одно задает шрифт по умолчанию на странице, второе определяет местоположение боковой панели, содержащей меню Slashdot, а третье задает местоположение раздела с основным контентом страницы.

body {
    font-family: Verdana, sans-serif;
    font-size: small;
}

.MenuBar {
    position: absolute;
    top: 20px;
    left: 0px;
    margin: 15px;
}

.MainContent
{
    margin-left: 180px;