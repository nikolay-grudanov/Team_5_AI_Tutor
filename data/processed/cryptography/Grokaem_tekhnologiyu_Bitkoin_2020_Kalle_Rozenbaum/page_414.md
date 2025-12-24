---
source_image: page_414.png
page_number: 414
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.75
tokens: 7268
characters: 726
timestamp: 2025-12-24T08:41:39.760283
finish_reason: stop
---

414 Глава 10. Segwit

![p2pkh: адрес в формате 1](../images/ch10_30.png)
OP_DUP OP_HASH160 <PKH> OP_EQUALVERIFY OP_CHECKSIG
Рис. 10.30. p2pkh: адрес в формате 1<символы в кодировке base58>

![p2sh: адрес в формате 3](../images/ch10_31.png)
OP_HASH160 <SH> OP_EQUAL 2 3 OP_CHECKMULTISIG
Рис. 10.31. p2sh: адрес в формате 3<символы в кодировке base58>

![p2wpkh: адрес в формате bc1q<38 символов](../images/ch10_32.png)
00 <20 байт PKH>
Рис. 10.32. p2wpkh: адрес в формате bc1q<38 символов в кодировке base32>

![p2wsh: адрес в формате bc1q<58 символов](../images/ch10_33.png)
00 <32 байта WSH>
0.08 wSH 0 0.07 wSH_x
Сценарий свидетеля
2 3 OP_CHECKMULTISIG
Рис. 10.33. p2wsh: адрес в формате bc1q<58 символов в кодировке base32>