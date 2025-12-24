---
source_image: page_138.png
page_number: 138
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.12
tokens: 6407
characters: 1288
timestamp: 2025-12-24T03:59:17.704011
finish_reason: stop
---

Листинг 7.1. Пример файла конфигурации sshd_config

# Какой порт будет использоваться для SSH-сервера.
# Порт по умолчанию - 22
# Теоретически, номер порта можно изменить, но на практике
# в этом нет необходимости. Защита с помощью изменения номера
# порта - дело неблагодарное, поскольку есть сканеры портов,
# которые могу легко вычислить номер порта
Port 22
# Какие адреса мы будем слушать. Чтобы sshd работал на всех
# интерфейсах, закомментируйте директиву ListenAddress
#ListenAddress ::
#ListenAddress 0.0.0.0

# Номер версии протокола
Protocol 2
# Ключи для протокола версии 2
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_dsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key

# Для улучшения безопасности включаем разделение привилегий
UsePrivilegeSeparation yes

# Время жизни (в секундах) и размер ключа сервера версии 1
KeyRegenerationInterval 3600
ServerKeyBits 768

# Журналирование
SyslogFacility AUTH
LogLevel INFO

# Аутентификация:
LoginGraceTime 120
# Если нужно запретить вход как root по ssh
# (это не запрещает команду
# su), выключите этот параметр (установите значение no).
PermitRootLogin yes
StrictModes yes

# Максимальное количество попыток аутентификации
#MaxAuthTries 3

# Использование RSA (yes)
RSAAuthentication yes
# Аутентификация с открытым ключом