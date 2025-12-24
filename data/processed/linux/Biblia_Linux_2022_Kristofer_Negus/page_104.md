---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.31
tokens: 7608
characters: 2147
timestamp: 2025-12-24T04:48:02.802403
finish_reason: stop
---

дополнительная информация, например имя файла, каталог, имя пользователя, устройство или другой элемент, который указывает команде, что делать. Например, команда cat /etc/passwd отображает содержимое файла /etc/passwd на экране. Часть /etc/passwd и есть аргумент. Обычно в командной строке можно использовать любое количество аргументов, ограниченное только общим количеством символов, разрешенных в командной строке. Иногда аргумент связан с параметром. В этом случае он должен стоять сразу за параметром. При однобуквенных параметрах аргумент обычно отделяется пробелом. Если параметр — это целое слово, то аргумент стоит за знаком равенства (=), например:

$ ls --hide=Desktop
Documents  Music  Public  Videos
Downloads  Pictures  Templates

Здесь параметр --hide указывает команде ls не отображать файл или каталог с именем Desktop при перечислении содержимого каталога. Обратите внимание на то, что знак равенства стоит сразу за параметром (без пробела), а затем указывается аргумент (опять же без пробела).

Вот пример однобуквенного параметра, за которым следует аргумент:

$ tar -cvf backup.tar /home/chris

Здесь параметры создают (с) файл (f) с именем backup.tar, который включает в себя все содержимое каталога home/chris и его подкаталогов и показывает подробные сообщения (v) при создании резервной копии. Поскольку текст backup.tar является аргументом для параметра f, аргумент backup.tar должен располагаться сразу за параметром.

Примените следующие команды. Посмотрите, как они ведут себя с различными параметрами:

$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates
Videos
$ ls -a
.
..
.bash_history
.bash_logout
.bash_profile
.bashrc
.Desktop
.Documents
.Downloads
.emacs
.esd_auth
.fsync.log
.gnome2_private
.gnote
.gnupg
.gstreamer-0.10
.gtk-bookmarks
.gvfs
.lesshst
.local
.mozilla
.Music
.Pictures
.Public
.Templates
.Videos
.xsession-errors
.zshrc
Pictures
$ uname
Linux
$ uname -a
Linux mydesktop 5.3.7-301.fc31.x86_64 #1 SMP Mon Oct 21 19:18:58 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
$ date
Wed 04 Mar 2020 09:06:25 PM EST
$ date +'%d/%m/%y'
04/03/20
$ date +'%A, %B %d, %Y'
Wednesday, March 04, 2020