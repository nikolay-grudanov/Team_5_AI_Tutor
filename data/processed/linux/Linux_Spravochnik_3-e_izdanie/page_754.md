---
source_image: page_754.png
page_number: 754
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.71
tokens: 11834
characters: 1655
timestamp: 2025-12-24T03:49:25.537331
finish_reason: stop
---

Таблица 14.8. Команды администратора

<table>
  <tr>
    <th>Команда</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>admin</td>
    <td>Выполнение задач администрирования</td>
  </tr>
  <tr>
    <td>adm</td>
    <td></td>
  </tr>
  <tr>
    <td>rcs</td>
    <td></td>
  </tr>
  <tr>
    <td>init</td>
    <td>Создание нового репозитория</td>
  </tr>
  <tr>
    <td>server</td>
    <td>Работа в серверном режиме</td>
  </tr>
</table>

Команда admin

admin
[ -b[rev] ]
[ -cstring ]
[ -kkflag ]
[ -l[rev] ]
[ -L ]
[ -mrev:msg ]
[ -nname[:[rev]] ]
[ -Nname[:[rev]] ]
[ -orange ]
[ -q ]
[ -sstate[:rev]
[ -t[file] ]
[ -t-string ]
[ -u[rev] ]
[ -U ]
[ files ... ]

Команда admin используется для выполнения задач администрирования. Если существует группа пользователей cvsadmin, только пользователи, входящие в эту группу, могут выполнять admin с параметрами, отличными от -k. Дополнительные параметры, которые могут быть использованы с командой admin, перечислены в табл. 14.9.

Таблица 14.9. Параметры команды admin

<table>
  <tr>
    <th>Параметр</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>-b[rev]</td>
    <td>Установить ветвь по умолчанию</td>
  </tr>
  <tr>
    <td>-cstring</td>
    <td>Вышел из употребления. Установить строку начала комментария</td>
  </tr>
  <tr>
    <td>-kkflag</td>
    <td>Установить значение по умолчанию для режима подстановки ключевых слов</td>
  </tr>
  <tr>
    <td>-l[rev]</td>
    <td>Заблокировать указанную версию</td>
  </tr>
  <tr>
    <td>-L</td>
    <td>Включить жесткую блокировку</td>
  </tr>
  <tr>
    <td>-mrev:msg</td>
    <td>Изменить запись в журнале версий для указанной версии</td>
  </tr>
</table>