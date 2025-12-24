---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.49
tokens: 11662
characters: 1288
timestamp: 2025-12-24T03:20:20.128618
finish_reason: stop
---

<table>
  <tr>
    <th>debugfs</th>
    <th>Команды</th>
  </tr>
  <tr>
    <td></td>
    <td><b>cat file</b><br>Отобразить содержимое inode-блока на стандартный вывод.<br><b>cd directory</b><br>Сменить текущий рабочий каталог на указанный.<br><b>chroot directory</b><br>Сменить корневой каталог на указанный inode-блок.<br><b>close</b><br>Закрыть открытую в настоящий момент файловую систему.<br><b>clri file</b><br>Очистить содержимое inode-блока, соответствующего файлу <i>file</i>.<br><b>dump file out_file</b><br>Записать содержимое inode-блока в файл <i>out_file</i>.<br><b>expand_dir directory</b><br>Раскрыть каталог.<br><b>find_free_block [goal]</b><br>Найти первый свободный блок, начиная с <i>goal</i> (если задан), и занять его.<br><b>find_free_inode [dir [mode]]</b><br>Найти свободный inode-блок и занять его.<br><b>freeb block</b><br>Пометить блок <i>block</i> как свободный.<br><b>freei file</b><br>Освободить inode-блок, соответствующий указанному файлу <i>file</i>.<br><b>help</b><br>Вывести список команд debugfs.<br><b>icheck block</b><br>Выполнить перевод блок → inode-блок.<br><b>initialize device blocksize</b><br>Создать файловую систему ext2 на указанном устройстве.<br><b>kill_file file</b><br>Удалить файл и освободить занимаемые им блоки.</td>
  </tr>
</table>