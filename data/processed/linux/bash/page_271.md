---
source_image: page_271.png
page_number: 271
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.56
tokens: 7584
characters: 1765
timestamp: 2025-12-23T23:12:04.413679
finish_reason: stop
---

Таблица 21.1. Формат файла проверки

<table>
  <tr>
    <th>Значение</th>
    <th>Формат</th>
  </tr>
  <tr>
    <td>Наличие файла</td>
    <td>file <code>_file path_&gt;</code></td>
  </tr>
  <tr>
    <td>Отсутствие файла</td>
    <td>! file <code>_file path_&gt;</code></td>
  </tr>
  <tr>
    <td>Хеш файла</td>
    <td>hash <code>_sha1 hash_&gt; _file path_&gt;</code></td>
  </tr>
  <tr>
    <td>Значение раздела реестра</td>
    <td>reg "<code>_key path_&gt;" "&lt;_value_&gt;" "&lt;_expected_&gt;"</code></td>
  </tr>
  <tr>
    <td>Наличие пользователя</td>
    <td>user <code>_user id_&gt;</code></td>
  </tr>
  <tr>
    <td>Отсутствие пользователя</td>
    <td>!user <code>_user id_&gt;</code></td>
  </tr>
  <tr>
    <td>Наличие группы</td>
    <td>group <code>_group id_&gt;</code></td>
  </tr>
  <tr>
    <td>Отсутствие группы</td>
    <td>! group <code>_group id_&gt;</code></td>
  </tr>
</table>

В примере 21.1 показан образец файла конфигурации.

Пример 21.1. validconfig.txt

user jsmith
file "c:\windows\system32\calc.exe"
!file "c:\windows\system32\bad.exe"

Сценарий в примере 21.2 считывает ранее созданный файл конфигурации и подтверждает, что данная конфигурация в системе существует.

Пример 21.2. validateconfig.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# validateconfig.sh
#
# Описание:
# Проверка наличия указанной конфигурации
#
# Использование:
# validateconfig.sh < configfile
#
# спецификация конфигурации выглядит так:
# [[!]file|hash|reg|[!]user|[!]group] [args]
# примеры:
# file /usr/local/bin/sfx - файл существует
# hash 12384970347 /usr/local/bin/sfx - это хеш файла
# !user bono - нет разрешенного пользователя "bono"
# group students - должна быть группа students
#
# errexit - показать правильное использование и выйти