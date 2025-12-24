---
source_image: page_431.png
page_number: 431
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.27
tokens: 7490
characters: 2146
timestamp: 2025-12-24T04:57:31.888694
finish_reason: stop
---

Вы можете просмотреть список различных юнитов, которые относятся к целевому юниту Requires (их необходимо активизировать, иначе юнит выйдет из строя), используя команду, приведенную в следующем примере. Обратите внимание на то, что вывод Requires намного короче, чем вывод Wants для юнита multi-user.target, поэтому никакого дополнительного форматирования выходных данных не требуется:

# systemctl show --property "Requires" multi-user.target
Requires=basic.target

Целевые юниты, как и сервисные, также имеют файлы конфигурации. В следующем примере показано содержимое файла конфигурации multi-user.target:

# cat /lib/systemd/system/multi-user.target
# This file is part of systemd.
#
...

[Unit]
Description=Multi-User
Documentation=man:systemd.special(7)
Requires=basic.target
Conflicts=rescue.service rescue.target
After=basic.target rescue.service rescue.target
AllowIsolate=yes

Этот базовый файл конфигурации целевого юнита имеет следующие параметры.

● Description — описание службы в свободной форме.
● Documentation — перечисляет соответствующие справочные страницы systemd.
● Requires — если файл multi-user.target активизируется, то вместе с ним активизируется и указанный целевой юнит. Если целевой юнит деактивизирован или выходит из строя, то и multi-user.target перестает функционировать. Если нет параметров After и Before, то одновременно активизируются как файл multi-user.target, так и указанный целевой юнит.
● Conflicts — позволяет избежать конфликтов во время работы служб. Запуск multi-user.target останавливает все перечисленные в нем целевые и сервисные юниты и наоборот.
● After — устанавливает порядок. Другими словами, параметр перечисляет, какие устройства должны быть активизированы до запуска определенной службы.
● AllowIsolate — представлен логическим значением yes или no. Если этот параметр установлен со значением yes, то целевой юнит multi-user.target активизируется вместе со своими зависимостями, а все остальные отключаются.

Чтобы получить более подробную информацию об этих файлах конфигурации и их параметрах, введите команды man sys emd.service, systemd.target и man systemd.unit в командной строке.