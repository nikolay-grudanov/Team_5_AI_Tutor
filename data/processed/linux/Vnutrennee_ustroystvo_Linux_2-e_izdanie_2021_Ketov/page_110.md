---
source_image: page_110.png
page_number: 110
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.01
tokens: 7429
characters: 2055
timestamp: 2025-12-24T04:34:57.204372
finish_reason: stop
---

В результате найдено правило ①, разрешающее доступ субъектов с типом unconfined_t к объектам, типы которых «обобщаются» атрибутом user_home_type.

При помощи команды seinfo(1) уточняется, что тип (-t, type) ssh_home_t действительно обобщен атрибутом ② user_home_type, и, наоборот, атрибут user_home_type обобщает такие «пользовательские» типы ③, как ssh_home_t, audio_home_t, user_home_t и пр.

Другими словами, всем процессам пользовательского сеанса (т. к. они имеют тип unconfined_t) разрешено обращаться к пользовательским SSH-ключам (имеющим тип ssh_home_t) и любым другим пользовательским данным (с типами audio_home_t, user_home_t и пр.).

Для ограничения программ в доступе к SSH-ключам пользователей потребуется некоторый другой тип (отличный от unconfined_t), которому правилами политики будет запрещено обращаться к файлам с типом ssh_home_t. Такими типами в целевой политике являются несколько типов «песочниц» (sandbox), например sandbox_t или sandbox_net_t (разрешающий сетевые соединения).

В примере из листинга 3.55 поиск ① разрешающих правил показывает, что процессам с типом sandbox_net_t не разрешено открытие файлов с типом ssh_home_t, но разрешены ② TCP-соединения. Таким образом, тип sandbox_net_t оказывается подходящим кандидатом процессов тех программ, которым нужно ограничить доступ к SSH-ключам и другим файлам пользователя.

Листинг 3.55. Мандатные правила типа sandbox_net_t

① [lich@centos ~]$ sesearch -A -s sandbox_net_t -t ssh_home_t -c file -p open
!
② [lich@centos ~]$ sesearch -A -s sandbox_net_t -c tcp_socket -p connect
Found 4 semantic av rules:
    allow sandbox_net_t sandbox_net_t: tcp_socket { ... read write ... connect ... shutdown } ;
[lich@centos ~]$ links -dump ~/.ssh/id_rsa
? -----BEGIN RSA PRIVATE KEY-----
... ... ... ...
-----END RSA PRIVATE KEY-----
[lich@centos ~]$ sandbox -t sandbox_net_t links -dump ~/.ssh/id_rsa
③ ELinks: Отказано в доступе

Запустить программу в процессе с соответствующей меткой позволяет команда sandbox(8), специально предназначенная для формирования «песочниц» при помощи