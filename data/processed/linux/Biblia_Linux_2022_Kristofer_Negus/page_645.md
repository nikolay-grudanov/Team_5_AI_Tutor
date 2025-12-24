---
source_image: page_645.png
page_number: 645
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.13
tokens: 7873
characters: 2653
timestamp: 2025-12-24T05:03:40.589926
finish_reason: stop
---

<table>
  <tr>
    <th>Имя журнала</th>
    <th>Имя файла</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>FTP Transfer Log</td>
    <td>xferlog</td>
    <td>Содержит информацию о файлах, передаваемых с помощью службы FTP</td>
  </tr>
  <tr>
    <td>GNOME Display Manager Log</td>
    <td>/var/log/gdm/:0.log</td>
    <td>Содержит сообщения, связанные с экраном входа в систему (GNOME display manager). Да, в имени файла действительно есть двоеточие</td>
  </tr>
  <tr>
    <td>LastLog</td>
    <td>lastlog</td>
    <td>Записывает последний вход учетной записи в систему</td>
  </tr>
  <tr>
    <td>Login/out Log</td>
    <td>wtmp</td>
    <td>Содержит историю входов в систему и выходов из нее</td>
  </tr>
  <tr>
    <td>Mail Log</td>
    <td>maillog</td>
    <td>Содержит информацию об адресах, на которые и с которых было отправлено электронное письмо. Полезно для обнаружения спама</td>
  </tr>
  <tr>
    <td>MySQL Server Log</td>
    <td>mysqld.log</td>
    <td>Включает в себя информацию, связанную с деятельностью сервера баз данных MySQL (mysqld)</td>
  </tr>
  <tr>
    <td>News Log</td>
    <td>spooler</td>
    <td>Предоставляет каталог, содержащий журналы сообщений с сервера новостей Usenet, если он запущен</td>
  </tr>
  <tr>
    <td>Samba Log</td>
    <td>/var/log/samba/smbd.log/ var/log/samba/nmbd.log</td>
    <td>Показывает сообщения от демона файловой службы Samba SMB</td>
  </tr>
  <tr>
    <td>Security Log</td>
    <td>secure</td>
    <td>Записывает дату, время и продолжительность попыток входа в систему и сеансов</td>
  </tr>
  <tr>
    <td>Sendmail Log</td>
    <td>sendmail</td>
    <td>Показывает сообщения об ошибках, записанные демоном sendmail</td>
  </tr>
  <tr>
    <td>Squid Log</td>
    <td>/var/log/squid/access.log</td>
    <td>Содержит сообщения, связанные с прокси/кэш-сервером squid</td>
  </tr>
  <tr>
    <td>System Log</td>
    <td>messages</td>
    <td>Предоставляет файл журнала общего назначения, в который многие программы записывают сообщения</td>
  </tr>
  <tr>
    <td>UUCP Log</td>
    <td>uucp</td>
    <td>Показывает сообщения о состоянии от демона UNIX Copy Protocol</td>
  </tr>
  <tr>
    <td>YUM Log</td>
    <td>yum.log</td>
    <td>Показывает сообщения, связанные с программными пакетами RPM</td>
  </tr>
  <tr>
    <td>X.Org X11 Log</td>
    <td>Xorg.0.log</td>
    <td>Показывает сообщения, выводимые сервером X.Org X</td>
  </tr>
</table>

Файлы журналов, находящиеся в каталоге /var/log системы, зависят от того, какие службы вы задействуете. Кроме того, некоторые файлы журналов зависят от дистрибутива. Например, если используется дистрибутив Fedora, то не будет файла журнала dpkg.