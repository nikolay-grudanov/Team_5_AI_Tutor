---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.03
tokens: 6283
characters: 1072
timestamp: 2025-12-24T03:59:43.088625
finish_reason: stop
---

### #
# Включаем другие конфигурационные файлы
#include /etc/proftpd/conf.d/*.conf

####

# ---------------------------------------------
# Настройки анонимного доступа
# ---------------------------------------------
# Базовая анонимная конфигурация, загрузка файлов
# на сервер запрещена
# Анонимным пользователям можно только скачивать файлы с сервера
# Если вам не нужен анонимный вход, просто удалите секцию
# <Anonymous>

<Anonymous ~ftp>
    # Limit LOGIN
    #<Limit LOGIN>
    # Order Allow,Deny
    # Allow from .examples.net,113.141.114.1
    # Deny from All
    #</Limit>

    # Ограничиваем WRITE везде, запрещаем запись полностью
    <Limit WRITE>
        DenyAll
    </Limit>

    # LoginPasswordPrompt -- будем ли отображать приветствие
    # или нет
    LoginPasswordPrompt off

    # DirFakeMode -- прячем настоящие разрешения файлов/
    # каталогов
    DirFakeMode 0640

    # DirFakeUser -- прячем настоящих владельцев файлов/
    # каталогов
    DirFakeUser On

    # DirFakeGroup -- скрываем настоящую группу файла/
    # каталога
    DirFakeGroup On