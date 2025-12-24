---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.15
tokens: 7590
characters: 1900
timestamp: 2025-12-24T04:33:55.417735
finish_reason: stop
---

Листинг 3.12. Сценарии запуска служб и их каталогизация по уровням исполнения

finn@ubuntu:~$ ls -l /etc/rc?.d

/etc/rc2.d:
lrwxrwxrwx 1 root root 20 ноя 13 00:16 /etc/rc2.d/S19postgresql -> ../init.d/postgresql
lrwxrwxrwx 1 root root 17 ноя 13 00:16 /etc/rc2.d/S20postfix -> ../init.d/postfix

/etc/rc6.d:
lrwxrwxrwx 1 root root 17 ноя 13 00:16 /etc/rc6.d/K20postfix -> ../init.d/postfix
lrwxrwxrwx 1 root root 17 ноя 13 00:16 /etc/rc6.d/K21postgresql -> ../init.d/postgresql

В этом примере сценарии postfix и postgresql имеют вторичные имена, начинающиеся с K в каталоге rc6.d, и другие вторичные имена, начинающиеся с S в каталоге rc2.d. Это символизирует необходимость запускать (start) службы postfix и postgresql при переключении системы на уровень исполнения № 2 и уничтожать (kill) процессы этих служб при переключении системы на уровень исполнения № 6.

3.2.5. Специальные файлы устройств

Специальные файлы устройств предназначены для ввода данных с аппаратных устройств и вывода данных на них. Настоящую работу по вводу и выводу данных проделывает драйвер устройства, а специальные файлы (листинг 3.13) играют роль своеобразных «порталов» связи с драйверами. Различают символные ① и блочные ② специальные файлы устройств, у которых минимальной единицей обмена информацией с драйверами является блок (обычно размером 512 байт) или символ (1 байт), соответственно.

Листинг 3.13. Специальные файлы устройств

finn@ubuntu:~$ ls -l /dev/sd* /dev/input/mouse* /dev/video* /dev/snd/pcm*

① crw-rw---- 1 root input 13 ①, 32 ② ноя 17 03:31 /dev/input/mouse0
crw-rw---- 1 root input 13, 33 ноя 17 03:31 /dev/input/mouse1
brw-rw---- 1 root disk 8, 0 ноя 17 03:31 /dev/sda
brw-rw---- 1 root disk 8, 1 ноя 17 03:31 /dev/sda1
② brw-rw---- 1 root disk 8, 5 ноя 17 03:31 /dev/sda5
crw-rw----+ 1 root audio 116, 3 ноя 17 15:03 /dev/snd/pcmC0D0c

1 Подробнее о шаблонных символах ?, * и пр. см. разд. 5.3.