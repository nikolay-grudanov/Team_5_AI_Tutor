---
source_image: page_239.png
page_number: 239
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.99
tokens: 7192
characters: 1034
timestamp: 2025-12-24T04:38:26.932533
finish_reason: stop
---

Рис. 5.5. Фильтр строк grep(1)

В примерах из листингов 5.55 и 5.56 fgrep(1) и grep(1) используются для фильтрации строк, содержащих (-F) фиксированные слова, что быстрее, чем обработка полных регулярных выражений.

Листинг 5.55. Выборка строк: список сценариев интерпретатора

bender@ubuntu:~ $ file -Li /*bin/* /usr/*bin/* | fgrep shellscript
/bin/bzcmp:           text/x-shellscript; charset=us-ascii
/bin/setupcon:        text/x-shellscript; charset=utf-8
/sbin/dkms:           text/x-shellscript; charset=us-ascii

Листинг 5.56. Выборка строк: RSS память процессов браузера chromium

bender@ubuntu:~$ ps axo rss,comm | grep -F chrome
137812 chrome
45872 chrome
13068 chrome
104368 chrome
72052 chrome
97244 chrome
50984 chrome
19936 chrome

В примере из листинга 5.57 отфильтровываются строки конфигурационного файла команды wget(1), закомментированные символом # в их начале. Для этого выбираются строки, соответствующие регулярному выражению ^[^#], которое требует в начале строки ^ наличия символа, не ^ входящего в набор [#].