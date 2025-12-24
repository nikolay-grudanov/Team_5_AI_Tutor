---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.77
tokens: 7686
characters: 1878
timestamp: 2025-12-24T09:12:32.683839
finish_reason: stop
---

сдвиг в противоположном направлении, для обращения MixColumns применить преобразование, описываемое обратной матрицей, а AddRoundKey не изменяется, потому что обращением операции XOR является она сама.

AES в действии

Чтобы потренироваться в зашифровывании и дешифрировании с помощью AES, можете воспользоваться криптографической библиотекой Python, как в листинге 4.1.

Листинг 4.1. Эксперименты с AES с применением криптографической библиотеки Python

#!/usr/bin/env python

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

# выбрать случайный 16-байтовый ключ, воспользовавшись PRNG, включенным в Python
k = urandom(16)
print "k = %s" % hexa(k)
# создать экземпляр AES-128 для шифрования одного блока
cipher = Cipher(algorithms.AES(k), modes.ECB(), backend = default_backend())
aes_encrypt = cipher.encryptor()

# выбрать в качестве блока открытого текста строку, состоящую из одних нулей
p = '\x00'*16
# зашифровать открытый текст p, получив шифртекст с
c = aes_encrypt.update(p) + aes_encrypt.finalize()
print "enc(%s) = %s" % (hexa(p), hexa(c))
# дешифрировать шифртекст с в открытый текст p
aes_decrypt = cipher.decryptor()
p = aes_decrypt.update(c) + aes_decrypt.finalize()
print "dec(%s) = %s" % (hexa(c), hexa(p))
При выполнении этого скрипта будет напечатано что-то типа:
$ ./aes_block.py
k = 2c6202f9a582668aa96d511862d8a279
enc(00000000000000000000000000000000) = 12b620bb5eddcde9a07523e59292a6d7
dec(12b620bb5eddcde9a07523e59292a6d7) = 00000000000000000000000000000000

На вашем компьютере результат будет иным, потому что ключ выбирается случайно при каждом выполнении.

Реализация AES

Настоящие реализации AES работают не так, как алгоритм на рис. 4.4. В производственном коде AES вы не увидите вызова функции Sub-