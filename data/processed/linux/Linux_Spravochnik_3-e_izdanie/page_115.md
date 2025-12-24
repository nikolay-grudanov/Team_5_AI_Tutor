---
source_image: page_115.png
page_number: 115
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.21
tokens: 11673
characters: 1511
timestamp: 2025-12-24T03:20:27.571771
finish_reason: stop
---

<table>
  <tr>
    <th>debugfs</th>
    <td>
      <b>testi block</b><br>
      Проверить, занят ли inode-блок, соответствующий указанному файлу.<br>
      <b>unlink file</b><br>
      Удалить ссылку на файл.<br>
      <b>write source_file file</b><br>
      Создать в файловой системе файл <i>file</i> и скопировать в него содержимое файла <i>source_file</i>.
    </td>
  </tr>
  <tr>
    <th>depmod</th>
    <td>
      <b>depmod [options] modules</b><br>
      Команда системного администрирования. Создать файл зависимостей для указанных в командной строке модулей (<i>modules</i>). Файл зависимостей может использоваться программой modprobe для автоматической загрузки необходимых модулей. Обычной практикой применения depmod является включение вызова /sbin/depmod -a в один из файлов каталога /etc/rc.d, чтобы корректные зависимости модулей были доступны сразу же после загрузки системы.<br>
      <b>Параметры</b><br>
      <b>-a</b> Создать зависимости для всех модулей, перечисленных в файле /etc/conf.modules.<br>
      <b>-d</b> Режим отладки. Отображать все выполняемые команды.<br>
      <b>-e</b> Перечислять не найденные в модулях имена (unresolved symbols).<br>
      <b>-v</b> Перечислять обработанные модули.<br>
      <b>Файлы</b><br>
      <i>/etc/conf.modules</i><br>
      Информация о модулях и их зависимостях, о каталогах, в которых расположены различные типы модулей.<br>
      <i>/sbin/insmod, /sbin/rmmod</i><br>
      Программы, с которыми работает depmod.
    </td>
  </tr>
</table>