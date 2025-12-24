---
source_image: page_310.png
page_number: 310
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.94
tokens: 6739
characters: 2202
timestamp: 2025-12-24T10:08:52.610197
finish_reason: stop
---

Если вы запустите npm-пакет jslint с аргументом --json, вы произведете простое преобразование из формата JSLint JSON в этот XML-формат. Моя реализация этого преобразования доступна по адресу: https://github.com/zzo/TestableJS/blob/master/hudson_jslint.pl.

Идея, как обычно, заключается в следующем: запустить JSLInt на нашем коде, получить вывод в формате XML и указать плагину Violations, где найти этот XML. Первым делом давайте добавим цель в наш make-файл:

JSLINT=jslint
JSL := $(patsubst %.js,% .jslint,$(SRC))
%.jslint : %.js
    -mkdir -p $(JSLINT)/$(@D)
    ./hudson_jslint.pl $< > $(JSLINT)/$(*D)/$(*F).jslint

Затем нужно добавить цель JSL в нашу цель prod:

prod: unit_tests $(OBJS) $(STYLE) $(JSL)

Все готово. Конечно, если нужно запустить JSLint отдельно, просто добавьте эту цель:

jslint: $(JSL)

Теперь настройте плагин Violations, указав расположение XML-файлов *.jslint (см. рис. 8.18).

<table>
  <tr>
    <th>Report Violations</th>
    <th colspan="3">XML filename pattern</th>
  </tr>
  <tr>
    <td>checkstyle</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td>checkstyle/**/*.xml</td>
  </tr>
  <tr>
    <td>codenarc</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>cpd</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>cpplint</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>csslint</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>findbugs</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>fxcop</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>gendarme</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>jcreport</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
  <tr>
    <td>jslint</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td>jslint/**/*.jslint</td>
  </tr>
  <tr>
    <td>pep8</td>
    <td>10</td>
    <td>999</td>
    <td>999</td>
    <td></td>
  </tr>
</table>

Рис. 8.18. Настройка плагина Violations в Jenkins