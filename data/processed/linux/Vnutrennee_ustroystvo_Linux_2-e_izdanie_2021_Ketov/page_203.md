---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.42
tokens: 7537
characters: 1713
timestamp: 2025-12-24T04:37:46.204430
finish_reason: stop
---

с символов, не являющихся ни буквой, ни цифрой. Таким образом, ни одна команда самостоятельно не вычисляет подстановки имен файлов, а пользуется результатами вычислений так, как будто они были заданы непосредственно в качестве ее аргументов.

Листинг 5.15. Просмотр файлов man-страниц по критерию имени

bender@ubuntu:~$ cd /usr/share/man/man1
bender@ubuntu:/usr/share/man/man1$ ls y*
ybmtopm.1.gz yes.1.gz ypdomainname.1.gz yuvtoppm.1.gz
yelp.1.gz youtube-dl.1.gz yuvsplittoppm.1.gz
bender@ubuntu:/usr/share/man/man1$ ls ???.*
'[.1.gz' dsa.1ssl.gz ico.1.gz rcp.1.gz tee.1.gz
apg.1.gz dwp.1.gz lcf.1.gz red.1.gz tgz.1.gz
dir.1.gz gtf.1.gz pwd.1.gz tbl.1.gz zip.1.gz
bender@ubuntu:/usr/share/man/man1$ set -x ①
bender@ubuntu:/usr/share/man/man1$ ls -l [0-9]*
+ ls --color=auto ① -l 2to3-2.7.1.gz 411toppm.1.gz ①
-rw-r--r-- 1 root root 563 окт 10 13:26 2to3-2.7.1.gz
-rw-r--r-- 1 root root 592 апр 23 2016 411toppm.1.gz
bender@ubuntu:/usr/share/man/man1$ ls [!a-z0-9]*
+ ls --color=auto '[.1.gz' CA.pl.1ssl.gz GET.1p.gz HEAD.1p.gz ImageMagick-im6.q16.1.gz POST.1p.gz Xephyr.1.gz Xmark.1.gz Xorg.1.gz Xorg.wrap.1.gz Xserver.1.gz ②
'[.1.gz' HEAD.1p.gz Xephyr.1.gz Xorg.wrap.1.gz
CA.pl.1ssl.gz ImageMagick-im6.q16.1.gz Xmark.1.gz Xserver.1.gz
GET.1p.gz POST.1p.gz Xorg.1.gz

В режиме трассировки командного интерпретатора видна еще и подстановка псевдонимов ①, которая заменяет «псевдоним» команды пользователя, например ls (листинг 5.16), ее «настоящим значением».

Листинг 5.16. Псевдонимы командного интерпретатора

bender@ubuntu:~$ alias
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'