---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.99
tokens: 7434
characters: 1627
timestamp: 2025-12-24T04:50:49.630046
finish_reason: stop
---

echo $* >> $PHONELIST
echo $* added to database
exit 0
fi

# Nope. But does the file have anything in it yet?
# This might be our first time using it, after all.
if [ ! -s $PHONELIST ] ; then
    echo "No names in the phone list yet! "
    exit 1
else
    grep -i -q "$*" $PHONELIST      # Quietly search the file
    if [ $? -ne 0 ] ; then           # Did we find anything?
        echo "Sorry, that name was not found in the phone list"
        exit 1
    else
        grep -i "$*" $PHONELIST
    fi
fi
exit 0

Итак, если вы создали файл ph со списком телефонов в своем текущем каталоге, введите приведенные ниже данные, чтобы проверить его работу:

$ chmod 755 ph
$ ./ph new "Mary Jones" 608-555-1212
Mary Jones 608-555-1212 added to database
$ ./ph Mary
Mary Jones 608-555-1212

Благодаря команде chmod скрипт ph становится исполняемым. Команда ./ph запускает команду ph из текущего каталога с параметром new. Таким образом имя Mary Jones и номер 608-555-1212 добавляются в базу данных ($HOME/.phonelist.txt). Далее команда ph ищет в базе данных имя Mary и отображает записанный для него телефон. Если скрипт работает, добавьте его в каталог в своем пути (например, $HOME/bin).

Скрипт резервного копирования

Поскольку ничто неечно и ошибки случаются у всех, резервные копии — это необходимость в ходе работы с компьютерными данными. Следующий простой скрипт создает резервные копии всех данных в домашних каталогах всех пользователей систем Fedora или RHEL:

#!/bin/bash
# (@)/my_backup
# A very simple backup script

# Change the TAPE device to match your system.
# Check /var/log/messages to determine your tape device.