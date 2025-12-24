---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.38
tokens: 7357
characters: 1939
timestamp: 2025-12-24T04:33:09.984765
finish_reason: stop
---

options. The : , true, false, and test builtins do not accept options and do not treat -- specially. The exit, logout, break, continue, let,
- cd [-L][-P [-e]] [-@]] [dir]
    Change the current directory to dir. if dir is not supplied, the value of the HOME shell variable is the default. Any additional ar

Однако обращаться каждый раз к весьма внушительной справке по командному интерпретатору не совсем удобно, поэтому встроенная в командный интерпретатор команда help позволяет получить краткую справку по встроенным командам интерпретатора (листинг 2.20).

Листинг 2.20. Встроенная справка командного интерпретатора

finn@ubuntu:~$ help -d help
help - Display information about builtin commands.
finn@ubuntu:~$ help -d cd
cd - Change the shell working directory.
finn@ubuntu:~$ help cd
cd: cd [-L][-P [-e]] [-@]] [каталог]
    Change the shell working directory.

    Change the current directory to DIR. The default DIR is the value of the HOME shell variable.

2.7. Пользователи и группы

Как было указано ранее, для начала работы в многопользовательской операционной системе пользователю необходимо «зарегистрироваться», предъявляя имя своей пользовательской учетной записи и пароль, подтверждающий право на ее использование. В результате регистрации в системе запускается командный интерпретатор — первая программа пользовательского сеанса.

Учетные записи (УЗ) служат для авторизации, т. е. для разграничения прав доступа субъектов (процессов пользователей или процессов системных служб) к объектам (файлам, другим процессам, системным вызовам пр.).

Различают пользовательские и групповые учетные записи, при этом каждая пользовательская учетная запись идентифицируется уникальным числовым «пользовательским идентификатором» — UID (User Identifier), а каждая групповая — таким же уникальным числовым «групповым идентификатором» GID (Group Identifier). Именно эти числовые идентификаторы и используются ядром операционной систе-