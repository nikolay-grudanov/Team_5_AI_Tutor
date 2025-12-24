---
source_image: page_599.png
page_number: 599
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.59
tokens: 7464
characters: 2132
timestamp: 2025-12-24T05:02:00.909313
finish_reason: stop
---

новый самостоятельно, чтобы можно было управлять командой или командами как службой. Помните, что файл rc.local — это быстрый и простой способ заставить команды запускаться при каждой загрузке системы.

Диагностика системы инициализации systemd

Последние версии систем Fedora, RHEL и Ubuntu используют systemd вместо System V init в качестве системы инициализации. И хотя systemd более сложна, чем System V init, она предлагает больше вариантов анализа того, что происходит во время инициализации.

Процесс загрузки systemd

Когда демон systemd (/usr/lib/systemd/systemd) запускается после запуска ядра, он приводит в движение все другие настроенные для запуска службы. В частности, отключает содержимое файла /etc/systemd/system/default.target, как в примере:

# cat /etc/systemd/system/default.target
...
[Unit]
Description=Graphical Interface
Documentation=man:systemd.special(7)
Requires=multi-user.target
Wants=display-manager.service
Conflicts=rescue.service rescue.target
After=multi-user.target rescue.service rescue.target display-manager.service
AllowIsolate=yes

Файл default.target на самом деле является символической ссылкой на файл в каталоге /lib/systemd/system. Для сервера он может быть связан с файлом multi-user.target, для рабочего стола — связан с файлом graphical.target (как показано в примере).

В отличие от инициализации System V init, которая просто запускает служебные скрипты в алфавитно-цифровом порядке, служба systemd должна работать в обратном направлении от файла default.target, чтобы определить, какие службы и целевые объекты запускаются. В примере default.target — это символическая ссылка на файл graphical.target. Перечисляя содержимое этого файла, вы можете увидеть следующее:

● требуется, чтобы файл multi-user.target был загружен первым;
● после него загружается служба display-manager.service.

Продолжив изучать, что требуется этим двум единицам, вы можете найти то, что нужно еще. Например, multi-user.target требует, чтобы basic.target (запускает различные базовые службы) и display-manager.service (запускает диспетчер отображения, gdm) запускали графический экран входа в систему.