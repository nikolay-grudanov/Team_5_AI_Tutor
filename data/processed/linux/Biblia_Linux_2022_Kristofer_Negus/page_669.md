---
source_image: page_669.png
page_number: 669
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.19
tokens: 7746
characters: 2138
timestamp: 2025-12-24T05:04:22.469022
finish_reason: stop
---

крытого/закрытого ключа для пользователя johndoe в соответствии с желаемыми настройками. Она также генерирует связку ключей для хранения этих ключей:

$ gpg2 --gen-key
gpg (GnuPG) 2.2.9; Copyright (C)
 2018 Free Software Foundation, Inc.
...
GnuPG needs to construct a user ID to identify your key.
Real name: John Doe
Email address: jdoe@example.com
You selected this USER-ID:
    "John Doe <jdoe@gmail.com>"
Change (N)ame, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.
<Во всплывающем окне появится запрос на ввод пароля>
Enter passphrase: ***********
Repeat passphrase: ***********
...
gpg: /home/jdoe/.gnupg/trustdb.gpg: trustdb created
gpg: key 383D645D9798C173 marked as ultimately trusted
gpg: directory '/home/jdoe/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/home/jdoe/.gnupg/openpgprevocs.d/7469BCD3D05A43130F1786E0383D645D9798C173.rev'
public and secret key created and signed.
pub    rsa2048 2019-10-27 [SC] [expires: 2021-10-26]
        7469BCD3D05A43130F1786E0383D645D9798C173
uid          John Doe <jdoe@example.com>
sub    rsa2048 2019-10-27 [E] [expires: 2021-10-26]

В предыдущем примере утилита gpg2 запрашивает несколько спецификаций для генерирования желаемых открытых/закрытых ключей:

● ID пользователя, который определяет часть открытого ключа пары «открытый/закрытый ключ»;
● адрес электронной почты, связанный с ключом;
● парольную фразу, которая и применяется для идентификации и защиты части закрытого ключа пары «открытый/закрытый ключ».

Пользователь johndoe может проверить свой набор ключей с помощью команды gpg2 --list-keys, как показано в следующем примере. Обратите внимание на то, что идентификатор пользователя (UID) открытого ключа отображается таким же, как был создан, и содержит настоящее имя пользователя johndoe, комментарий и адрес электронной почты:

$ gpg2 --list-keys
/home/jdoe/.gnupg/pubring.kbx
--------------------------
pub    rsa2048 2019-10-27 [SC] [expires: 2021-10-26]
        7469BCD3D05A43130F1786E0383D645D9798C173
uid          [ultimate] John Doe <jdoe@example.com>
sub    rsa2048 2019-10-27 [E] [expires: 2021-10-26]