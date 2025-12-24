---
source_image: page_521.png
page_number: 521
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 66.74
tokens: 12280
characters: 2605
timestamp: 2025-12-24T03:39:11.892042
finish_reason: stop
---

Различия

В приведенной ниже таблице отображены возможности, различающиеся в этих трех командных интерпретаторах.

<table>
  <tr>
    <th>Значение/Действие</th>
    <th>bash</th>
    <th>csh</th>
    <th>tcsh</th>
  </tr>
  <tr>
    <td>Стандартное приглашение командной строки</td>
    <td>$</td>
    <td>%</td>
    <td>%</td>
  </tr>
  <tr>
    <td>Принудительное перенаправление</td>
    <td>>|</td>
    <td>>!</td>
    <td>>!</td>
  </tr>
  <tr>
    <td>Принудительное добавление</td>
    <td></td>
    <td>>>!</td>
    <td>>>!</td>
  </tr>
  <tr>
    <td>Присваивание значения переменной</td>
    <td>var=val</td>
    <td>set var=val</td>
    <td>set var=val</td>
  </tr>
  <tr>
    <td>Установка переменной окружения</td>
    <td>export var=val</td>
    <td>setenv var val</td>
    <td>setenv var val</td>
  </tr>
  <tr>
    <td>Количество аргументов</td>
    <td>#</td>
    <td>#argv</td>
    <td>#argv</td>
  </tr>
  <tr>
    <td>Код возврата</td>
    <td>$?</td>
    <td>$status</td>
    <td>$?</td>
  </tr>
  <tr>
    <td>Выполнить команды из файла (<i>file</i>)</td>
    <td>. file</td>
    <td>source file</td>
    <td>source file</td>
  </tr>
  <tr>
    <td>Завершение цикла</td>
    <td>done</td>
    <td>end</td>
    <td>end</td>
  </tr>
  <tr>
    <td>Завершение оператора case или switch</td>
    <td>esac</td>
    <td>endsw</td>
    <td>endsw</td>
  </tr>
  <tr>
    <td>Обработка в цикле</td>
    <td>for/do</td>
    <td>foreach</td>
    <td>foreach</td>
  </tr>
  <tr>
    <td>Пример условного оператора if</td>
    <td>if [ $i -eq 5 ] fi</td>
    <td>if ($i==5) endif</td>
    <td>if ($i==5) endif</td>
  </tr>
  <tr>
    <td>Завершение условного оператора if</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Установка ограничения ресурсов</td>
    <td>ulimit</td>
    <td>limit</td>
    <td>limit</td>
  </tr>
  <tr>
    <td>Чтение с терминала</td>
    <td>read</td>
    <td>$<</td>
    <td>$<</td>
  </tr>
  <tr>
    <td>Запретить изменение значения переменной</td>
    <td>readonly</td>
    <td></td>
    <td>set -r</td>
  </tr>
  <tr>
    <td>Поиск файлов ненулевого размера</td>
    <td></td>
    <td>-s</td>
    <td></td>
  </tr>
  <tr>
    <td>Дополнение слова</td>
    <td>Tab</td>
    <td></td>
    <td>Tab</td>
  </tr>
  <tr>
    <td>Игнорировать прерывания</td>
    <td>trap 2</td>
    <td>onintr</td>
    <td>onintr</td>
  </tr>
  <tr>
    <td>Начало цикла until</td>
    <td>until/do</td>
    <td>until</td>
    <td>until</td>
  </tr>
  <tr>
    <td>Начало цикла while</td>
    <td>while/do</td>
    <td>while</td>
    <td>while</td>
  </tr>
</table>