---
source_image: page_716.png
page_number: 716
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.38
tokens: 7815
characters: 2614
timestamp: 2025-12-24T05:05:34.193137
finish_reason: stop
---

отображаются и соответствующие настройки MLS/MCS для каждого пользователя SELinux:

# semanage login -l
Login Name      SELinux User      MLS/MCS Range      Service
__default__     unconfined_u       s0-s0:c0.c1023     *
root            unconfined_u       s0-s0:c0.c1023     *

Чтобы увидеть текущих пользователей SELinux и связанные с ними роли, возьмите команду semanage user -l. В следующем примере частично отображены роли, сопоставленные с именами пользователей SELinux:

# semanage user -l

<table>
  <tr>
    <th>SELinux User</th>
    <th>Labeling Prefix</th>
    <th>MLS Level</th>
    <th>MCS Level</th>
    <th>MCS Range</th>
    <th>SELinux Roles</th>
  </tr>
  <tr>
    <td>guest_u</td>
    <td>user</td>
    <td>s0</td>
    <td>s0</td>
    <td>s0</td>
    <td>guest_r</td>
  </tr>
  <tr>
    <td>...</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>user_u</td>
    <td>user</td>
    <td>s0</td>
    <td>s0</td>
    <td>s0</td>
    <td>user_r</td>
  </tr>
  <tr>
    <td>xguest_u</td>
    <td>user</td>
    <td>s0</td>
    <td>s0</td>
    <td>s0</td>
    <td>xguest_r</td>
  </tr>
</table>

Если вам нужно добавить новое имя пользователя SELinux, снова примените утилиту semanage. На этот раз задействуется команда semanage user -a selinux_имя_пользователя. Сопоставить идентификатор входа с недавно добавленным именем пользователя SELinux можно с помощью команды semanage login -a -s selinux_имя_пользователя LoginID. Команда semanage — это мощный инструмент управления конфигурацией SELinux. Чтобы получить более подробную информацию о ней, см. справочные страницы.

Управление контекстом безопасности файла

Метки файлов имеют решающее значение для поддержания надлежащего контроля доступа к данным из файлов. SELinux устанавливает метки безопасности файлов при установке и перезагрузке системы, когда SELinux переключается из режима disabled в любой другой. Чтобы увидеть текущую метку файла (она же контекст безопасности), используйте команду ls -Z:

# ls -Z /etc/passwd
-rw-r--r--. root root system_u:object_r:etc_t:s0 /etc/passwd

Управлять метками контекста безопасности файлов можно с помощью нескольких команд (табл. 24.2).

Таблица 24.2. Команды управления метками контекста безопасности

<table>
  <tr>
    <th>Утилита</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>chcat</td>
    <td>Изменяет категории метки контекста безопасности файла</td>
  </tr>
  <tr>
    <td>chcon</td>
    <td>Изменяет метки контекста безопасности файла</td>
  </tr>
  <tr>
    <td>fixfiles</td>
    <td>Вызывает команду restorecon/setfiles</td>
  </tr>
</table>