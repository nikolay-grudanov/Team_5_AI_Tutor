---
source_image: page_167.png
page_number: 167
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.42
tokens: 6342
characters: 1171
timestamp: 2025-12-24T03:59:48.957969
finish_reason: stop
---

# Для анонимного входа можно использовать как имя
# anonymous, так и ftp
UserAlias anonymous ftp

# Максимальное число одновременных анонимных
# пользователей
MaxClients 10
# Максимальный размер получаемого файла
#MaxRetrieveFileSize 512 Mb

# Ограничиваем скорость передачи данных до 255 Кайт/с
#TransferRate APPE,RETR,STOR,STOU 255

# Файл 'welcome.msg' будет отображаться при входе, а файл
# '.message' при
# каждом новом изменении каталога
DisplayLogin welcome.msg
DisplayChdir .message

# Далее следует закомментированная секция Directory,
# позволяющая указать
# параметры каталога. В данном случае ограничивается
# доступ к каталогу
# pub. Получить доступ к нему могут только сети
# .examples.net и с IP
# 113.141.114.1
#<Directory pub>
# <Limit ALL>
# Order Allow,Deny
# Allow from .examples.net,113.141.114.1
# Deny from All
# </Limit>
#</Directory>

# Следующая секция содержит параметры каталога uploads,
# который обычно
# используется для загрузки файлов анонимными пользователями
# на сервер.
# Если вам нужна такая возможность, раскомментируйте эту
# секцию
# Мы запретили чтение этого каталога, но разрешили
# загрузку в него файлов
#<Directory uploads/*>