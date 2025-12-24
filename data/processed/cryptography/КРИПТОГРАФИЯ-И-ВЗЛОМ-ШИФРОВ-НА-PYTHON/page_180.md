---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.28
tokens: 7473
characters: 1920
timestamp: 2025-12-24T08:50:27.012777
finish_reason: stop
---

Откройте в редакторе файлов новое окно, выбрав пункты меню File→New File. Введите приведенный ниже код и сохраните его в файле transpositionFileCipher.py. После этого скопируйте файл frankenstein.txt из папки с примерами книги и поместите в тот же каталог, в котором находится файл transpositionFileCipher.py. Запустите программу, нажав клавишу <F5>.

transpositionFileCipher.py

1. # Шифрование/дешифрование файлов с помощью перестановочного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import time, os, sys, transpositionEncrypt, transpositionDecrypt
5.
6. def main():
7.     inputFilename = 'frankenstein.txt'
8.     # БУДЬТЕ ВНИМАТЕЛЬНЫ: если файл с именем outputFilename
9.     # уже существует, программа перезапишет его
10.    outputFilename = 'frankenstein.encrypted.txt'
11.    myKey = 10
12.    myMode = 'encrypt'  # задать 'encrypt' или 'decrypt'
13.
14.    # Если входного файла не существует, программа завершается
15.    if not os.path.exists(inputFilename):
16.        print('The file %s does not exist. Quitting...' % (inputFilename))
17.        sys.exit()
18.
19.    # Если выходной файл существует, задать пользователю вопрос
20.    if os.path.exists(outputFilename):
21.        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
22.        response = input('> ')
23.        if not response.lower().startswith('c'):
24.            sys.exit()
25.
26.    # Прочитать сообщение из входного файла
27.    fileObj = open(inputFilename)
28.    content = fileObj.read()
29.    fileObj.close()
30.
31.    print('%sing...' % (myMode.title()))
32.
33.    # Измерить, как долго длится шифрование/дешифрование
34.    startTime = time.time()
35.    if myMode == 'encrypt':
36.        translated = transpositionEncrypt.encryptMessage(myKey, content)
37.    elif myMode == 'decrypt':
38.        translated = transpositionDecrypt.decryptMessage(myKey, content)