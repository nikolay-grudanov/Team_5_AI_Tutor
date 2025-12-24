---
source_image: page_879.png
page_number: 879
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.66
tokens: 7467
characters: 1832
timestamp: 2025-12-24T05:09:52.749563
finish_reason: stop
---

10. Чтобы удалить пакет, содержащий команду mogrify, из своей системы, введите следующее:

# yum remove ImageMagick

Глава 11. Управление учетными записями

Для выполнения упражнений, связанных с добавлением и удалением учетных записей пользователей, можно применять окно Users (Пользователи), программу User Manager (Менеджер пользователей) или инструменты командной строки, например команды useradd и usermod. Чтобы получить те же результаты, которые даны в ответах, не обязательно выполнять упражнения только описанным здесь способом.

Существует множество путей достижения одних и тех же результатов. Приведенные далее ответы показывают, как выполнить упражнения из командной строки. (Станьте суперпользователем, когда увидите приглашение.)

1. Чтобы добавить локальную учетную запись пользователя в систему Linux с именем jbaxter и полным именем John Baxter, которая применяет /bin/sh в качестве оболочки по умолчанию и имеет следующий доступный UID (ваш может отличаться от показанного), введите следующее. Можете применить команду grep для проверки новой учетной записи пользователя. Затем установите пароль My1N1te0ut для пользователя jbaxter:

# useradd -c "John Baxter" -s /bin/sh jbaxter
# grep jbaxter /etc/passwd
jbaxter:x:1001:1001:John Baxter:/home/jbaxter:/bin/sh
# passwd jbaxter
Changing password for user jbaxter
New password: My1N1te0ut!
Retype new password: My1N1te0ut!
passwd: all authentication tokens updated successfully

2. Чтобы создать учетную запись группы с именем testing, использующую идентификатор группы 315, введите следующее:

# groupadd -g 315 testing
# grep testing /etc/group
testing:x:315:

3. Чтобы добавить jbaxter в группу testing и группу bin, введите следующее:

# usermod -aG testing,bin jbaxter
# grep jbaxter /etc/group
bin:x:1:bin,daemon,jbaxter
jbaxter:x:1001:
testing:x:315:jbaxter