---
source_image: page_475.png
page_number: 475
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.70
tokens: 7238
characters: 818
timestamp: 2025-12-24T08:43:23.858482
finish_reason: stop
---

Данная строка представляет собой JSON-объект, который описывает транзакцию на блокчейне Bitcoin. Включает в себя следующие ключевые поля:

- `txid`: хеш транзакции.
- `vout`: список выходов транзакции, где каждый выход имеет свой номер и сценарий публичного ключа (scriptPubKey).
- `scriptSig`: сценарий подтверждений входов транзакции.
- `txinwitness`: свидетельства входов транзакции.
- `sequence`: последовательность входов транзакции.

Внутри `vout` находятся два выхода:
1. Выход с номиналом 0.00399859, сценарий публичного ключа типа witness_v0_keyhash, адрес которого bc1qf0cyrun3hk2rshttetyys7kldjdgvtgs6ymhzz.
2. Выход с номиналом 0.00100000, сценарий публичного ключа типа witness_v0_keyhash, адрес которого bc1qu456w7a5mawlg35y00xu03wp8wc7d65t7uulqm.

`hex` — это шестнадцатеричный представление транзакции.