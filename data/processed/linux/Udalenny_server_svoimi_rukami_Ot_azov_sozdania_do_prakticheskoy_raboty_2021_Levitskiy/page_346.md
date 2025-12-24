---
source_image: page_346.png
page_number: 346
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.56
tokens: 6230
characters: 820
timestamp: 2025-12-24T04:03:28.977799
finish_reason: stop
---

<?php
include «config.php»;    // здесь параметры доступа к БД

$mysqli = new mysqli($DBHOST, $DBUSER, $DBPASSWD, $DBNAME);

if ($mysqli->connect_errno) {
    echo "0";
}
else «1»;                // connect ok
?>

Затем создается bash-сценарий подобный этому:

#!/bin/bash
RESULT=$(/usr/bin/php test-mysql.php)
if [ $RESULT -eq 0 ]; then
echo "Restarting MySQL"
/etc/init.d/mysqld restart
fi

Как и в случае с первым нашим bash-сценарием, вызов этого сценария нужно поместить в расписание планировщика. Можно объединить эти два bash-сценария в один и вызывать все сразу.

20.2.3. Если падают процессы

Если процессы не виснут, а «падают», то есть после сбоя вообще нет процессов Apache/MySQL в таблице процессов, тогда поможет следующий сценарий:

#!/bin/bash
RESTART="/etc/init.d/apache2 restart"
PGREP="/usr/bin/pgrep"