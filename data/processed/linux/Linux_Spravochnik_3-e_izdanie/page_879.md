---
source_image: page_879.png
page_number: 879
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.46
tokens: 11948
characters: 2234
timestamp: 2025-12-24T03:55:03.209368
finish_reason: stop
---

Для того чтобы получить столь же тонкий контроль над указателем, как при работе с мышью, нужно определить сочетания, перемещающие указатель на один процент размера страницы за одно нажатие:

## Press Shift + Control + arrow in any context
## to move the pointer by 1% of a page in direction of arrow
Key Left      A   SC   CursorMove -1 0
Key Right     A   SC   CursorMove +1 +0
Key Up        A   SC   CursorMove +0 -1
Key Down      A   SC   CursorMove +0 +1

В табл. 17.6 приведены выполняемые при этом действия.

Таблица 17.6. Сочетания клавиш для перемещения указателя на один процент размера страницы

<table>
  <tr>
    <th>Комбинация</th>
    <th>Перемещение указателя</th>
  </tr>
  <tr>
    <td>&lt;Shift&gt;+&lt;Ctrl&gt;+&lt;стрелка влево&gt;</td>
    <td>На одну сотую часть страницы влево</td>
  </tr>
  <tr>
    <td>&lt;Shift&gt;+&lt;Ctrl&gt;+&lt;стрелка вправо&gt;</td>
    <td>На одну сотую часть страницы вправо</td>
  </tr>
  <tr>
    <td>&lt;Shift&gt;+&lt;Ctrl&gt;+&lt;стрелка вверх&gt;</td>
    <td>На одну сотую часть страницы вверх</td>
  </tr>
  <tr>
    <td>&lt;Shift&gt;+&lt;Ctrl&gt;+&lt;стрелка вниз&gt;</td>
    <td>На одну сотую часть страницы вниз</td>
  </tr>
</table>

Сочетания клавиш для меню и управления окнами

До сих пор мы ограничивали назначение сочетаний клавиш навигацией по рабочему пространству и перемещением указателя. Но можно определять сочетания клавиш, связанные с любой функцией оконного менеджера.

Вот некоторые примеры сочетаний, предназначенных для выполнения простых операций над окнами и отображения меню:

# Keyboard accelerators
Key F1      A   M   Iconify
Key F2      A   M   Move
Key F3      A   M   Resize
Key F4      A   M   Popup "RootMenu"
Key F5      A   M   Popup "Misc-Ops"
Key F6      A   M   Popup "Utilities"
Key F7      A   M   Popup "Module-Popup"
Key F10     A   M   Restart fvwm2
Key F12     A   SM  Close

Это просто примеры; пользователь может создать собственные комбинации и заставить их делать, что угодно. Но эти сочетания позволят нам рассмотреть некоторые из доступных возможностей, а также потенциальные проблемы.

Первая из строк этих определений связывает нажатие функциональной клавиши <F1> при нажатой клавише <Meta> («М») и указателе в произвольном