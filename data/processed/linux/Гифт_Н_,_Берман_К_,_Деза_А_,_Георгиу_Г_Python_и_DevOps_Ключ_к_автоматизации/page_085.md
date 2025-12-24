---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.57
tokens: 7428
characters: 1714
timestamp: 2025-12-24T03:03:07.766177
finish_reason: stop
---

Далее можно зашифровать данные с помощью открытого ключа:

In [8]: message = b"More secrets go here"

In [9]: from cryptography.hazmat.primitives.asymmetric import padding
In [11]: from cryptography.hazmat.primitives import hashes

In [12]: encrypted = public_key.encrypt(message,
    ...:     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256())),
    ...:     algorithm=hashes.SHA256(),
    ...:     label=None))

И расшифровать их с помощью секретного ключа:

In [13]: decrypted = private_key.decrypt(encrypted,
    ...:     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256())),
    ...:     algorithm=hashes.SHA256(),
    ...:     label=None))

In [14]: decrypted
Out[14]: b'More secrets go here'

Модуль os

os — один из чаще всего используемых модулей Python, позволяющий выполнять множество низкоуровневых системных вызовов. Кроме того, он предоставляет единообразный интерфейс для различных операционных систем, что важно для приложений, которые может понадобиться применять как в Windows-, так и в Unix-системах. Он также обеспечивает некоторые возможности, ориентированные на конкретные операционные системы (os.O_TEXT для Windows и os.O_CLOEXEC в Linux) и недоступные на всех платформах. Использовать их следует только в том случае, если для приложения точно не требуется переносимость между различными операционными системами. В примере 2.1 показаны некоторые из самых полезных методов модуля os.

Пример 2.1. Методы модуля os

In [1]: os.listdir('.') ①
Out[1]: ['__init__.py', 'os_path_example.py']

In [2]: os.rename('_crud_handler', 'crud_handler') ②

In [3]: os.chmod('my_script.py', 0o777) ③

In [4]: os.mkdir('/tmp/holding') ④

In [5]: os.makedirs('/Users/kbehrman/tmp/scripts/devops') ⑤