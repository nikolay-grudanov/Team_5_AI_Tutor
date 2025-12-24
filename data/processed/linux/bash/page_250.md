---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.10
tokens: 7317
characters: 1439
timestamp: 2025-12-23T23:11:15.449999
finish_reason: stop
---

User profile
Home directory
Last logon                12/27/2018 9:47:22 AM

Logon hours allowed      All
Local Group Memberships   *accounting*Users
Global Group memberships *None
The command completed successfully.

Права доступа к файлам и списки управления доступом

После создания пользователей и групп им можно назначить полномочия. Полномочия определяют, что пользователь или группа может делать в системе, а что — не может.

Права доступа к файлам Linux

Пользователям и группам могут быть назначены основные права доступа к файлам в Linux. Существует три основных вида полномочий: полномочия на чтение (r), на запись (w) и на выполнение (x). Команду chown можно применять для передачи полномочий на использование (владение) файлом от одного пользователя другому. Например, присвоить права на владение и использование файла report.txt пользователю jsmith можно так:

chown jsmith report.txt

Команда chown также может использоваться для смены владельца группы файла report.txt на accounting:

chown :accounting report.txt

Следующая команда предоставляет пользователю права на чтение/запись/выполнение файла, владельцу группы — на чтение/запись файла, а всем другим пользователям — на чтение/выполнение файла report.txt:

chmod u=rwx,g=rw,o=rx report.txt

Проще предоставить права с помощью команды chmod и восьмеричных значений (0–7). Права, предоставленные в предыдущем коде, можно задать следующим образом:

chmod 765 report.txt