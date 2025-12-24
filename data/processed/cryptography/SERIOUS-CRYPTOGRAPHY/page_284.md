---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.10
tokens: 7760
characters: 2039
timestamp: 2025-12-24T09:18:20.827170
finish_reason: stop
---

Чтобы узнать, что находится внутри сертификата, выполним команду, показанную в листинге 13.2, и скопируем первый сертификат из листинга 13.1.

Листинг 13.2. Декодирование сертификата, полученного от www.google.com

$ openssl x509 -text -noout
-----BEGIN CERTIFICATE-----
--опущено--
-----END CERTIFICATE-----
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 5200243873191028410 (0x482afa4026f3e6ba)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=Google Inc, CN=Google Internet Authority G2
        Validity
            Not Before: Dec 15 14:07:56 2016 GMT
            Not After : Mar 9 13:35:00 2017 GMT
        Subject: C=US, ST=California, L=Mountain View, O=Google Inc, CN=www.google.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            Public-Key: (2048 bit)
            Modulus:
                00:bc:bc:b2:f3:1a:16:3b:c6:f6:9d:28:e1:ef:8e:
                92:9b:13:b2:ae:7b:50:8f:f0:b4:e0:36:8d:09:00:
            Exponent: 65537 (0x10001)
        Signature Algorithm: sha256WithRSAEncryption
            94:cd:66:55:83:f1:16:7d:46:d8:66:21:06:ec:c6:9d:7c:1c:
            2b:c1:f6:4f:b7:3e:cd:01:ad:69:bd:a1:81:6a:7c:96:f5:9c:
        Signature Algorithm: sha256WithRSAEncryption
            85:fa:2b:99:35:05:04:31:c3:d1:e3:bf:b3:69:ea:c2:e5:8b:
            a4:11:fa:5d

Здесь мы видим результат декодирования командой openssl x509 сертификата, представленного блоком текста в кодировке base64. Поскольку OpenSSL знает структуру этого блока, он может сказать, что находится внутри сертификата, в т. ч. серийный номер, информацию о версии, идентифицирующую информацию, срок действия (строки Not Before (не раньше) и Not After (не позже)), открытый ключ (в данном случае модуль и открытый показатель степени RSA) и подпись всего вышеперечисленного.

Хотя специалисты по безопасности и криптографы часто заявляют, что вся система сертификатов изначально порочна, это одно из лучших имеющихся в нашем распоряжении решений — наряду с полити-