---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.49
tokens: 7367
characters: 1161
timestamp: 2025-12-24T09:12:21.297768
finish_reason: stop
---

Рис. 4.7. Исходное изображение (слева) и оно же, зашифрованное в режиме ECB (справа)

Программа на Python в листинге 4.4 также демонстрирует небезопасность ECB. Она выбирает псевдослучайный ключ и шифрует 32-байтовое сообщение p, содержащее два блока нулевых байтов. Заметьте, что шифрование дает два идентичных блока, а при повторном шифровании с тем же ключом и тем же открытым текстом снова получаются те же самые два блока.

Листинг 4.4. Использование AES в режиме ECB в Python

#!/usr/bin/env python

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

BLOCKLEN = 16
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]
    return ' '.join(split)

k = urandom(16)
print "k = %s" % hexa(k)

# создать экземпляр AES-128 для шифрования и дешифрирования
cipher = Cipher(algorithms.AES(k), modes.ECB(), backend=default_backend())
aes_encrypt = cipher.encryptor()

# блок p открытого текста содержит все нули
p = '\x00'*BLOCKLEN*2

# зашифровать открытый текст p в шифртекст c