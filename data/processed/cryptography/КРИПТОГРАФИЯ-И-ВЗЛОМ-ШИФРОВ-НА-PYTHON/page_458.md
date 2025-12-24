---
source_image: page_458.png
page_number: 458
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.00
tokens: 7607
characters: 2314
timestamp: 2025-12-24T08:57:48.222007
finish_reason: stop
---

81.
82. def decryptMessage(encryptedBlocks, messageLength, key, blockSize):
83.     # Дешифрует список зашифрованных блоков в строку сообщения,
84.     # длину которого необходимо задать, чтобы корректно дешифровать
85.     # последний блок. Для дешифрования нужен ЗАКРЫТЫЙ ключ.
86.     decryptedBlocks = []
87.     n, d = key
88.     for block in encryptedBlocks:
89.         # сообщение = шифротекст ^ d mod n
90.         decryptedBlocks.append(pow(block, d, n))
91.     return getTextFromBlocks(decryptedBlocks, messageLength,
92.                                 blockSize)
93.
94. def readKeyFile(keyFilename):
95.     # Считывает из указанного файла открытый или
96.     # закрытый ключ в виде кортежа (n,e) или (n,d)
97.     fo = open(keyFilename)
98.     content = fo.read()
99.     fo.close()
100.    keySize, n, EorD = content.split(',')
101.    return (int(keySize), int(n), int(EorD))
102.
103.
104. def encryptAndWriteToFile(messageFilename, keyFilename, message,
105.                             blockSize=None):
106.     # Считывает ключ из файла, шифрует сообщение и сохраняет его
107.     # в выходном файле, возвращая зашифрованную строку
108.     keySize, n, e = readKeyFile(keyFilename)
109.     if blockSize == None:
110.         # Если параметр blockSize не задан, сделать его максимально
111.         # допустимым для текущей длины ключа и размера набора символов
112.         blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))
113.     # Проверяем, достаточно ли длины ключа для данного размера блока
114.     if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
115.         sys.exit('ERROR: Block size is too large for the key and
116.                     symbol set size. Did you specify the correct key file
117.                     and encrypted file?')
118.     # Шифруем сообщение
119.     encryptedBlocks = encryptMessage(message, (n, e), blockSize)
120.     # Преобразование больших целочисленных значений в единую строку
121.     for i in range(len(encryptedBlocks)):
122.         encryptedBlocks[i] = str(encryptedBlocks[i])
123.     encryptedContent = ','.'join(encryptedBlocks)
124.
125.     # Запись зашифрованной строки в выходной файл
126.     encryptedContent = '%s_%s_%s' % (len(message), blockSize,
127.                                         encryptedContent)