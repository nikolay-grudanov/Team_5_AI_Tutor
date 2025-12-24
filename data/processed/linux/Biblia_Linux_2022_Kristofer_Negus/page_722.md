---
source_image: page_722.png
page_number: 722
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.22
tokens: 7513
characters: 2034
timestamp: 2025-12-24T05:05:41.733476
finish_reason: stop
---

pid=1067
    comm="httpd" path="/var/myserver/services" dev="dm-0" ino=655836
    scontext=system_u:system_r:httpd_t:s0
    tcontext=unconfined_u:object_r:var_t:s0 tclass=file permissive=0

В примере отображается информация о том, кто пытался получить доступ, а также их контекст безопасности при попытке доступа. Ищите в сообщении об отказе AVC следующие ключевые слова:

● type=AVC;
● avc: denied;
● com="httpd";
● path="/var/myserver/services".

Вывод команды дает достаточно данных, чтобы либо начать устранять проблему, либо отследить вредоносную активность. В примере каталог /var/myserver/services имеет неправильный контекст файла SELinux для чтения службой httpd.

Просмотр сообщений SELinux в журнале сообщений

Если у вас запущена служба auditd, вы можете найти сообщения об отказе AVC, выполнив поиск в файле /var/log/audit/audit.log с помощью команды grep. Для последних систем RHEL и Fedora или любой системы Linux, использующей службу systemd, можете запустить команду journalctl, чтобы проверить наличие сообщений журнала отказа AVC. Внутри каждого сообщения журнала находится сообщение AVC, позволяющее изучить информацию об этом отказе AVC, как в следующем примере:

# journalctl | grep AVC
type=AVC msg=audit(1580397837.346:275): avc: denied { getattr }for pid=1067
    comm="httpd" path="/var/myserver/services" dev="dm-0" ino=655836
    scontext=system_u:system_r:httpd_t:s0
    tcontext=unconfined_u:object_r:var_t:s0 tclass=file permissive=0

Поскольку вы знаете, что отказы AVC есть, можете передать весь файл /var/log/audit/audit.log в команду sealert, чтобы решить следующие проблемы:

# sealert -a /var/log/audit/audit.log
SELinux is preventing httpd from getattr access on the file /var/myserver/services.

***** Plugin catchall (100. confidence) suggests ***************

If you believe that httpd should be allowed getattr access on the services file by default.
Then you should report this as a bug.
You can generate a local policy module to allow this access.
Do
allow this access for now by executing: