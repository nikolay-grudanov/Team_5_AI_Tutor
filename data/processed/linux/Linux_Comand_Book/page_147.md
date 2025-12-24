---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.21
tokens: 5920
characters: 1099
timestamp: 2025-12-24T04:07:43.736045
finish_reason: stop
---

whoami    coreutils
/usr/bin   stdin stdout -file --opt —help —version

Команда whoami выводит имя текущего, действующего пользователя. Оно может отличаться от имени пользователя, под которым вы входили в систему (выходные данные команды logname), если вы затем использовали команду su. Следующий пример показывает отличие команды whoami от команды logname.

$ logname   •-
smith
$ whoami
smith
$ su Password:
#logname
smith
#whoami
root

id [опции] [имя_пользователя]    coreutils
/usr/bin   stdin stdout -file —opt --help -version
Каждый пользователь имеет уникальный численный идентификатор (UID) и уникальный численный идентификатор группы (GID), в которую он входит по умолчанию. Команда id выводит эти идентификаторы с соответствующими им именами пользователя и группы.
$ id
uid=500(smith) gid=500(smith)
groups=500(smith),6(disk),490(src),501(cdwrite)

Полезные опции
- u    Вывести идентификатор действующего пользователя и завершить работу
- g    Вывести идентификатор действующей группы и завершить работу
- G    Вывести идентификаторы всех других групп, к которым принадлежит пользователь