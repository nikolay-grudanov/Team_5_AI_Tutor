---
source_image: page_405.png
page_number: 405
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.92
tokens: 11670
characters: 1413
timestamp: 2025-12-24T03:33:16.841905
finish_reason: stop
---

<table>
  <tr>
    <th>tee</th>
    <td>
      <b>-i, --ignore-interrupts</b><br>
      Игнорировать сигналы прерываний.<br>
      <b>--help</b><br>
      Отобразить информацию по использованию и завершить работу.<br>
      <b>--version</b><br>
      Вывести информацию о версии и завершить работу.<br>
      <b>Пример</b><br>
      <code>ls -l | tee savefile</code> <i>Просмотреть листинг и сохранить его</i>
    </td>
  </tr>
  <tr>
    <th>telinit</th>
    <td>
      <b>telinit [option][runlevel]</b><br>
      Команда системного администрирования. Предписание init изменить уровень выполнения (<i>runlevel</i>). telinit является просто ссылкой на init — прадродителя всех процессов.<br>
      <b>Параметр</b><br>
      <b>-t seconds</b><br>
      Послать сигнал SIGKILL через <i>seconds</i> секунд после посылки SIGTERM. По умолчанию — через 20 секунд.<br>
      <b>Уровни выполнения</b><br>
      В зависимости от дистибутива уровни выполнения могут различаться, тем не менее, нижеперечисленные являются стандартными:<br>
      <b>0</b> Останов системы.<br>
      <b>1, s, S</b> Однопользовательский режим.<br>
      <b>6</b> Перезагрузка системы.<br>
      <b>a, b, c</b> Обрабатывать только записи /etc/inittab, отмеченные уровнями а, b и с.<br>
      <b>q, Q</b> Повторное чтение /etc/inittab.<br>
      Информация об уровнях выполнения системы содержится в файле /etc/inittab.
    </td>
  </tr>
</table>