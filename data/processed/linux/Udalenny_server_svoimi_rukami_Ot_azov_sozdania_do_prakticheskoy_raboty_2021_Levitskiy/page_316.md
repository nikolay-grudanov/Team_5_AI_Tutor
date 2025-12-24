---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.24
tokens: 6098
characters: 393
timestamp: 2025-12-24T04:02:51.422110
finish_reason: stop
---

Рис. 18.4. Редактирование php.ini

После этого заставьте сервер перечитать файл конфигурации или попросту перезагрузите его.

Примечание. Для директивы max_execution_time значение указывается в секундах. Например, 3600 — это 1 час. Значение 0 отключает проверку времени выполнения и сценарии могут выполняться вечно.

Создайте сценарий info.php в корне вашего веб-сервера:

<?php
phpinfo();
?>