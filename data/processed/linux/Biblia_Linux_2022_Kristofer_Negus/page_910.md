---
source_image: page_910.png
page_number: 910
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.26
tokens: 7535
characters: 1802
timestamp: 2025-12-24T05:10:43.913366
finish_reason: stop
---

2. Чтобы сгенерировать пару ключей с помощью утилиты gpg2, введите следующее:

$ gpg2 --gen-key

Необходимо добавить:
а) настоящее имя и адрес электронной почты;
б) ключевую фразу для личного пароля.

3. Чтобы перечислить сгенерированные ключи, введите:

$ gpg2 --list-keys

4. Чтобы зашифровать файл и добавить свою цифровую подпись с помощью утилиты gpg2, выполните следующие действия:
а) сгенерируйте связку ключей (см. упражнение 2);
б) после этого введите:

$ gpg2 --output EncryptedSignedFile --sign FiletoEncryptSign

5. На странице getfedora.org выберите один из дистрибутивов Fedora для загрузки. Когда она будет завершена, выберите Verify your Download (Проверить загруженный образ), чтобы просмотреть инструкции по проверке образа. Например, загрузите файл CHECKSUM для загруженного образа, а затем введите следующее:

$ curl https://getfedora.org/static/fedora.gpg | gpg --import
$ gpg --verify-files *-CHECKSUM
$ sha256sum -c *-CHECKSUM

6. Чтобы определить, подключена ли команда su в вашей системе Linux к PAM, введите следующее:

$ ldd $(which su) | grep pam
libpam.so.0 => /lib64/libpam.so.0 (0x00007fca14370000)
libpam_misc.so.0 => /lib64/libpam_misc.so.0 (0x00007fca1416c000)

Если команда su в системе Linux поддерживает PAM, то после выполнения команды ldd вы увидите в списке имя библиотеки PAM.

7. Чтобы определить, есть ли у команды файл конфигурации PAM, введите следующее:

$ ls /etc/pam.d/su
/etc/pam.d/su

Если файл существует, то, чтобы отобразить его содержимое, введите в командной строке следующее (контексты модулей PAM, которые модули используют, включают любое из следующих значений — auth, account, password или session):

$ cat /etc/pam.d/su

8. Чтобы перечислить различные модули PAM в системе Fedora или RHEL, введите следующее:

$ ls /usr/lib64/security/pam*.so