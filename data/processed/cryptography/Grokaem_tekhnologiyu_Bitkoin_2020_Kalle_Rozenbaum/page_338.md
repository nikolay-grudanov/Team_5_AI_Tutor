---
source_image: page_338.png
page_number: 338
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.62
tokens: 7449
characters: 1738
timestamp: 2025-12-24T08:39:34.253692
finish_reason: stop
---

Подписание открытого ключа на нашем компьютере как доверенного

Мы убедились, что ключ действительно принадлежит команде Bitcoin Core, и установили его в свою систему с помощью gpg.

Теперь подпишете его своим закрытым ключом, чтобы запомнить этот ключ как доверенный. Команда Bitcoin Core наверняка выпустит новые версии Bitcoin Core в будущем, и если GnuPG запомнит этот открытый ключ как доверенный, нам не придется снова выполнять шаги проверки ключа при обновлении.

Вот как выглядит эта процедура:

1. Создать свой ключ.

2. Подписать открытый ключ Bitcoin Core своим закрытым ключом.

Создать свой ключ в GnuPG можно, выполнив следующую команду:

$ gpg --gen-key
gpg (GnuPG) 2.1.18; Copyright (C) 2017 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Note: Use "gpg --full-generate-key" for a full featured key generation dialog.
GnuPG needs to construct a user ID to identify your key.

GnuPG предложит ввести имя и адрес электронной почты. Ответим на эти вопросы; они будут использоваться для идентификации ключа:

Real name: Kalle Rosenbaum
Email address: kalle@example.com
You selected this USER-ID:
    "Kalle Rosenbaum <kalle@example.com>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit?

Продолжим, нажав клавишу O (заглавная латинская буква «О»). Затем нам нужно выбрать пароль для шифрования закрытого ключа. Выберите пароль и запомните его.

Чтобы сгенерировать ключ, может понадобиться некоторое время, потому что создание хороших случайных чисел для ключа — не самая быстрая процедура. По завершении команда выведет следующее:

public and secret key created and signed.

pub rsa2048 2018-04-27 [SC] [expires: 2020-04-26]