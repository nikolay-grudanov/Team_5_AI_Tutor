---
source_image: page_638.png
page_number: 638
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 88.74
tokens: 12683
characters: 3478
timestamp: 2025-12-24T03:44:51.502844
finish_reason: stop
---

Метасимволы в программах Linux

<table>
  <tr>
    <th>Символ</th>
    <th>ed</th>
    <th>vi</th>
    <th>sed</th>
    <th>awk</th>
    <th>grep</th>
    <th>egrep</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>^</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Привязка к началу строки</td>
  </tr>
  <tr>
    <td>$</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Привязка к концу строки</td>
  </tr>
  <tr>
    <td>\</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Экранирует следующий символ</td>
  </tr>
  <tr>
    <td>[ ]</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Один из перечисленных символов или символ из диапазона</td>
  </tr>
  <tr>
    <td>\( \)</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Сохранить найденный текст для последующего использования</td>
  </tr>
  <tr>
    <td>\n</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td></td>
    <td></td>
    <td></td>
    <td>Повторное использование текста, найденного и сохраненного n-ным вхождением элемента \( \)</td>
  </tr>
  <tr>
    <td>{ }</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td></td>
    <td>Диапазон символов</td>
  </tr>
  <tr>
    <td>\{ \}</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Диапазон символов</td>
  </tr>
  <tr>
    <td>\< \></td>
    <td>•</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Привязка к началу или к концу слова</td>
  </tr>
  <tr>
    <td>+</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Одно или более вхождений предшествующего символа</td>
  </tr>
  <tr>
    <td>?</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Отсутствие или одно вхождение предшествующего символа</td>
  </tr>
  <tr>
    <td>|</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Варианты шаблона</td>
  </tr>
  <tr>
    <td>( )</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Группировка выражений для поиска</td>
  </tr>
</table>

В некоторых дистрибутивах Linux grep является ссылкой на egrep, поэтому команда grep на самом деле вызывает egrep.

При выполнении операции подстановки (поиска и замены) с помощью редакторов ed, vi и sed метасимволы приведенной таблицы имеют смысл только в шаблонах поиска, но не в строке замены.

При работе с awk следует помнить, что символы { }, упомянутые в стандарте POSIX, поддерживаются gawk только при запуске с параметром -Wre-interval.

Следующие дополнительные метасимволы в редакторах ed, vi и sed доступны только для применения в шаблонах замены:

<table>
  <tr>
    <th>Символ</th>
    <th>ex</th>
    <th>sed</th>
    <th>ed</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>\</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Экранировать следующий символ</td>
  </tr>
  <tr>
    <td>\n</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>Вставить текст, найденный n-ым вхождением \( \)</td>
  </tr>
  <tr>
    <td>&</td>
    <td>•</td>
    <td>•</td>
    <td></td>
    <td>Вставить предыдущий шаблон поиска</td>
  </tr>
</table>