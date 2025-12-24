---
source_image: page_391.png
page_number: 391
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.74
tokens: 6313
characters: 1144
timestamp: 2025-12-24T04:04:26.953309
finish_reason: stop
---

$ curl --socks5-hostname localhost:9050 -O https://ubuntu.bigbluebutton.org/repo/bigbluebutton.asc
$ sudo apt-key add ./bigbluebutton.asc

Если у вас не получится скачать ASC-файл, он будет приложен к материалам для этой книги и вы сможете скачать его с сайта издательства. В книге листинг приводить не станем, поскольку очень сложно будет его перепечатать вручную и не допустить ошибок.

Добавляем репозиторий, указывая tor+https для того чтобы гарантировано добраться до пакетов:

$ echo "deb tor+https://ubuntu.bigbluebutton.org/xenial-220/ bigbluebutton-xenial main" | sudo tee /etc/apt/sources.list.d/bigbluebutton.list

Устанавливаем bigbluebutton и bbb-html5:

$ sudo apt-get update
$ sudo apt-get install bigbluebutton
$ sudo apt-get install bbb-html5

Поскольку мы используем Tor, загружаться пакеты будут медленно, но ничего, мы это переживем.

Примечание. Если вы используете Ubuntu 16.04, игнорируйте сообщение «Невозможность загрузить дополнительные файлы данных». Это известная ошибка 16.04 и она ни на что не влияет.

Теперь, когда все установлено, проверим, соответствует ли наша система требованиям BBB:

$ sudo bbb-conf -check