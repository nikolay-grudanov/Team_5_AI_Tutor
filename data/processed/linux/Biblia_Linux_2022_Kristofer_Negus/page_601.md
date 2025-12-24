---
source_image: page_601.png
page_number: 601
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.89
tokens: 7642
characters: 2237
timestamp: 2025-12-24T05:02:16.138176
finish_reason: stop
---

Из вывода systemctl можно понять, произошел ли сбой какого-либо единичного файла. В примере видно, что запустить httpd.service (ваш веб-сервер) не удалось. Продолжая исследование, используйте команду journalctl -u для этой службы, чтобы увидеть, были ли добавлены какие-то сообщения об ошибках:

# journalctl -u httpd.service
...
Dec 08 09:30:36 rhel81-bible systemd[1]: Starting The Apache HTTP Server...
Dec 08 09:30:36 rhel81-bible httpd[16208]: httpd: Syntax error on line 105 of /etc/httpd/conf/httpd.conf:
    /etc/httpd/conf/httpd.conf:105: <Directory> was not closed.
Dec 08 09:30:36 rhel81-bible systemd[1]: httpd.service: Main process exited, code=exited, status=1/FAILURE
Dec 08 09:30:36 rhel81-bible systemd[1]: httpd.service: Failed with result 'exit-code'.
Dec 08 09:30:36 rhel81-bible systemd[1]:
    Failed to start The Apache HTTP Server.

Из выходных данных видно, что в файле httpd.conf обнаружилось несоответствие директив (не удалось закрыть раздел каталога). После того как ошибка была исправлена, я смог запустить службу (systemctl start httpd). Если другие unit-файлы отображаются как невыполненные, можно снова запустить команду journalctl -u, используя эти имена unit-файлов в качестве аргументов.

Анализ процесса загрузки systemd

Чтобы точно увидеть, что произошло в ходе загрузки системы, использующей службу systemd, система systemd применяет инструмент systemd-analyze. Чтобы узнать, остановились ли службы, или чтобы найти место для собственной службы systemd, задействуйте эту команду для анализа всего процесса загрузки. Вот несколько примеров:

# systemd-analyze time
Startup finished in 1.775s (kernel) + 21.860s (initrd)
    + 1min 42.414s (userspace) = 2min 6.051s
graphical.target reached after 1min 42.121s in userspace

Параметр time позволяет увидеть, сколько времени заняла каждая фаза процесса загрузки, от старта ядра до конца загрузки целевого объекта по умолчанию. Вы можете использовать команду plot для создания SVG-графики каждого компонента процесса запуска (в примере применяется команда eog для отображения выходных данных):

# systemd-analyze plot > /tmp/systemd-plot.svg
# eog /tmp/systemd-plot.svg

На рис. 21.3 показан небольшой фрагмент вывода из гораздо более крупного графика.