---
source_image: page_283.png
page_number: 283
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.95
tokens: 7828
characters: 2375
timestamp: 2025-12-24T09:18:15.996945
finish_reason: stop
---

Например, команда в листинге 13.1 показывает, что происходит при использовании пакета OpenSSL для инициирования TLS-подключения к www.google.com по сетевому порту 443, который предназначен для обмена данными по протоколу HTTP, защищенному TLS (т. е. HTTPS).

Листинг 13.1. Установление TLS-подключения к www.google.com и получение сертификатов для аутентификации этого подключения

$ openssl s_client -connect www.google.com:443
CONNECTED(00000003)
-- опущено --
---
Certificate chain
① 0 s:/C=US/ST=California/L=Mountain View/O=Google Inc/CN=www.google.com
    i:/C=US/O=Google Inc/CN=Google Internet Authority G2
② 1 s:/C=US/O=Google Inc/CN=Google Internet Authority G2
    i:/C=US/O=GeoTrust Inc./CN=GeoTrust Global CA
③ 2 s:/C=US/O=GeoTrust Inc./CN=GeoTrust Global CA
    i:/C=US/O=Equifax/OU=Equifax Secure Certificate Authority
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEgDCCA2igAwIBAgIISCr6QCbz5rowDQYJKoZIhvcNAQELBQAwSTELMAkGA1UE
BhMCVVVMxEzARBgNVBAoTCkdvb2dsZSBJbmMxJTAjBgNVBAMTHEdvb2dsZSBJbnRl
-- опущено --
cb9geU8in8yCaH8dtzrFyUracpMureWnBeajOYXRPTdCFccejAh/xyH5SKD00Z4v
3TP9GBtClAH1mSXoPhX73dp7jiPZqgbY4kiEDNx+hf0gmTUFBDHD0e0/s2nqwuwL
pBH6XQ==
-----END CERTIFICATE-----
subject=/C=US/ST=California/L=Mountain View/O=Google Inc/CN=www.google.com
issuer=/C=US/O=Google Inc/CN=Google Internet Authority G2
-- опущено --

Я оставил только интересную часть вывода, а именно сам сертификат. Обратите внимание, что до первого сертификата (начинающегося строкой BEGIN CERTIFICATE) расположено описание цепочки сертификатов, в которой строка, начинающаяся с s:, описывает имя субъекта, а строка, начинающаяся с i:, — владельца подписи. Здесь сертификат 0 выдан google.com ①, сертификат 1 ② принадлежит организации, подписавшей сертификат 0, а сертификат 2 ③ — организации, подписавшей сертификат 1. Организация, выпустившая сертификат 1 (GeoTrust), предоставила организации Google Internet Authority право выпуска сертификата (именно сертификата 0) для доменного имени www.google.com, делегировав тем самым доверие к Google Internet Authority.

Очевидно, что сами удостоверяющие центры должны быть достойны доверия и выпускать сертификаты только для заслуживающих доверия организаций и что они должны защищать свои закрытые ключи, чтобы никакой противник не мог выпустить сертификаты от их лица (например, с целью притвориться легитимным сервером google.com).