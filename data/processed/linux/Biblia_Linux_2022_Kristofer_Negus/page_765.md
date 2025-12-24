---
source_image: page_765.png
page_number: 765
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.50
tokens: 7615
characters: 2034
timestamp: 2025-12-24T05:06:47.226954
finish_reason: stop
---

# firewall-cmd --zone=public \
    --add-port=21100-21110/tcp
# firewall-cmd --zone=public \
    --permanent --add-port=21100-21110/tcp
# firewall-cmd reload

Теперь можно применить любой FTP-клиент для доступа к FTP-службе через анонимного пользователя. Для дальнейшей настройки службы vsftpd и проверки ее работоспособности обратитесь к главе 18 «Настройка FTP-сервера».

Запуск и остановка контейнеров

Если вы специально не настраивали контейнер для удаления при его остановке (параметр --rm), то если контейнер остановлен, приостановлен или просто выходит из строя, он все еще будет находиться в вашей системе. Вы можете увидеть состояние всех контейнеров в системе (запущенных в данный момент или нет) с помощью параметра ps:

# podman ps
CONTAINER ID   IMAGE           COMMAND                  CREATED         NAMES
4d6be3e63fe3   localhost/vsftpd:latest   /usr/local/s2... About an hour ago
    Up About an hour ago  0.0.0.0:20-21->20-21/tcp  vsftpd
# podman ps -a
CONTAINER ID   IMAGE           COMMAND                  CREATED         NAMES
7da88bd62667   ubi8/ubi:latest   bash                     2 minutes       ago
    Exited 7 seconds ago silly_wozniak
4d6be3e63fe3   localhost/vsftpd:latest   /usr/local/s2i/ru... About an hour ago
    Up About an hour ago  0.0.0.0:20-21->20-21/tcp  vsftpd

Только запущенные контейнеры отображаются с помощью podman ps. Добавив параметр -a, вы можете увидеть все контейнеры, включая те, которые больше не работают, но еще не удалены. Вы можете перезапустить существующий неработающий контейнер, используя параметр start.

# podman start -a 7da88bd62667
[root@7da88bd62667 /]#

Перезапущенный контейнер запускает оболочку bash. Поскольку сеанс терминала контейнера уже существовал, не было необходимости начинать новый (-it). Нужно было прикрепить его (-a) к существующему сеансу. Контейнер, который только что работал в отключенном режиме, можно просто запустить и остановить по мере необходимости:

# podman stop 4d6be3e63fe3
4d6be3e63fe3...
# podman start 4d6be3e63fe3
4d6be3e63fe3