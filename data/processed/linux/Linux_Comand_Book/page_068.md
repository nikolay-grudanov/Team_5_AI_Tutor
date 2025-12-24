---
source_image: page_068.png
page_number: 68
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.81
tokens: 6242
characters: 1860
timestamp: 2025-12-24T04:06:20.931454
finish_reason: stop
---

(http://www.foolabs.com/xpdf/).

Полезные опции

<table>
  <tr>
    <th>Опция</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>-page P</td>
    <td>Начать с P-й страницы (по умолчанию с 1-й)</td>
  </tr>
  <tr>
    <td>-monochrome</td>
    <td>Задать режим вывода: монохромный, оттенки серого или цветной соответственно</td>
  </tr>
  <tr>
    <td>-grayscale</td>
    <td></td>
  </tr>
  <tr>
    <td>-color</td>
    <td></td>
  </tr>
  <tr>
    <td>-portrait</td>
    <td>Выбрать ориентацию страницы; как правило, программа gv определяет это автоматически</td>
  </tr>
  <tr>
    <td>-landscape</td>
    <td></td>
  </tr>
  <tr>
    <td>-seascape</td>
    <td></td>
  </tr>
  <tr>
    <td>-upsidedown</td>
    <td></td>
  </tr>
  <tr>
    <td>-scale N</td>
    <td>Задать коэффициент масштабирования для вывода. Целое число Сможет быть положительным (изображение будет больше) или отрицательным (меньше).</td>
  </tr>
  <tr>
    <td>-watch</td>
    <td>При изменении Postscript-файла автоматически перезагружать его (watch), либо не делать этого</td>
  </tr>
  <tr>
    <td>-nowatch (nowatch)</td>
    <td></td>
  </tr>
</table>

xdvi [опции] файл tetex-xdvi
/usr/bin stdin stdout -file --opt -help -version

Система обработки документов TeX создает двоичные выходные файлы в формате DVI, с расширением .dvi. Программа просмотра xdvi выводит DVI-файлы в графическом окне. При желании вы можете преобразовать DVI-файл в Postscript-файл с помощью команды dvips, а затем использовать программу GhostView (gv) для его просмотра:

$ dvips -o myfile.ps myfile.dvi
$ gv myfile.ps

При выводе файла программа xdvi предоставляет колонку кнопок справа с очевидными функциями, например, Next (следующая страница) для перехода к следующей странице (вы можете скрыть кнопки, вызвав программу xdvi с опцией -expert). Также вы можете перемещаться по файлу с помощью клавиш.