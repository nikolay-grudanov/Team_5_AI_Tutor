---
source_image: page_615.png
page_number: 615
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.77
tokens: 11897
characters: 1892
timestamp: 2025-12-24T03:43:17.674464
finish_reason: stop
---

<table>
  <tr>
    <th>bindkey</th>
    <td>
      <ul>
        <li><b>-s</b> Интерпретировать команду как обычную строку, получаемую со стандартного ввода.</li>
        <li><b>-u</b> Отобразить справку по использованию команды.</li>
        <li><b>-v</b> Привязка к стандартным клавиатурным комбинациям vi.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>break</th>
    <td>
      <b>break</b><br>
      Продолжить выполнение с команды, следующей за ключевым словом <b>end</b>, принадлежащим ближайшему охватывающему циклу <b>while</b> или <b>foreach</b>.
    </td>
  </tr>
  <tr>
    <th>breaksw</th>
    <td>
      <b>breaksw</b><br>
      Аналог <b>break</b> для конструкции <b>switch</b>; выполнение продолжается с команды, следующей за <b>endsw</b>.
    </td>
  </tr>
  <tr>
    <th>built-ins</th>
    <td>
      <b>built-ins</b><br>
      Только для <b>tcsh</b>. Перечислить все встроенные команды интерпретатора.
    </td>
  </tr>
  <tr>
    <th>bye</th>
    <td>
      <b>bye</b><br>
      Только для <b>tcsh</b>. Синоним <b>logout</b>.
    </td>
  </tr>
  <tr>
    <th>case</th>
    <td>
      <i>case pattern :</i><br>
      Идентификация шаблона <i>pattern</i> в конструкции <b>switch</b>.
    </td>
  </tr>
  <tr>
    <th>cd</th>
    <td>
      <b>cd [dir]</b><br>
      Сменить рабочий каталог на <i>dir</i>; по умолчанию — на домашний каталог пользователя. Если <i>dir</i> является относительным путем, но не находится в текущем каталоге, происходит поиск по содержимому переменной <b>cdpath</b>. См. пример файла <i>.cshrc</i> ранее в этой главе.<br><br>
      <b>Параметры команды для tcsh</b><br>
      <ul>
        <li><b>-</b> Перейти в предыдущий каталог.</li>
        <li><b>-l</b> Явно расширять символ <code>~</code>.</li>
        <li><b>-n</b> Переносить имена ранее конца строки; подразумевается использование <b>-p</b>.</li>
      </ul>
    </td>
  </tr>
</table>