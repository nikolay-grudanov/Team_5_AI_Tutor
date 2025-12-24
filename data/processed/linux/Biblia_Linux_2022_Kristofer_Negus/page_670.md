---
source_image: page_670.png
page_number: 670
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.40
tokens: 7700
characters: 2295
timestamp: 2025-12-24T05:04:20.732717
finish_reason: stop
---

После создания пары ключей и их связки файлы могут быть зашифрованы и расшифрованы. В первую очередь открытый ключ должен быть извлечен из связки ключей, чтобы его можно было использовать совместно. В следующем примере утилита gpg2 применяется для извлечения открытого ключа из связки ключей пользователя johndoe. Извлеченный ключ помещается в файл совместного применения. Имя файла может быть любым. В данном случае пользователь johndoe выбрал имя файла JohnDoe.pub:

$ gpg2 --export John Doe > JohnDoe.pub
$ ls *.pub
JohnDoe.pub
$ file JohnDoe.pub
JohnDoe.pub: PGP/GPG key public ring (v4) created Sun Oct 27 16:24:27 2019 RSA (Encrypt or Sign) 2048 bits MPI=0xc57a29a6151b3e8d...

Передача открытого ключа. Файл, содержащий открытый ключ, может быть передан любым доступным способом. Его можно отправить в виде вложения по электронной почте или даже разместить на веб-странице. Открытый ключ — он и есть открытый, поэтому нет необходимости его скрывать. В следующем примере пользователь johndoe передал файл, содержащий его открытый ключ, пользователю jill. Далее последний добавляет открытый ключ пользователя johndoe в свою связку ключей с помощью команды gpg2 --import. Пользователь jill убеждается, что открытый ключ johndoe добавлен, с помощью команды gpg2 --list-keys, которая просматривает ключи в общей связке ключей:

$ ls *.pub
JohnDoe.pub
$ gpg2 --import JohnDoe.pub
gpg: directory '/home/jill/.gnupg' created
...
gpg: directory '/home/jill/.gnupg' created
gpg: keybox '/home/jill/.gnupg/pubring.kbx' created
gpg: /home/jill/.gnupg/trustdb.gpg: trustdb created
gpg: key 383D645D9798C173: public key "John Doe <jdoe@example.com>" imported
gpg: Total number processed: 1
gpg:                imported: 1
$ gpg2 --list-keys
/home/jill/.gnupg/pubring.gpg
--------------------------
pub    rsa2048 2019-10-27 [SC] [expires: 2021-10-26]
        7469BCD3D05A43130F1786E0383D645D9798C173
uid          [ unknown] John Doe <jdoe@example.com>
sub    rsa2048 2019-10-27 [E] [expires: 2021-10-26]

Шифрование сообщения электронной почты. Добавленный в связку ключей открытый ключ можно применять для шифрования данных для первоначального владельца. В приведенном далее примере кода обратите внимание на то, что пользователь jill создал текстовый файл MessageForJohn.txt для пользователя johndoe.