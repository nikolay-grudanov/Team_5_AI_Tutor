---
source_image: page_462.png
page_number: 462
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.48
tokens: 7504
characters: 2190
timestamp: 2025-12-24T08:57:56.421540
finish_reason: stop
---

12. def main():
13.    # Проверяем, что необходимо сделать: записать зашифрованное
14.    # сообщение в файл или дешифровать сообщение, прочитанное из файла
15.    filename = 'encrypted_file.txt'  # файл для чтения/записи
16.    mode = 'encrypt'  # задать 'encrypt' или 'decrypt'

Если в строке 16 для переменной mode задано значение 'encrypt', то программа зашифрует сообщение и запишет его в файл, имя которого содержится в переменной filename. Если же переменная mode равна 'decrypt', то программа прочитает содержимое зашифрованного файла (его имя берется из переменной filename) и дешифрует его.
Строки 18–25 определяют порядок действий в случае шифрования.

18.    if mode == 'encrypt':
19.        message = 'Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets. Gerald Priestland. The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people. Hugo Black.'
20.        pubKeyFilename = 'al_sweigart_pubkey.txt'
21.        print('Encrypting and writing to %s...' % (filename))
22.        encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)
23.
24.        print('Encrypted text:')
25.        print(encryptedText)

Переменная message (строка 19) содержит текст, подлежащий шифрованию, а переменная pubKeyFilename (строка 20) задает имя файла открытого ключа (в данном примере это файл al_sweigart_pubkey.txt). Не забывайте о том, что переменная message может содержать лишь символы, которые входят в состав используемого символьного набора, хранящегося в переменной SYMBOLS. В строке 22 вызывается функция encryptAndWriteToFile(), которая шифрует сообщение с помощью открытого ключа и записывает его в файл, задаваемый переменной filename.

Строки 27–33 определяют порядок действий, когда переменная mode содержит строку 'decrypt'. В этом случае вместо того, чтобы шифровать сообщение, программа считывает содержимое файла закрытого ключа, имя которого задано в переменной privKeyFilename (строка 28).

27.    elif mode == 'decrypt':
28.        privKeyFilename = 'al_sweigart_privkey.txt'
29.        print('Reading from %s and decrypting...' % (filename))