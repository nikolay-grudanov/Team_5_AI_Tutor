---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.92
tokens: 7464
characters: 1194
timestamp: 2025-12-24T09:12:32.669810
finish_reason: stop
---

![Режим CTR](https://i.imgur.com/3Q5z5QG.png)

Рис. 4.10. Режим CTR

Листинг 4.6. Использование AES в режиме CTR

#!/usr/bin/env python

from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from os import urandom
from struct import unpack

k = urandom(16)
print "k = %s" % hexa(k)

# выбрать одноразовое число
nonce = unpack('<Q', urandom(8))[0]

# создать объект счетчика
ctr = Counter.new(128, initial_value=nonce)
# создать экземпляр AES в режиме CTR, используя ctr в качестве счетчика
aes = AES.new(k, AES.MODE_CTR, counter=ctr)

# в режиме CTR шифровать целый блок необязательно
p = '\x00\x01\x02\x03'

# зашифровать p
c = aes.encrypt(p)
print "enc(%s) = %s" % (hexa(p), hexa(c))

# дешифрировать, используя функцию шифрования
ctr = Counter.new(128, initial_value=nonce)
aes = AES.new(k, AES.MODE_CTR, counter=ctr)
p = aes.encrypt(c)
print "enc(%s) = %s" % (hexa(c), hexa(p))

В этом примере шифруется 4-байтовый открытый текст, и в результате получается 4-байтовый шифртекст. Затем шифртекст дешифрируется с применением функции шифрования:

$ ./aes_ctr.py
k = 130a1aa77fa58335272156421cb2a3ea
enc(00010203) = b23d284e
enc(b23d284e) = 00010203