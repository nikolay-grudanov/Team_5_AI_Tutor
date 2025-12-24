---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.28
tokens: 7888
characters: 2289
timestamp: 2025-12-24T04:24:54.816808
finish_reason: stop
---

Современные версии Windows шифруют пароль, но вы можете отключить эту возможность. Для этого в реестре нужно изменить параметр EnablePlainTextPassword, установив в нем значение 1. В Windows 9x этот параметр находится в реестре по адресу:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\VxD\VNETSUP

Для Windows NT это:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Rdr\Parameters

В Windows 2000 и более поздних версиях:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters

Если соответствующего параметра не существует, его следует создать. Он должен иметь тип Dword.

Если возникли проблемы с входом в систему, то переключите систему в режим работы с незашифрованными паролями. В этом случае Samba использует для авторизации файлы /etc/passwd и /etc/shadow. Полученный открытый пароль шифруется по алгоритму MD5 и сравнивается со значениями из этого файла.

Если вы работаете в режиме с шифрованными паролями, то при авторизации будет использоваться файл /etc/samba/smbpasswd (это можно изменить с помощью директивы smb passwd file). Такой файл необходим из-за отличий в шифровании Windows и Linux;

СОВЕТ
Не применяйте открытые пароли без особой надобности. Не забывайте о существовании программ-снифферов, которые анализируют сетевой трафик и позволяют найти пароли, передаваемые по сети. Если они не зашифрованы, то злоумышленник сможет проникнуть в вашу систему.

smb passwd file = файл — указывает на расположение файла с паролями. По умолчанию он находится в том же каталоге, где расположены конфигурационные файлы Samba;

ssl CA certFile = файл — задает файл сертификата, необходимый для работы протокола SSL, гарантирующего безопасность передачи данных;

unix password sync = yes — разрешает пользователям Windows менять пароль Samba, одновременно обновляя системные пароли в Linux. Если в этом нет необходимости, установите значение параметра no. Для работы этой директивы нужно указать программы, которые будут изменять пароли (параметр passwd program) и сообщения, появляющиеся перед пользователем (параметр passwd chat). Приведу пример использования:

unix password sync = Yes
passwd program = /usr/bin/passwd %u
passwd chat = *New*password* %n\n *Retype*new*password* %n\n *passwd:*all*authentication*tokens*updated*successfully*