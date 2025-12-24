---
source_image: page_821.png
page_number: 821
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.84
tokens: 7498
characters: 1867
timestamp: 2025-12-24T05:08:19.428536
finish_reason: stop
---

$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/joe/.ssh/id_rsa): <ENTER>
Created directory '/home/joe/.ssh'.
Enter passphrase (empty for no passphrase): <ENTER>
Enter same passphrase again:
Your identification has been saved in /home/joe/.ssh/id_rsa.
Your public key has been saved in /home/joe/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Wz63Ax1UdZnX+qKDmefSAZc3zoKS791hfaHy+usRP7g joe@ansible
The key's randomart image is:
+---[RSA 3072]----+
|      ...*|
|     . o+|
|    . . .|
|   . + +|
| S..= * +|
| o+o + O.o|
| .ooB.Bo+o|
| *+O+o.O|
| ..=BEO |
+----[SHA256]-----+

3. С помощью команды ssh-copy-id скопируйте свой открытый ключ в корневую учетную запись на каждом хосте. В следующем цикле for выполняется копирование пароля пользователя на все три хоста:

$ for i in 1 2 3; do ssh-copy-id joe@host0$i; done
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed:
"/home/joe/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed
-- if you are prompted now it is to install the new keys
joe@host01's password: <пароль>

Number of key(s) added: 1
Now try logging into the machine, with: "ssh 'joe@host01'"
and check to make sure that only the key(s) you wanted were added.

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed:
"/home/joe/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed
-- if you are prompted now it is to install the new keys

joe@host02's password: <пароль> ...

Далее необходимо установить пакет ansible на узел управления (ansible). С этого момента вся работа выполняется из узла управления.