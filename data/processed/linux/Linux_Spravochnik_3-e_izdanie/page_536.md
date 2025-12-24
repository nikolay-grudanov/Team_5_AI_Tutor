---
source_image: page_536.png
page_number: 536
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.30
tokens: 11766
characters: 1736
timestamp: 2025-12-24T03:39:16.721216
finish_reason: stop
---

> run sed from a shell program, not from the command line.
> END_ARCHIVE
XX This is often how a shell archive is "wrapped",
XX bundling text for distribution. You would normally
XX run sed from a shell program, not from the command line.

Для того чтобы перенаправить стандартный поток вывода в стандартный поток ошибок, можно использовать следующую команду:

$ echo "Usage error: see administrator" 1>&2

Следующая команда записывает результат (список файлов) в файл filelist, а сообщения об ошибках (файлы, к которым нет доступа) — в файл no_access:

$ find / -print > filelist 2>no_access

Сопроцессы

Сопроцессы являются уникальной возможностью интерпретатора bash и в других интерпретаторах не встречаются.

<table>
  <tr>
    <th>Синтаксис</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>cmd1 | cmd2 |&</td>
    <td>Сопроцессы; выполнять конвейерную последовательность в фоновом режиме. Командный интерпретатор создает двунаправленный конвейер, позволяя перенаправлять одновременно стандартный ввод и стандартный вывод.</td>
  </tr>
  <tr>
    <td>read -p var</td>
    <td>Читать ввод сопроцесса в переменную var.</td>
  </tr>
  <tr>
    <td>print -p string</td>
    <td>Передать строку string сопроцессу.</td>
  </tr>
  <tr>
    <td>cmd <&p</td>
    <td>Вводом для команды cmd являются данные сопроцесса.</td>
  </tr>
  <tr>
    <td>cmd >&p</td>
    <td>Вывод команды cmd перенаправляется сопроцессу.</td>
  </tr>
</table>

Примеры

cat memo
Sufficient unto the day is
A word to the wise.

ed - memo |&
print -p /word/
read -p search
print "$search"
A word to the wise.

Отобразить содержимое файла
Запустить сопроцессы
Послать команду ed сопроцессу
Прочитать вывод ed в переменную search
Отобразить строку на стандартный вывод