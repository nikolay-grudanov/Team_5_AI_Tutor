---
source_image: page_873.png
page_number: 873
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.74
tokens: 7403
characters: 1541
timestamp: 2025-12-24T05:09:41.051492
finish_reason: stop
---

б) скрипт может содержать следующее:

#!/bin/bash
# myos
read -p "Ваша любимая операционная система — macOS, Windows или Linux? " opsys
if [ $opsys = macOS ] ; then
    echo "macOS — хороший выбор, но он недостаточно хорош для меня."
elif [ $opsys = Windows ] ; then
    echo "Как-то я использовал Windows. Для чего этот синий экран?"
elif [ $opsys = Linux ] ; then
    echo "Отличный выбор!"
else
    echo "Разве $opsys — это операционная система?"
fi

5. Чтобы создать скрипт с именем $HOME/bin/animals, который проходит через слова «мышь», «корова», «гусь» и «свинья» и через цикл for и добавляет каждое из них в конец строки «У меня есть...», выполните следующие действия:
а) сделайте скрипт исполняемым:

$ touch $HOME/bin/animals
$ chmod 755 $HOME/bin/animals

б) скрипт может содержать следующее:

#!/bin/bash
# animals
for ANIMALS in moose cow goose sow ; do
    echo "У меня есть $ANIMALS"
done

в) при запуске скрипта выходные данные должны выглядеть так:

$ animals
У меня есть мышь
У меня есть корова
У меня есть гусь
У меня есть свинья

Глава 8. Системное администрирование

1. Чтобы запустить интерфейс Cockpit в своей системе, введите следующее:

# systemctl enable --now cockpit.socket
Created symlink /etc/systemd/system/sockets.target.wants/cockpit.socket → /usr/lib/systemd/system/cockpit.socket

2. Чтобы открыть интерфейс Cockpit в браузере, введите имя хоста или IP-адрес системы, поддерживающей службу, а затем номер порта 9090. Например, наберите в адресной строке браузера следующее:

https://host1.example.com:9090/