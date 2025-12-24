---
source_image: page_474.png
page_number: 474
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.51
tokens: 7795
characters: 1724
timestamp: 2025-12-24T08:43:45.590313
finish_reason: stop
---

Кошелек закрыт. Снова выведем информацию о транзакции:

$ ./bitcoin-cli listtransactions
[
    {
        "address": "bc1q2r9mql4mkz3z7yfxvef76yxjd637r429620j75",
        "category": "receive",
        "amount": 0.00500000,
        "label": "",
        "vout": 1,
        "confirmations": 1,
        "blockhash": "000000000000000000000000240eec03ac7499805b0f3df34a7d5005670f3a8fa836ca",
        "blockindex": 311,
        "blocktime": 1541946325,
        "txid": "ebfd0d14c2ea74ce408d01d5ea79636b8dee88fe06625f5d4842d2a0ba45c195",
        "walletconflicts": [
        ],
        "time": 1541941483,
        "timereceived": 1541941483,
        "bip125-replaceable": "no"
    },
    {
        "address": "bc1qu456w7a5mawlg35y00xu03wp8wc7d65t7uulqm",
        "category": "send",
        "amount": -0.00100000,
        "vout": 1,
        "fee": -0.00000141,
        "confirmations": 0,
        "trusted": true,
        "txid": "a13bcb16d8f41851cab8e939c017f1e05cc3e2a3c7735bf72f3dc5ef4a5893a2",
        "walletconflicts": [
        ],
        "time": 1541946631,
        "timereceived": 1541946631,
        "bip125-replaceable": "no",
        "abandoned": false
    }
]

Новая транзакция — последняя из двух. Она пока не подтверждена, о чем говорит атрибут "confirmations": 0. Размер комиссии составил 141 сатоши. Рассмотрим эту транзакцию подробнее:

$ ./bitcoin-cli getrawtransaction \
    a13bcb16d8f41851cab8e939c017f1e05cc3e2a3c7735bf72f3dc5ef4a5893a2 1
{
    "txid": "a13bcb16d8f41851cab8e939c017f1e05cc3e2a3c7735bf72f3dc5ef4a5893a2",
    "hash": "554a3a3e57dcd07185414d981af5fd272515d7f2159cf9ed9808d52b7d852ead",
    "version": 2,
    "size": 222,
    "vsize": 141,
    "weight": 561,
    "locktime": 549665,
    "vin": [