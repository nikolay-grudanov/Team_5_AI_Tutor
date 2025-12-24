---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.10
tokens: 5963
characters: 1377
timestamp: 2025-12-24T04:08:27.300032
finish_reason: stop
---

mail [опции] получатель MailX
/bin stdin stdout - file -- opt --help --version
Программа mail (эквивалентно Mail)* — это быстрый, простой почтовый клиент. Большинство людей предпочитают для регулярного использования более мощные программы, но для быстрого обмена сообщениями через командную строку или скрипт действительно удобной оказывается программа mail.
Чтобы отправить короткое сообщение, введите следующие команды.
$ mail smith@example.com
Subject: my subject
I'm typing a message.
To end it, I type a period by itself on a line.
Cc: jones@example.com
$
* В более старых Unix-системах mail и Mail были разными программами, но в Linux это одно и то же: /usr/bin/Mail- это символьная ссылка на /bin/mail.

Чтобы отправить короткое сообщение одной командой, наберите следующее.
$ echo "Hello world" | mail -s "subject" smith@example.com
Чтобы отправить файл одной командой, используйте любую из следующих команд.
$ mail -s "my subject" smith@example.com < filename
$ cat filename | mail -s "my subject" smith@example.com
Обратите внимание на то, как легко вы можете отправлять выходные данные конвейера в виде почтовых сообщений.

Полезные опции
-s subject Установить поле SubpctfteMa) исходящего сообщения
-v Подробный режим: выводить сообщения о доставке почты
-c addresses Отправить копии сообщения заданным адресатам (CC), адреса в списке addresses разделяются запятыми