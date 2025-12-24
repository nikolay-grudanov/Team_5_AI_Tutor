---
source_image: page_764.png
page_number: 764
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 95.74
tokens: 12610
characters: 3223
timestamp: 2025-12-24T03:50:41.498630
finish_reason: stop
---

Таблица 14.17. Общие параметры

<table>
  <tr>
    <th>Параметр</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td><b>-D date</b></td>
    <td>Использовать самую последнюю версию, датированную не позднее <i>date</i></td>
  </tr>
  <tr>
    <td><b>-f</b></td>
    <td>Для команд, которые работают с меткой (при помощи <b>-r</b>) или датами (при помощи <b>-D</b>), включать файлы, не отмеченные указанной меткой или не соответствующие указанной дате. Включаются самые последние версии таких файлов</td>
  </tr>
  <tr>
    <td><b>-k kflag</b></td>
    <td>Определить, как будет производиться подстановка ключевых слов. Пробел между <b>-k</b> и флагом <i>kflag</i> не обязателен. Режимы подстановки ключевых слов см. в табл. 14.19</td>
  </tr>
  <tr>
    <td><b>-l</b></td>
    <td>Не производить рекурсивный обход подкаталогов</td>
  </tr>
  <tr>
    <td><b>-n</b></td>
    <td>Не выполнять программы для модулей</td>
  </tr>
  <tr>
    <td><b>-R</b></td>
    <td>Производить рекурсивный обход подкаталогов (режим по умолчанию)</td>
  </tr>
  <tr>
    <td><b>-r rev</b></td>
    <td>Использовать номер или метку конкретной версии</td>
  </tr>
</table>

В табл. 14.18 показано, какие общие параметры доступны для каждой пользовательской команды.

Таблица 14.18. Применимость общих параметров клиента

<table>
  <tr>
    <th>Команда</th>
    <th>-D</th>
    <th>-f</th>
    <th>-k</th>
    <th>-l</th>
    <th>-n</th>
    <th>-R</th>
    <th>-r</th>
  </tr>
  <tr>
    <td>add</td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>annotate</td>
    <td>•</td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>checkout</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>commit</td>
    <td></td>
    <td></td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>diff</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>edit</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>editors</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>export</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>help</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>history</td>
    <td>•</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
  </tr>
  <tr>
    <td>import</td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>log</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>login</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>