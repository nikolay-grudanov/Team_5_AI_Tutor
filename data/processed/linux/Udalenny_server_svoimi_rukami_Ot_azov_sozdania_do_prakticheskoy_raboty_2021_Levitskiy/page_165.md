---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.43
tokens: 6268
characters: 1144
timestamp: 2025-12-24T03:59:40.145717
finish_reason: stop
---

# ------------------------------------------------------
# Можно ли перезаписывать существующие файлы или нет
AllowOverwrite off
# Можно ли клиентам продолжать загрузку (on) или нет (off)
# Для удобства пользователей рекомендую включить этот
# параметр
AllowRetrieveRestart on
# Для более безопасной загрузки включите (on) этот параметр
HiddenStores on
# Включает автоматическое удаление частично загруженных
# файлов
DeleteAbortedStores on
#AllowStoreRestart off

# ------------------------------------------------------
# Параметры протоколирования. Смело все оставляйте как есть
# ------------------------------------------------------

WtmpLog off
TransferLog /var/log/proftpd/xferlog

# Записываем все попытки входа
ExtendedLog /var/log/proftpd/auth.log AUTH auth

# Протоколирование доступа к файлам/каталогам
ExtendedLog /var/log/proftpd/access.log WRITE,READ write

# Параноидальный уровень протоколирования....
ExtendedLog /var/log/proftpd/paranoid.log ALL default

# SQLLogFile
#SQLLogFile /var/log/proftpd/SQL.log
</Global>

### Конец глобальных параметров ###

# Запрещаем использование CHMOD
<Limit SITE_CHMOD>
    DenyAll
</Limit>