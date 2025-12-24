---
source_image: page_880.png
page_number: 880
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.74
tokens: 7719
characters: 2225
timestamp: 2025-12-24T05:10:04.113478
finish_reason: stop
---

4. Чтобы стать пользователем jbaxter и временно сделать группу testing группой jbaxter по умолчанию, запустите файл touch /home/jbaxter/file.txt так, чтобы группа testing была назначена в качестве его группы:

$ su - jbaxter
Password: My1N1te0ut!
sh-4.2$ newgrp testing
sh-4.2$ touch /home/jbaxter/file.txt
sh-4.2$ ls -l /home/baxter/file.txt
-rw-rw-r--. 1 jbaxter testing 0 Jan 25 06:42 /home/jbaxter/file.txt
sh-4.2$ exit ; exit

5. Обратите внимание на то, какой идентификатор пользователя был назначен пользователю jbaxter, а затем удалите учетную запись пользователя, не удаляя домашний каталог, назначенный для jbaxter:

$ userdel jbaxter

6. Примените следующую команду, чтобы найти в каталоге /home (и любых подкаталогах) все файлы, назначенные идентификатору пользователя, который недавно принадлежал пользователю с именем jbaxter. (У меня оба идентификатора, UID и GID, были 1001, ваши могут отличаться.) Обратите внимание на то, что имя пользователя jbaxter больше не назначается в системе, поэтому любые файлы, созданные пользователем, перечислены как принадлежащие к UID 1001 и GID 1001, за исключением нескольких файлов, которые были назначены группе testing из-за команды newgrp, выполненной ранее:

# find /home -uid 1001 -ls
262184 4 drwx------ 4 1001 1001 4096 Jan 25 08:00 /home/jbaxter
262193 4 -rw-r--r-- 1 1001 1001 176 Jan 27 2011 /home/jbaxter/.bash_profile
262196 4 -rw------- 1 13602 testing 93 Jan 25 08:00 /home/jbaxter/.bash_history
262194 0 -rw-rw-r-- 1 13602 testing 0 Jan 25 07:59 /home/jbaxter/file.txt
...

7. Выполните приведенные далее команды, чтобы скопировать файл /etc/services в каталог /etc/skel/, затем добавьте в систему нового пользователя с именем mjones, полным именем Mary Jones и домашним каталогом /home/maryjones. Укажите ее домашний каталог, чтобы убедиться, что файл служб находится там:

# cp /etc/services /etc/skel/
# useradd -d /home/maryjones -c "Mary Jones" mjones
# ls -l /home/maryjones
total 628
-rw-r--r--. 1 mjones mjones 640999 Jan 25 06:27 services

8. Выполните следующую команду, чтобы найти в каталоге /home все файлы, принадлежащие mjones. Если вы выполняли упражнения по порядку, обратите внимание на то, что после удаления пользователя с самыми высокими