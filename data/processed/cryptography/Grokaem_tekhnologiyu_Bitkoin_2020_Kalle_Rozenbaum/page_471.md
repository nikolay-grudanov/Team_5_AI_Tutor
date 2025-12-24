---
source_image: page_471.png
page_number: 471
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.29
tokens: 8157
characters: 1729
timestamp: 2025-12-24T08:43:52.785947
finish_reason: stop
---

"asm": "3045022100cc095e6b7c0d4c42a1741371cfdda4f1b518590f1af
0915578d3966fee7e34ea02205fc1e976edcf4fe62f16035a5389c661844f7189
a9eb45adf59e061ac8cc6fd3[ALL]
030ace35cc192cedfe2a730244945f1699ea2f6b7ee77c65c83a2d7a37440e3dae",
"hex":
"483045022100cc095e6b7c0d4c42a1741371cfdda4f1b518590f1af0915578d3966
fee7e34ea02205fc1e976edcf4fe62f16035a5389c661844f7189a9eb45adf59e061
ac8cc6fd 30121030ace35cc192cedfe2a730244945f1699ea2f6b7ee77c65c83a2d7
a37440e3dae"
},
"sequence": 4294967293
}
],
"vout": [
{
"value": 0.00313955,
"n": 0,
"scriptPubKey": {
"asm": "OP_DUP OP_HASH160 6da68d8f89dced72d4339959c94a4fcc872fa089
OP_EQUALVERIFY OP_CHECKSIG",
"hex": "76a9146da68d8f89dced72d4339959c94a4fcc872fa08988ac",
"reqSigs": 1,
"type": "pubkeyhash",
"addresses": [
"1AznBDM2ZfjYNoRw3DLSR9NL2cwwqDHJY6"
]
}
},
{
"value": 0.00500000,
"n": 1,
"scriptPubKey": {
"asm": "0 50cbb07ebbb0a22f11266653ed10d26ea3e1d545",
"hex": "001450cbb07ebbb0a22f11266653ed10d26ea3e1d545",
"reqSigs": 1,
"type": "witness_v0_keyhash",
"addresses": [
"bc1q2r9mq14mkz3z7yfxvef76yxjd637r429620j75"
]
}
}
],
"hex":
"01000000012fb29a90ec1e2a3581342d515a62fc3676e455606068d3517fdc57cfdb
23408a000000006b483045022100cc095e6b7c0d4c42a1741371cfdda4f1b518590f1
af0915578d3966fee7e34ea02205fc1e976edcf4fe62f16035a5389c661844f7189a9
eb45adf59e061ac8cc6fd30121030ace35cc192cedfe2a730244945f1699ea2f6b7ee77
c65c83a2d7a37440e3daeffffff0263ca0400000000001976a9146da68d8f89dced72
d4339959c94a4fcc872fa0898820a10700000000016001450cbb07ebbb0a22f11266653
ed10d26ea3e1d54517630800"
}

Эта команда вывела транзакцию целиком в удобочитаемой (по крайней мере, для разработчика) форме. Начнем сначала и пройдемся по самым важным разделам этой транзакции. txid — это идентификатор транзакции.