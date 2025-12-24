---
source_image: page_261.png
page_number: 261
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.26
tokens: 7446
characters: 1632
timestamp: 2025-12-23T23:11:38.698568
finish_reason: stop
---

echo '-----------------------------------------------'
while read -r ipadd
do
    ipadd=$(echo "$ipadd" | sed 's/\r//')   ①
    ping -n 1 "$ipadd" | egrep '(Destination host unreachable|100%)' &> /dev/null   ②
    if (( "$?" == 0 ))   ③
        then
            tput setaf 1   ④
            echo "Host $ipadd not found - $(date)" | tee -a monitorlog.txt   ⑤
            tput setaf 7
        fi
    done < "$1"

echo ""
echo "Done."

for ((i="$2"; i > 0; i--))   ⑥
do
    tput cup 1 0   ⑦
    echo "Status: Next scan in $i seconds"
    sleep 1
done
done

① Удаление разрывов строк после чтения поля из файла в Windows.

② Однократная проверка связи с хостом. grep применяется для поиска в выводе команды ping фраз Destination host unreachable (Целевой хост недоступен) или 100 % — это означает, что хост не найден. Поскольку используется ping -n, этот сценарий настроен для выполнения в операционной системе Windows. Для выполнения сценария в Linux укажите ping -c.

③ Проверка, завершила ли команда grep работу с кодом состояния 0: это означает, что были обнаружены строки с ошибками и хост не ответил на запрос ping.

④ Установка красного цвета шрифта для важного текста.

⑤ Уведомление пользователя о том, что хост не найден, и добавление сообщения в файл monitorlog.txt.

⑥ Запуск обратного отсчета времени до начала следующего сканирования.

⑦ Перемещение курсора в строку 1, столбец 0.

Чтобы запустить pingmonitor.sh, предоставьте ему файл, содержащий список IP-адресов или имен хостов (по одному на строку) и время задержки между сканированиями в секундах:

$ ./pingmonitor.sh monitor.txt 60

Cybersecurity Ops System Monitor