---
source_image: page_186.png
page_number: 186
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.00
tokens: 11789
characters: 1756
timestamp: 2025-12-24T03:23:43.273896
finish_reason: stop
---

<table>
  <tr>
    <th>Файлы</th>
    <th></th>
  </tr>
  <tr>
    <td>/etc/gcd.conf+</td>
    <td>Испытательный файл настройки. Если конфигурация работает удовлетворительно, необходимо выполнить gated newconf, чтобы испытательный файл стал постоянным файлом настройки /etc/gated.conf.</td>
  </tr>
  <tr>
    <td>/etc/gated.conf–</td>
    <td>Резервная копия старого файла настройки.</td>
  </tr>
  <tr>
    <td>/etc/gated.conf—</td>
    <td>Резервная копия резервной копии старого файла настройки.</td>
  </tr>
  <tr>
    <td>/etc/gated.conf</td>
    <td>Собственно файл настройки.</td>
  </tr>
  <tr>
    <td>/etc/gated.pid</td>
    <td>Идентификатор процесса gated.</td>
  </tr>
  <tr>
    <td>/usr/tmp/gated_dump</td>
    <td>Файл состояния.</td>
  </tr>
  <tr>
    <td>/usr/tmp/gated_parse</td>
    <td>Перечень ошибок разбора, найденных при чтении файла настройки.</td>
  </tr>
  <tr>
    <th>getkeycodes</th>
    <th></th>
  </tr>
  <tr>
    <td colspan="2">Команда выдает таблицы преобразования скан-кодов в коды клавиш.</td>
  </tr>
  <tr>
    <th>getty [options] port [speed [term [lined]]]</th>
    <th></th>
  </tr>
  <tr>
    <td colspan="2">Команда системного администрирования. Установка типа терминала, режимов, скорости и характеристик линии. На системах Linux иногда для этой цели используется agetty, что подразумевает отличный синтаксис. getty запускается программой init. Это второй из процессов в последовательности init-getty-login-shell, которая в конечном итоге соединяет пользователя с системой. getty считывает имя пользователя и выполняет команду login с именем пользователя в качестве аргумента. В процессе считывания имени getty пытается адаптировать систему к скорости и типу установленного устройства.</td>
  </tr>
</table>