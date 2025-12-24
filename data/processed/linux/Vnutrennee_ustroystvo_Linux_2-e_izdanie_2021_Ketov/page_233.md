---
source_image: page_233.png
page_number: 233
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.97
tokens: 7210
characters: 1045
timestamp: 2025-12-24T04:38:26.828808
finish_reason: stop
---

файла, определяется и выполняется в соответствующей ветви команда распаковки tar(1), gunzip(1), bunzip2(1), rar(1), unzip(1), uncompress(1) или 7z(1). При запуске функции в режиме трассировки видно, как работает передача аргументов в функцию, как выполняются списки ветвлений и множественного ветвлений.

Листинг 5.52. Универсальный экстрактор архивов

bender@ubuntu:~$ extract ()

1 > if [ -f $1 ]
> then
2 > case $1 in
>   *.tar)           tar xf $1;;
>   *.tar.bz2|*.tbz2) tar xjf $1;;
>   *.tar.gz|*.tgz)   tar xzf $1;;
>   *.gz)            gunzip $1;;
>   *.bz2)           bunzip2 $1;;
>   *.rar)           rar x $1;;
>   *.zip)           unzip $1;;
>   *.Z)             uncompress $1;;
>   *.7z|*.iso)      7z x $1;;
>   *) echo "Неизвестен распаковщик для '$1'"; return 1;;
> esac
> else
>   echo "'$1' не является файлом"; return 1
> fi

bender@ubuntu:~$ type -a extract
extract является функцией
extract ()
{
}
bender@ubuntu:~$ set -x
bender@ubuntu:~$ extract dvd.iso
+ extract dvd.iso
- + '[' -f dvd.iso ']'
+ case $1 in
+ 7z x dvd.iso