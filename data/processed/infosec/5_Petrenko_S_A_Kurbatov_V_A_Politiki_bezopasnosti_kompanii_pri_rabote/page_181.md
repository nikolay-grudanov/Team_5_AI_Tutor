---
source_image: page_181.png
page_number: 181
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.21
tokens: 11668
characters: 1508
timestamp: 2025-12-23T23:42:34.942811
finish_reason: stop
---

floodguard enable

Защита от атак с подменой адреса. Для защиты от атак с подменой адреса используется возможность проверки правильности адреса отправителя uRPF:

ip verify reverse-path interface AdminDmz
ip verify reverse-path interface WebDMZ
ip verify reverse-path interface ServiceDMZ
ip verify reverse-path interface SecureData
ip verify reverse-path interface Management
ip verify reverse-path interface Internal

Конфигурирование межсетевых экранов PIX для работы в режиме горячего резервирования. Настройка осуществляется следующим образом:
1. Выключить резервный межсетевой экран.
2. Синхронизировать время на обоих межсетевых экранах:

ntp authentication-key 1 md5 For$Ntp
ntp authenticate
ntp trusted-key 1
ntp server 172.16.6.41 key 1 source Management

3. Подключить failover-кабель к обоим межсетевым экранам.
4. Необходимо сконфигурировать только основной межсетевой экран.
5. В отличие от VRRP или HSRP Cisco PIX не требует дополнительного IP-адреса для режима failover.
6. Включить режим failover:

failover
failover link State

7. Определить IP-адреса для интерфейсов:

failover ip address AdminDMZ 172.16.1.2
failover ip address WebDMZ 172.16.3.2
failover ip address ServiceDMZ 172.16.4.2
failover ip address SecureData 172.16.5.2
failover ip address Management 172.16.6.2
failover ip address Internal 172.16.9.2
failover ip address State 172.16.1.66

8. Включить резервный межсетевой экран. Проверить функционирование.

Дополнительные настройки безопасности. С целью ограничения доступа и