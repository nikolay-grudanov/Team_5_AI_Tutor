---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.91
tokens: 7816
characters: 1754
timestamp: 2025-12-24T04:24:14.069967
finish_reason: stop
---

• ssh_host_key.pub;
• ssh_host_rsa_key;
• ssh_host_rsa_key.pub.

Почему так много файлов с ключами? Просто SSH работает с разными алгоритмами шифрования и поддерживает два наиболее популярных и криптостойких алгоритма: DSA (ssh_host_dsa_key, ssh_host_dsa_key.pub) и RSA (ssh_host_rsa_key и ssh_host_rsa_key.pub).

Замечу, что первое сокращение — DSA — означает Digital Signature Algorithm (алгоритм цифровой подписи), тогда как второе — RSA, несмотря на схожесть написания, состоит из первых букв имен основателей одноименного алгоритма шифрования: Ronald Rivest, Adi Shamir и Leonard Adleman.

Оставшиеся два файла ssh_host_key и ssh_host_key.pub хранят ключи для первой версии SSH. Для каждого алгоритма требуется по два файла: с расширением pub — хранит открытый ключ, без расширения — содержит приватный ключ.

С помощью открытого ключа можно закодировать данные и отправить их на сервер, но для расшифровки нужен только закрытый ключ, который не может быть подобран простыми алгоритмами. Он должен быть только у вас, его необходимо беречь и никому не показывать.

5.3.2. Основные параметры конфигурации сервера SSH

Давайте теперь рассмотрим содержимое файла конфигурации SSH-сервера (sshd). Файл достаточно большой, и для экономии места я привел только небольшую его часть (листинг 5.1).

Листинг 5.1. Файл конфигурации sshd

#Port 22
#Protocol 2,1
#ListenAddress 0.0.0.0
#ListenAddress ::

# HostKey for protocol version 1
# Ключ для первой версии протокола
#HostKey /etc/ssh/ssh_host_key
# HostKeys for protocol version 2
# Ключи для второй версии протокола
#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_dsa_key

# Lifetime and size of ephemeral version 1 server key
# Время жизни и размер репернируемого серверного ключа версии 1