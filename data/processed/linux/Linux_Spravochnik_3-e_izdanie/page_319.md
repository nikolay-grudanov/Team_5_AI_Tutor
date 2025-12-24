---
source_image: page_319.png
page_number: 319
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.03
tokens: 11779
characters: 1825
timestamp: 2025-12-24T03:29:36.222560
finish_reason: stop
---

<table>
  <tr>
    <th>nslookup</th>
    <td>
      <b>server domain</b><br>
      Изменить сервер по умолчанию на <i>domain</i>. Использовать текущий сервер по умолчанию для поиска информации о сервере <i>domain</i>.
      <br>
      <b>set keyword[=value]</b><br>
      Изменить информацию состояния, влияющую на поиск. Допустимые ключевые слова:
      <ul>
        <li><b>all</b><br>
          Вывести текущие значения часто используемых аргументов <b>set</b>.
        </li>
        <li><b>class=name</b><br>
          Установить класс запросов в IN (Интернет), CHAOS, HESIOD или ANY. По умолчанию устанавливается IN.
        </li>
        <li><b>domain=name</b><br>
          Изменить имя домена по умолчанию на <i>name</i>.
        </li>
        <li><b>[no]debug</b><br>
          Включение и выключение режима отладки.
        </li>
        <li><b>[no]d2</b><br>
          Включение и выключение режима исчерпывающей отладки.
        </li>
        <li><b>[no]defname</b><br>
          Добавлять в каждый запрос имя домена по умолчанию.
        </li>
        <li><b>[no]ignoretc</b><br>
          Игнорировать ошибку усечения.
        </li>
        <li><b>[no]recurse</b><br>
          Предписание серверу имен опрашивать или не опрашивать другие серверы, если на нем нет требуемой информации.
        </li>
        <li><b>[no]search</b><br>
          Для <i>defname</i> производить поиск всех имен в родительских или в текущем доменах.
        </li>
        <li><b>[no]vc</b><br>
          Всегда использовать виртуальный канал при посылке запросов к серверу.
        </li>
        <li><b>port=port</b><br>
          Назначить указанный порт <i>port</i> для подключения к серверу.
        </li>
        <li><b>querytype=value</b><br>
          См. <b>type=value</b>.
        </li>
      </ul>
    </td>
  </tr>
</table>