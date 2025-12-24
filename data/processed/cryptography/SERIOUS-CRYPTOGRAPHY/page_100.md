---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.69
tokens: 7859
characters: 2023
timestamp: 2025-12-24T09:12:48.053601
finish_reason: stop
---

шифровании одинаковых открытых текстов будут получаться разные шифртексты.

В листинге 4.5 иллюстрируются оба этих преимущества. Программа принимает 32-байтовое сообщение, состоящее из одних нулей (как в листинге 4.4), дважды зашифровывает его в режиме CBC и выводит оба шифртекста. В строке iv = urandom(16), выделенной полужирным шрифтом, выбирается случайное начальное значение для каждого нового шифрования.

Листинг 4.5. Использование AES в режиме CBC

#!/usr/bin/env python

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

BLOCKLEN = 16
# функция blocks() разбивает строку данных на блоки, разделенные пробелами
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]
    return ' '.join(split)
k = urandom(16)
print "k = %s" % hexa(k)
# выбрать случайное начальное значение IV
iv = urandom(16)
print "iv = %s" % hexa(iv)
# создать экземпляр AES в режиме CBC
aes = Cipher(algorithms.AES(k), modes.CBC(iv), backend=default_backend()).encryptor()

p = '\x00'*BLOCKLEN*2
c = aes.update(p) + aes.finalize()
print "enc(%s) = %s" % (blocks(p), blocks(c))
# теперь с другим IV и тем же самым ключом
iv = urandom(16)
print "iv = %s" % hexa(iv)
aes = Cipher(algorithms.AES(k), modes.CBC(iv), backend=default_backend()).encryptor()
c = aes.update(p) + aes.finalize()
print "enc(%s) = %s" % (blocks(p), blocks(c))

Оба открытых текста одинаковы (состоят из одних нулей), но зашифрованные блоки должны быть разными, как в примере ниже:

$ ./aes_cbc.py
k = 9cf0d31ad2df24f3cbbefc1e6933c872
iv = 0a75c4283b4539c094fc262aff0d17af
enc(00000000000000000000000000000000 00000000000000000000000000000000) =
370404dcab6e9ecbc3d24ca5573d2920 3b9e5d70e597db225609541f6ae9804a
iv = a6016a6698c3996be13e8739d9e793e2
enc(00000000000000000000000000000000 00000000000000000000000000000000) =
655e1bb3e74ee8cf9ec1540afd8b2204 b59db5ac28de43b25612dfd6f031087a