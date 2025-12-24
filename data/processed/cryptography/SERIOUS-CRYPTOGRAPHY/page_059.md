---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.06
tokens: 7525
characters: 1381
timestamp: 2025-12-24T09:11:19.117700
finish_reason: stop
---

Листинг 2.3. Скрипт, показывающий, как изменяется оценка энтропии в /dev/random

#!/bin/sh
ESTIMATE=/proc/sys/kernel/random/entropy_avail
timeout 3s dd if=/dev/random bs=4k count=1 2> /dev/null | base64
ent=`cat $ESTIMATE`
while [ $ent -lt 128 ]
do
    sleep 3
    ent=`cat $ESTIMATE`
    echo $ent
done
dd if=/dev/random bs=8 count=1 2> /dev/null | base64
cat $ESTIMATE

В примере прогона в листинге 2.3 показан вывод скрипта в листинге 2.4. (Угадайте, когда я начал хаотично двигать мышью и стучать по клавиатуре для сбора энтропии.)

Листинг 2.4. Пример выполнения скрипта, демонстрирующего изменение оценки энтропии

xFNX/f2R87/zrrNJ6Ibr5R1L913tl+F4GNzKb60BC+qQnHQcyA==
2
18
19
27
28
72
124
193
jq8XWCt8
129

Как видно из листинга 2.4, согласно оценке /dev/random, в пуле осталось 193 – 64 = 129 бит энтропии. Имеет ли смысл считать, что в PRNG стало на N бит энтропии меньше, лишь потому что из PRNG только что было прочитано N бит? (Подсказка: нет.)

Примечание Как и /dev/random, системный вызов Linux getrandom() блокирует выполнение, если не набрано достаточно начальной энтропии. Но, в отличие от /dev/random, он не пытается оценить количество энтропии в системе и никогда не блокируется после стадии инициализации. И это хорошо. (Путем установки флагов можно заставить getrandom() использовать /dev/random и блокироваться, но я не вижу, зачем бы это могло понадобиться.)