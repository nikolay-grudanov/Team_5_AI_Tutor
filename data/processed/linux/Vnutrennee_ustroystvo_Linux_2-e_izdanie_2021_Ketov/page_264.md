---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.80
tokens: 7597
characters: 2042
timestamp: 2025-12-24T04:39:25.735068
finish_reason: stop
---

с помощью проверки корректности его цифровой подписи удостоверяется в подлинности владельца вложенного ключа. Остается только убедиться, что владельцем вложенного ключа и является целевой сервер.

В примере из листинга 6.14 иллюстрируется первое присоединение к SSH-серверу grex.org (162.202.67.158), в результате чего был получен открытый ключ алгоритма W:[ECDSA], который, возможно, действительно принадлежит этому серверу, а не злоумышленнику посередине соединения. Единственный способ это проверить — заранее знать действительный открытый ключ SSH-сервера grex.org и побитно сверить его с присланным ключом, что довольно затруднительно сделать человеку. Поэтому на практике сверяют короткие хэш-суммы действительного и присланного ключей, называемые «отпечатками пальца» (fingerprint), совпадение которых гарантирует совпадение ключей. Хэш-суммы открытых ключей SSH-серверов заранее известны и открыто публикуются, например для grex.org — на Web-странице http://grex.cyberspace.org/faq.xhtml#sshfinger. После ручной сверки ключа ① при первом подключении он сохраняется в файле ~/.ssh/known_hosts для автоматической сверки при последующих подключениях.

Листинг 6.14. Первое присоединение к SSH-серверу

lumpy@ubuntu:~$ ssh jake@grex.org
The authenticity of host 'grex.org (75.61.90.157)' can't be established.
ECDSA key fingerprint is SHA256:pM03fe6UTyqtqzUMq5SmTmH5tqUuN9WdvIwdpcEJhSU.
Are Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ①
Warning: Permanently added 'grex.org,75.61.90.157' (ECDSA) to the list of known hosts.
jake@grex.org's password: P@ssw0rd ②

grex$ uname -a
OpenBSD grex.org 6.3 GENERIC#9 i386
grex$ whoami
jake
grex$ w
8:44PM up 41 days, 3:15, 8 users, load averages: 1.44, 1.46, 1.60
USER   TTY FROM           LOGING IDLE WHAT
cross  p0 166.84.136.80   01Nov19 2days -bash
mcd    p1 37.59.109.123   12Nov19 9days -zsh
fernand pa 24.78.62.91    11Nov1911days -ksh
cross  pi 166.84.136.80   Tue04PM 2days -bash

1 При этом подобрать другой ключ с такой же хэш-суммой практически невозможно.