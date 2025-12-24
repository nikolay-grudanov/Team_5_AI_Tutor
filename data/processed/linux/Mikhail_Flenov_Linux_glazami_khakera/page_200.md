---
source_image: page_200.png
page_number: 200
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.22
tokens: 7727
characters: 1595
timestamp: 2025-12-24T04:24:28.444929
finish_reason: stop
---

# RhostsRSAAuthentication yes
# RSAAuthentication yes
# PasswordAuthentication yes
# FallBackToRsh no
# UseRsh no
# BatchMode no
# CheckHostIP yes
# StrictHostKeyChecking ask
# IdentityFile ~/.ssh/identity
# IdentityFile ~/.ssh/id_rsa
# IdentityFile ~/.ssh/id_dsa
# Port 22
# Protocol 2,1
# Cipher 3des
# Ciphers aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,arcfour
# EscapeChar ~
Host *
Protocol 2,1

Некоторые из этих параметров мы уже видели при рассмотрении серверного конфигурационного файла. Здесь также можно увидеть параметр Protocol, в котором указываются используемые версии SSH. В данном случае не стоит запрещать версию 1. На безопасность клиента это не повлияет, зато не будет проблем при подключении к серверу, который работает только на такой версии. Я надеюсь, что это будет не ваш сервер :).

Вот характерные для клиента команды:

☐ Host — сервер, к которому относятся следующие настройки;
☐ CheckHostIP — разрешение проверки IP-адреса с перечисленными в файле known_hosts адресами;
☐ Compression — разрешение (yes) или запрет (no) использования сжатия данных;
☐ KerberosAuthentication — разрешение (yes) или запрет (no) использования аутентификации по протоколу Kerberos;
☐ NumberOfPasswordPrompts — количество попыток ввода пароля. Если пароль не введен верно, то соединение разрывается;
☐ IdentityFile — имя файла, содержащего закрытые ключи пользователя;
☐ PasswordAuthentication — режим аутентификации по паролю.

5.3.5. Пример работы клиента SSH

Теперь рассмотрим на примере, как можно подключиться к удаленному серверу. Для этого служит команда:

ssh пользователь@сервер