---
source_image: page_084.png
page_number: 84
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.79
tokens: 7444
characters: 1728
timestamp: 2025-12-24T03:03:07.932683
finish_reason: stop
---

При хранении такого ключа в файле необходимо использовать двоичный тип данных. Следующий шаг — шифрование данных с помощью объекта Fernet:

In [4]: f = Fernet(key)

In [5]: message = b"Secrets go here"

In [6]: encrypted = f.encrypt(message)

In [7]: encrypted
Out[7]: b'gAAAAABdPyg4 ... plhkpvkC8ezOHaOLIA=='

Расшифровать данные можно с помощью объекта Fernet, созданного на основе того же ключа:

In [1]: f = Fernet(key)

In [2]: f.decrypt(encrypted)
Out[2]: b'Secrets go here'

При шифровании с асимметричным ключом используется пара ключей: один открытый, а второй секретный. Открытый ключ должен быть общедоступным, а секретный — известен только одному пользователю. Расшифровать зашифрованные с помощью открытого ключа сообщения можно, только задействуя соответствующий секретный ключ. Эта разновидность шифрования широко применяется для безопасной передачи информации как в локальных сетях, так и через Интернет. Один из самых популярных алгоритмов шифрования с асимметричным ключом RSA (Rivest — Shamir — Adleman, Ривест — Шамир — Адлеман) широко используется для общения в различных сетях. Библиотека cryptography позволяет создавать пары из открытого и секретного ключей:

In [1]: from cryptography.hazmat.backends import default_backend

In [2]: from cryptography.hazmat.primitives.asymmetric import rsa

In [3]: private_key = rsa.generate_private_key(public_exponent=65537,
   key_size=4096,
   backend=default_backend())

In [4]: private_key
Out[4]: <cryptography.hazmat.backends.openssl.rsa._RSAPrivateKey at 0x10d377c18>

In [5]: public_key = private_key.public_key

In [6]: public_key = private_key.public_key()

In [7]: public_key
Out[7]: <cryptography.hazmat.backends.openssl.rsa._RSAPublicKey at 0x10da642b0>