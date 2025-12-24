---
source_image: page_801.png
page_number: 801
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.00
tokens: 11860
characters: 1846
timestamp: 2025-12-24T03:51:41.520723
finish_reason: stop
---

<table>
  <tr>
    <th>rcs</th>
    <td>ниe было произведено кем-то другим, вам будет предложено ввести причину нарушения блокировки. Сообщение отправляется по электронной почте пользователю, заблокировавшему файл.<br><b>-U</b> Включить мягкую блокировку. Все, кроме владельца файла, должны использовать со <b>-l</b> для его редактирования (см. <b>-L</b>).<br><b>-V</b> Вывести номер версии RCS.<br><b>-zzone</b><br>Установить часовой пояс по умолчанию для временных отметок, создаваемых командами <i>ci</i> и <i>co</i>.</td>
  </tr>
  <tr>
    <th colspan="2">Примеры</th>
  </tr>
  <tr>
    <td colspan="2">Связать метку <b>To_customer</b> с последней версией всех файлов RCS:</td>
  </tr>
  <tr>
    <td colspan="2">rcs -nTo_customer: RCS/*</td>
  </tr>
  <tr>
    <td colspan="2">Добавить трех пользователей в список доступа для файла <b>beatle_deals</b>:</td>
  </tr>
  <tr>
    <td colspan="2">rcs -ageorge,paul,ringo beatle_deals</td>
  </tr>
  <tr>
    <td colspan="2">Удалить версии с 1.2 по 1.5:</td>
  </tr>
  <tr>
    <td colspan="2">rcs -o1.2-1.5 doc</td>
  </tr>
  <tr>
    <td colspan="2">Заменить описание файла RCS значением переменной:</td>
  </tr>
  <tr>
    <td colspan="2">echo "$description" | rcs -t file</td>
  </tr>
  <tr>
    <th>rcsclean</th>
    <td><b>rcsclean [options] [files]</b><br>Сравнить извлеченные файлы с соответствующей последней версией или версией <i>R</i> (в зависимости от параметров командной строки). Если различия отсутствуют, рабочий файл удаляется. (Для поиска различий используйте rcsdiff.) Команда rcsclean полезна для файлов сборки (makefiles). Например, можно создать цель «clean-up» для обновления ваших каталогов. rcsclean также полезно использовать перед выполнением rcsfreeze. rcsclean работает со стандартными параметрами <b>-q</b>, <b>-V</b>, <b>-x</b> и <b>-z</b>.</td>
  </tr>
</table>