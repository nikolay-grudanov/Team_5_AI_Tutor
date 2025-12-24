---
source_image: page_269.png
page_number: 269
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.87
tokens: 8521
characters: 3460
timestamp: 2025-12-24T04:40:10.604136
finish_reason: stop
---

2 lumpy@ubuntu:~$ rsync -avrz jake@grex.org:/usr/share/man/man1 .
receiving incremental file list
man1/
man1/acme-client.1
man1/addr2line.1
...
man1/i386/fdformat.1
man1/sparc64/
man1/sparc64/fdformat.1
man1/sparc64/mksuncd.1

sent 9,529 bytes received 4,180,838 bytes 239,449.54 bytes/sec
total size is 12,970,760 speedup is 3.10

Как оказывается на практике, использование «файловой» надстройки sftp-server(1) для безопасного доступа к дереву каталогов удаленных узлов имеет достаточно широкое распространение. В частности, терминальный файловый менеджер mc(1), W:[Midnight Commander], тоже является SSH:sftp-клиентом, что иллюстрирует листинг 6.20. Более того, при помощи FUSE-файловых систем sshfs(1) (см. листинг 3.29) или gvfs файлы SSH:sftp-серверов могут быть смонтированы в дерево каталогов так, что вообще любые программы смогут ими воспользоваться.

Листинг 6.20. Файловый менеджер mc(1) — клиент SSH (sftp)

<table>
  <tr>
    <th>Левая панель</th>
    <th>Файл</th>
    <th>Команда</th>
    <th>Настройки</th>
    <th>Правая панель</th>
  </tr>
  <tr>
    <td>Список файлов</td>
    <td></td>
    <td>правки</td>
    <td>/sh://jake@grex.org</td>
    <td>Время правки</td>
  </tr>
  <tr>
    <td>Быстрый просмотр</td>
    <td>C-x q</td>
    <td>8 12:56</td>
    <td>'и</td>
    <td>марта 28 21:50</td>
  </tr>
  <tr>
    <td>Информация</td>
    <td>C-x i</td>
    <td>15 2014</td>
    <td>/..</td>
    <td>-BВЕРХ-</td>
    <td>янв. 6 2012</td>
  </tr>
  <tr>
    <td>Дерево</td>
    <td></td>
    <td>3 12:27</td>
    <td>/.qt</td>
    <td>512</td>
    <td>янв. 21 2012</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>1 18:24</td>
    <td>/a</td>
    <td>512</td>
    <td>марта 6 2010</td>
  </tr>
  <tr>
    <td>Формат списка...</td>
    <td></td>
    <td>11 2013</td>
    <td>/afs</td>
    <td>512</td>
    <td>авг. 17 2011</td>
  </tr>
  <tr>
    <td>Порядок сортировки...</td>
    <td></td>
    <td>11 2013</td>
    <td>/altroot</td>
    <td>512</td>
    <td>июня 8 2015</td>
  </tr>
  <tr>
    <td>Фильтр...</td>
    <td></td>
    <td>31 21:04</td>
    <td>~bbs</td>
    <td>20</td>
    <td>янв. 22 2012</td>
  </tr>
  <tr>
    <td>Выбор кодировки...</td>
    <td>M-e</td>
    <td>3 2015</td>
    <td>/bin</td>
    <td>1024</td>
    <td>янв. 21 2012</td>
  </tr>
  <tr>
    <td>FTP-соединение...</td>
    <td></td>
    <td>11 2013</td>
    <td>/c</td>
    <td>512</td>
    <td>янв. 21 2012</td>
  </tr>
  <tr>
    <td>Shell-соединение...</td>
    <td></td>
    <td>9 18:37</td>
    <td>/cyberspace</td>
    <td>512</td>
    <td>янв. 21 2012</td>
  </tr>
  <tr>
    <td>Панелизация</td>
    <td></td>
    <td>29 01:03</td>
    <td>/dev</td>
    <td>39936</td>
    <td>марта 31 19:07</td>
  </tr>
  <tr>
    <td>Пересмотреть</td>
    <td>C-r</td>
    <td>1 17:24</td>
    <td>/etc</td>
    <td>4096</td>
    <td>апр. 3 03:04</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>11 2013</td>
    <td>/home</td>
    <td>512</td>
    <td>авг. 17 2011</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>22 10:17</td>
    <td>/mnt</td>
    <td>512</td>
    <td>янв. 21 2012</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>11 2013</td>
    <td>/root</td>
    <td>512</td>
    <td>дек. 2 23:20</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>/sbin</td>
    <td>2048</td>
    <td>янв. 22 2012</td>
  </tr>
</table>

-ВВЕРХ-

75G/454G (16%)

Совет: Макросы % работают даже в командной строке.
lumpy@ubuntu:~$