---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.88
tokens: 6251
characters: 904
timestamp: 2025-12-24T03:59:58.007825
finish_reason: stop
---

# Максимальная скорость передачи данных (в байтах/сек.)
# 0 - без ограничения
local_max_rate=7200

# Разрешена ли запись в каталог?
write_enable=NO

# Выводить ли сообщения при смене директории?
dirmessage_enable=YES

# Строка, которая будет показана при входе пользователя
ftpd_banner="Welcome to FTP service."

# Включить регистрацию событий?
xferlog_enable=YES

# Протоколировать все активные FTP-соединения?
log_ftp_protocol=NO

# Разрешать ли соединения только на порт 20 (ftp data)?
connect_from_port_20=YES

# Таймаут сессии
idle_session_timeout=600

# Таймаут передачи данных
data_connection_timeout=120

# Предоставлять вход через PAM
pam_service_name=vsftpd

# Для автономной работы (как standalone в proftpd) для следующего
# параметра нужно установить значение YES
listen=YES

После того, как вы отредактируете файл конфигурации, сохраните его и запустите сервер:

sudo systemctl start vsftpd