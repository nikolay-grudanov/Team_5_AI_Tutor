---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.91
tokens: 7219
characters: 942
timestamp: 2025-12-24T09:21:23.685465
finish_reason: stop
---

Те же самые правила nth-child применяются и ко всем другим вложенным группам элементов, таким как, например, ul и li, и к любой другой произвольной комбинации «родитель/потомок».

Обратите внимание: сам символ пробела тоже является частью селектора. Это поможет вам детализировать иерархию родительских элементов.

3.1. :link

:link похож на a[href].

<table>
  <tr>
    <th><a href="http://www.google.com/">Текст ссылки</a></th>
  </tr>
</table>

:link не выбирает элементы href-less.

<table>
  <tr>
    <th><a href-less>href-less</a></th>
  </tr>
</table>

3.2. :visited

:visited выбирает посещенные ссылки в текущем браузере.

<table>
  <tr>
    <th><a href="http://www.google.com/">Посещенная ссылка</a></th>
  </tr>
</table>

3.3. :hover

:hovered выбирает элемент ссылки, на которую наведен указатель мыши.

<table>
  <tr>
    <th><a href="http://www.google.com/">Ссылка, на которую установлен указатель мыши</a></th>
  </tr>
</table>