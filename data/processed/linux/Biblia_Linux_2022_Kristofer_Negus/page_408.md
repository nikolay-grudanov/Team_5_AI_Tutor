---
source_image: page_408.png
page_number: 408
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.31
tokens: 7683
characters: 2497
timestamp: 2025-12-24T04:56:49.168844
finish_reason: stop
---

Каждая запись с директивой nameserver (имя сервера) идентифицирует IP-адрес DNS-сервера. Порядок записей определяет порядок проверки DNS-серверов. Если первая запись недоступна, вполне нормально, что отображаются две или три дополнительные. Более того, проверка недопустимого имени хоста для каждого сервера может занять слишком много времени.

Другой тип записи, которую можно добавить в этот файл, — запись поиска. Она позволяет указывать домены для поиска, когда имя хоста запрашивается по базовому имени, а не полному доменному имени. Записей поиска может быть несколько при идентификации одного или нескольких доменных имен после ключевого слова поиска, как в следующем примере:

search example.com example.org example.net

Параметры поиска разделены пробелами или отступами.

Файл /etc/nsswitch.conf. В отличие от предыдущих файлов, файлом /etc/nsswitch.conf управляет команда authselect и его нельзя изменять вручную. Чтобы внести изменения, отредактируйте файл //etc/authselect/user-nsswitch.conf и запустите команду authselect apply-changes.

Настройки в файле /etc/nsswitch.conf определяют, что преобразование имени хоста выполняется поиском сначала локального файла (файлов) /etc/hosts, а затем DNS-серверов, перечисленных в файле /etc/resolv.conf (dns). Значение переменной myhostname используется для того, чтобы гарантировать, что адрес всегда будет возвращаться хосту. Вот как выглядит запись hosts в файле /etc/resolv.conf в дистрибутиве Red Hat Enterprise Linux:

hosts:      files dns myhostname

Вы можете добавлять и другие местоположения, такие как базы данных Network Information Service (nis или nisplus), чтобы запросить перевод имени хоста в IP-адрес. Можно изменить порядок, в котором запрашиваются различные службы, а также проверить правильность преобразования имени хоста в IP-адрес с помощью различных команд.

Если вы хотите проверить, правильно ли запрашиваются ваши DNS-серверы, используйте команды host или dig, например:

$ host redhat.com
redhat.com has address 209.132.183.105
redhat.com mail is handled by 10 us-smtp-inbound-1.mimecast.com.
redhat.com mail is handled by 10 us-smtp-inbound-2.mimecast.com.

$ dig redhat.com
; <<>> DiG 9.11.11-RedHat-9.11.11-1.fc30 <<>> redhat.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 9948
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;redhat.com.           IN  A
...