---
source_image: page_881.png
page_number: 881
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.92
tokens: 7741
characters: 2064
timestamp: 2025-12-24T05:10:04.532187
finish_reason: stop
---

ID пользователя и группы его номера были присвоены пользователю mjones. В результате все файлы, оставленные в системе jbaxter, теперь принадлежат mjones (по этой причине вы должны удалить или изменить владельца файлов, оставшихся после удаления пользователя):

# find /home -user mjones -ls
262184 4 drwx------ 4 mjones mjones 4096 Jan 25 08:00 /home/jbaxter
262193 4 -rw-r--r-- 1 mjones mjones 176 Jan 27 2011 /home/jbaxter/.bash_profile
262189 4 -rw-r--r-- 1 mjones mjones 18 Jan 27 2011 /home/jbaxter/.bash_logout
262194 0 -rw-rw-r-- 1 mjones testing 0 Jan 25 07:59 /home/jbaxter/file.txt
262188 4 -rw-r--r-- 1 mjones mjones 124 Jan 27 2011 /home/jbaxter/.bashrc
262197 4 drwx------ 4 mjones mjones 4096 Jan 25 08:27 /home/maryjones
262207 4 -rw-r--r-- 1 mjones mjones 176 Jan 27 2011 /home/maryjones/.bash_profile
262202 4 -rw-r--r-- 1 mjones mjones 18 Jan 27 2011 /home/maryjones/.bash_logout
262206 628 -rw-r--r-- 1 mjones mjones 640999 Jan 25 08:27 /home/maryjones/services
262201 4 -rw-r--r-- 1 mjones mjones 124 Jan 27 2011 /home/maryjones/.bashrc

9. От имени пользователя mjones вы можете применить код, приведенный далее, чтобы создать файл с именем /tmp/mary-file.txt и с помощью ACL назначить этому файлу права пользователя bin на чтение/запись и права группы lp на чтение/запись:

[mjones]$ touch /tmp/maryfile.txt
[mjones]$ setfacl -m u:bin:rw /tmp/maryfile.txt
[mjones]$ setfacl -m g:lp:rw /tmp/maryfile.txt
[mjones]$ getfacl /tmp/maryfile.txt
# file: tmp/maryfile.txt
# owner: mjones
# group: mjones
user::rw-
user:bin:rw-
group::rw-
group:lp:rw-
mask::rw-
other::r& –

10. Выполните от имени пользователя mjones набор команд, чтобы создать каталог с именем /tmp/mydir и применить ACL для назначения ему прав по умолчанию, чтобы пользователь adm имел права на чтение/запись/выполнение этого каталога и любых файлов или каталогов, созданных в нем. Проверьте, сработал ли набор команд, создав каталог /tmp/mydir/testing/ и файл /tmp/mydir/newfile.txt:

[mary]$ mkdir /tmp/mydir
[mary]$ setfacl -m d:u:adm:rwx /tmp/mydir
[mjones]$ getfacl /tmp/mydir