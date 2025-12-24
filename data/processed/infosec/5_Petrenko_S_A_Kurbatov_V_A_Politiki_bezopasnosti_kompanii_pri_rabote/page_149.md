---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.39
tokens: 11662
characters: 1762
timestamp: 2025-12-23T23:41:06.113569
finish_reason: stop
---

enable secret Gh!U765H!!
no enable password

Отключение неиспользуемых возможностей управления. Для управления используется консольный доступ, поэтому все остальные способы доступа должны быть отключены:

...
line vty 0 15
no login
transport input none
transport output none
line aux 0
no login
transport input none
transport output none

Отключение возможности маршрутизатора загружать конфигурацию из сети:

...
no boot network
no service config

Настройка TACACS+. Необходимо защитить доступ для управления. Хотя этот доступ не разрешен по сети, нужно использовать TACACS+ для централизованного управления аутентификацией и авторизацией доступа с целью управления и журналирования изменений, произведенных на маршрутизаторах. TACACS+ был выбран вместо RADIUS по причине большей защищенности. Имя пользователя и пароль в TACACS+ шифруются, в то время как в RADIUS шифруется только пароль. При использовании Cisco ACS TACACS+ можно настроить детальные уровни доступа для различных пользователей и групп пользователей.
Определяем IP-адрес сервера TACACS+ и пароль для аутентификации:

...
tacacs-server 172.16.6.21
tacacs-server key F$!19Ту
tacacs-server attempts 3
ip tacacs source-interface Fa0/0

Далее настраивается аутентификация, авторизация и журналирование. TACACS+ будет использоваться в качестве главного средства аутентификации, а локальная база пользователей маршрутизатора будет использоваться в случае, если сервер TACACS+ станет недоступным. Для этого обязательно должны быть созданы локальные учетные записи на маршрутизаторе. Настройка использования TACACS+ для AAA:

...
aaa new-model
aaa authentication login default group tacacs+ local
aaa authentication enable default group tacacs+ enable
aaa authorization exec default group tacacs + local