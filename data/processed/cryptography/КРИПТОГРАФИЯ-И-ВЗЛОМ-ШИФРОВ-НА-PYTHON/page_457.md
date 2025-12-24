---
source_image: page_457.png
page_number: 457
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.25
tokens: 7463
characters: 1962
timestamp: 2025-12-24T08:57:39.570972
finish_reason: stop
---

35.
36. def getBlocksFromText(message, blockSize):
37.     # Преобразует строку сообщения в список целочисленных блоков
38.     for character in message:
39.         if character not in SYMBOLS:
40.             print('ERROR: The symbol set does not have the character %s' % (character))
41.             sys.exit()
42.     blockInts = []
43.     for blockStart in range(0, len(message), blockSize):
44.         # Вычисляем целочисленный блок для текущей группы символов
45.         blockInt = 0
46.         for i in range(blockStart, min(blockStart + blockSize, len(message))):
47.             blockInt += (SYMBOLS.index(message[i])) * (len(SYMBOLS) ** (i % blockSize))
48.         blockInts.append(blockInt)
49.     return blockInts

52. def getTextFromBlocks(blockInts, messageLength, blockSize):
53.     # Преобразует список целочисленных блоков в строку исходного сообщения. Необходимо задать длину исходного сообщения, чтобы корректно преобразовать последний блок.
56.     message = []
57.     for blockInt in blockInts:
58.         blockMessage = []
59.         for i in range(blockSize - 1, -1, -1):
60.             if len(message) + i < messageLength:
61.                 # Декодирование строки сообщения для нужного числа символов (задается переменной blockSize) из блока
62.                 charIndex = blockInt // (len(SYMBOLS) ** i)
63.                 blockInt = blockInt % (len(SYMBOLS) ** i)
65.                 blockMessage.insert(0, SYMBOLS[charIndex])
66.             message.extend(blockMessage)
67.     return ''.join(message)

70. def encryptMessage(message, key, blockSize):
71.     # Преобразует строку сообщения в список целочисленных блоков и шифрует каждый блок. Для шифрования нужен ОТКРЫТЫЙ ключ.
73.     encryptedBlocks = []
74.     n, e = key
76.     for block in getBlocksFromText(message, blockSize):
77.         # шифротекст = сообщение ^ e mod n
78.         encryptedBlocks.append(pow(block, e, n))
79.     return encryptedBlocks