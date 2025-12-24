---
source_image: page_723.png
page_number: 723
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.55
tokens: 7639
characters: 2371
timestamp: 2025-12-24T05:05:50.113254
finish_reason: stop
---

# ausearch -c 'httpd' --raw | audit2allow -M my-httpd
# semodule -X 300 -i my-httpd.pp

Additional Information:
Source Context system_u:    system_r:httpd_t:s0
Target Context unconfined_u: object_r:var_t:s0
Target Objects                /var/myserver/services [ file ]
...
Raw Audit Messages
type=AVC msg=audit(1580397837.346:275): avc: denied { getattr } for pid=1067 comm="httpd" path="/var/myserver/services" dev="dm-0" ino=655836 scontext=system_u:system_r:httpd_t:s0 tcontext=unconfined_u:object_r:var_t:s0 tclass=file permissive=0 Hash: httpd,httpd_t,var_t,file,getattr

В этом случае, если вы хотите разрешить службе httpd доступ к содержимому запрещаемого каталога, можете запустить команды ausearch и semodule, как в примере. Это создает и применяет новую политику SELinux, которая разрешает доступ к содержимому. При условии, что нет никаких других проблем с разрешениями, httpd должен получить доступ к этому контенту.

Диагностика журналов SELinux

Очевидно, что файлы журналов чрезвычайно важны для диагностики и устранения нарушений политики SELinux. Ведение файлов журнала или прямого запроса журнала systemd (команда journalctl) — это первые шаги по устранению неполадок SELinux. Таким образом, важно убедиться, что ваша система Linux регистрирует сообщения в первую очередь.
Быстрый способ определить, ведется ли журнал, — проверить, работают ли соответствующие демоны: auditd, rsyslogd и/или setroubleshootd. Используйте соответствующую команду, например systemctl status auditd.service. Конечно, применяемая команда зависит от вашего дистрибутива Linux и его версии. Более подробную информацию см. в главе 15. Если демон не запущен, запустите его, чтобы начать ведение журнала.

ВНИМАНИЕ!
Иногда отказы AVC не регистрируются из-за правил политики dontaudit. Хотя правила dontaudit помогают уменьшить количество ложных срабатываний в журналах, они могут вызвать проблемы при устранении неполадок. Чтобы исправить ситуацию, временно отключите все правила политики dontaudit с помощью команды semodule -DB.

Устранение распространенных проблем SELinux

В начале работы с SELinux легко упустить из виду очевидное. Всякий раз, когда доступ оказывается запрещен, вы должны сначала проверить традиционные разрешения Linux DAC. Например, используйте команду ls -l и дважды проверьте правильность назначений владельца файла, группы, чтения, записи и выполнения.