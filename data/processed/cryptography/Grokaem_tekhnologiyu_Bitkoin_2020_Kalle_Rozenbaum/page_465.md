---
source_image: page_465.png
page_number: 465
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.68
tokens: 7321
characters: 1386
timestamp: 2025-12-24T08:43:10.439149
finish_reason: stop
---

модействовать с bitcoin-qt с помощью bitcoin-cli, запустите bitcoin-qt следующей командой:

$ ./bitcoin-qt -server &

Знакомство с bitcoin-cli

Итак, предположим, что вы уже запустили Bitcoin Core в фоновом режиме как

$ ./bitcoind -daemon

Первая важная команда, которую нужно запомнить, — это команда help. Если выполнить ее без аргументов, она вернет список всех доступных команд:

$ ./bitcoin-cli help

Вы получите длинный список команд, сгруппированных по темам — например, Blockchain, Mining и Wallet. Назначение некоторых команд очевидно из их имен, но если вы захотите узнать больше о конкретной команде, вызовите команду help и передайте ей аргумент с именем интересующей команды. Например:

$ ./bitcoin-cli help getblockhash
getblockhash height

Returns hash of block in best-block-chain at height provided.

Arguments:
1. height (numeric, required) The height index

Result:
"hash" (string) The block hash

Examples:
> bitcoin-cli getblockhash 1000
> curl --user myusername --data-binary '{"jsonrpc": [CA]"1.0", "id":"curltest", "method": "getblockhash", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

Вызвать bitcoin-cli можно двумя способами:

★ С помощью позиционных аргументов. Смысл аргументов зависит от их относительного местоположения, например ./bitcoin-cli getblockhash 1000. Это самый распространенный вариант использования bitcoin-cli.