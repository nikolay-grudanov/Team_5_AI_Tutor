---
source_image: page_470.png
page_number: 470
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.96
tokens: 7676
characters: 1633
timestamp: 2025-12-24T08:43:31.053110
finish_reason: stop
---

Лично я выполнил перевод на свой новый адрес и затем проверил кошелек:

$ ./bitcoin-cli getunconfirmedbalance
0.00500000

Как показывает этот пример, появился входящий платеж в размере 5 мВТС (0,005 ВТС), ожидающий подтверждения. Теперь нужно подождать, пока платеж не будет включен в блокчейн, а пока углубимся в транзакцию, выполнив команду listtransactions. Вот что вывела эта команда у меня:

$ ./bitcoin-cli listtransactions
[
    {
        "address": "bc1q2r9mql4mkz3z7yfxvef76yxjd637r429620j75",
        "category": "receive",
        "amount": 0.00500000,
        "label": "",
        "vout": 1,
        "confirmations": 0,
        "trusted": false,
        "txid": "ebfd0d14c2ea74ce408d01d5ea79636b8dee88fe06625f5d4842d2a0ba45c195",
        "walletconflicts": [
        ],
        "time": 1541941483,
        "timereceived": 1541941483,
        "bip125-replaceable": "yes"
    }
]

Эта транзакция имеет 0 подтверждений и переводит 0,005 ВТС. Также можно заметить, что эта транзакция имеет идентификатор ebfdo1d14...ba45c195.

Рассмотрим эту транзакцию поближе, выполнив команду getrawtransaction:

$ ./bitcoin-cli getrawtransaction \
    ebfdo1d14c2ea74ce408d01d5ea79636b8dee88fe06625f5d4842d2a0ba45c195 1
{
    "txid": "ebfd0d14c2ea74ce408d01d5ea79636b8dee88fe06625f5d4842d2a0ba45c195",
    "hash": "ebfd0d14c2ea74ce408d01d5ea79636b8dee88fe06625f5d4842d2a0ba45c195",
    "version": 1,
    "size": 223,
    "vsize": 223,
    "weight": 892,
    "locktime": 549655,
    "vin": [
        {
            "txid": "8a4023dbcf57dc7f51d368606055e47636fc625a512d3481352a1eec909ab22f",
            "vout": 0,
            "scriptSig": {