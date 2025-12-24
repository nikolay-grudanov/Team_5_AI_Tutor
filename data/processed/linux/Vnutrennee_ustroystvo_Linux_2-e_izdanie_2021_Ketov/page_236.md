---
source_image: page_236.png
page_number: 236
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.33
tokens: 7289
characters: 1309
timestamp: 2025-12-24T04:38:30.405872
finish_reason: stop
---

236

[ -z "$1" ] && usage

ldpath=$(grep -h '^[^#]' /etc/ld.so.conf.d/*.conf)

case $1 in
|① /*/lib*.so.[0-9]) what=$1;;
|② *) what=$(find $ldpath -name "lib$1.so.[0-9]" 2>/dev/null);;
    esac

if [ -z "$what" ]
then
    echo "Library $1 is not found in $LD_LIBRARY_PATH"
    usage
fi

where=$(printenv PATH | tr ':' ' ')

for lib in $what
do
    find $where -type f |
    |① xargs file -L |
    |② grep ':.*ELF' |
    |③ cut -f 1 -d : |
    |④ while read exe
        do
            ldd $exe | grep -q $lib && echo $exe
        done
    done
done

Целевая работа сценария выполняется одним конвейером ⑦, в котором при помощи find(1) ищутся ① регулярные файлы (-type f) в каталогах $where, список имен которых при помощи xargs(1) передается ① для классификации file(1). Построенный классификатор имя: класс фильтруется ② при помощи grep(1), из которого затем отделяются имена ③ посредством cut(1). Последняя команда конвейера — составной список while циклично перебирает ④ имена файлов, считывая их встроенной командой read в переменную exe, где на каждой итерации цикла проверяется зависимость исполняемого файла $exe от заданной библиотеки. Зависимость устанавливается ⑤ по факту успешного завершения grep(1), определяющего только наличие (-q) в выводе ldd(1) строки с именем путевого файла библиотеки $lib.