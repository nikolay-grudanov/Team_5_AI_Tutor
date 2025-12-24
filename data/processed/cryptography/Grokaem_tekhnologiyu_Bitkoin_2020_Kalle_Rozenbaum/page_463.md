---
source_image: page_463.png
page_number: 463
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.50
tokens: 7584
characters: 1862
timestamp: 2025-12-24T08:43:20.190747
finish_reason: stop
---

Веб-сервер обрабатывает HTTP-запрос, получает хеш блока из блокчейна и возвращает следующий HTTP-ответ:

{"result":"000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
"error":null,"id":"1"}

после чего bitcoin-cli выводит значение свойства result в окно терминала:

000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f

Это тело HTTP-запроса соответствует стандарту JSON-RPC, который описывает, как клиент может вызывать функции в удаленном процессе с использованием формата записи объектов JavaScript (JavaScript Object Notation, JSON).

Использование curl

Поскольку взаимодействие с процессом bitcoind происходит через HTTP, для связи с ним можно использовать любую программу, способную отправлять HTTP-запросы POST, например утилиту командной строки curl. Но при использовании инструментов, отличных от bitcoin-cli, вы должны настроить имя пользователя и пароль для аутентификации на веб-сервере.

Остановите узел командой ./bitcoin-cli stop. Откройте или создайте, если он отсутствует, файл конфигурации Bitcoin Core ~/.bitcoin/bitcoin.conf и добавьте в него следующие строки:

rpcuser=<имя пользователя по вашему выбору>
rpcpassword=<пароль по вашему выбору>

Изменив и сохранив файл ~/.bitcoin/bitcoin.conf, запустите узел командой ./bitcoind -daemon, чтобы активировать изменения.

Вот как я вызвал getblockhash с помощью curl (символ обратного слеша \ означает перенос команды на следующую строку):

curl --user kalle --data-binary \
    '{"method":"getblockhash","params":[0],"id":1}' \
    -H 'content-type: text/plain;' http://127.0.0.1:8332/
Enter host password for user 'kalle':
{"result":"000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
"error":null,"id":1}

БОЛЬШЕ ПАРАМЕТРОВ
Bitcoin Core поддерживает большое количество параметров. Выполните команду ./bitcoind --help, чтобы получить полный список.