---
source_image: page_321.png
page_number: 321
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.54
tokens: 11336
characters: 607
timestamp: 2025-12-24T09:40:14.085345
finish_reason: stop
---

Когда в редакторе Dreamweaver вы применяете шаблон для создания отдельных страниц, комментарии на новых страницах немного отличаются от комментариев на первоначальной странице. Например, Dreamweaver заменяет команду TemplateBeginEditable командой InstanceBeginEditable.

В редакторе Expression Web, как показано далее, новая страница получает те же самые комментарии, что и исходный шаблон.

<!DOCTYPE html>

<html>

<!-- #BeginTemplate "PageTemplate.dwt" -->
<head>
 <!-- #BeginEditable "title" -->
 <title>Page Templates</title>
 <!-- #EndEditable -->

 <link rel="stylesheet" href="styles.css" />
</head>