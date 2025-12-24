---
source_image: page_469.png
page_number: 469
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.41
tokens: 7426
characters: 1747
timestamp: 2025-12-24T08:58:06.557110
finish_reason: stop
---

76. for block in getBlocksFromText(message, blockSize):
77. # шифротекст = сообщение ^ e mod n
78. encryptedBlocks.append(pow(block, e, n))
79. return encryptedBlocks

Полученный зашифрованный блок добавляется в список encryptedBlocks.

Функция decryptMessage()

Функция decryptMessage() дешифрует список блоков и возвращает дешифрованную строку сообщения. В качестве аргументов ей передается список зашифрованных блоков, длина сообщения, кортеж закрытого ключа и размер блока.

В строке 86 создается список decryptedBlocks, предназначенный для хранения дешифрованных блоков, а в строке 87 мы применяем трюк с групповым присваиванием для записи двух целочисленных составляющих кортежа ключа в переменные n и d.

82. def decryptMessage(encryptedBlocks, messageLength, key, blockSize):
83. # Дешифрует список зашифрованных блоков в строку сообщения,
84. # длину которого необходимо задать, чтобы корректно дешифровать
85. # последний блок. Для дешифрования нужен ЗАКРЫТЫЙ ключ.
86. decryptedBlocks = []
87. n, d = key

Арифметика дешифрования блоков та же, что и в случае шифрования, за исключением того, что целочисленное значение блока возводится не в степень e, а в степень d (строка 90).

88. for block in encryptedBlocks:
89. # сообщение = шифротекст ^ d mod n
90. decryptedBlocks.append(pow(block, d, n))

Список дешифрованных блоков вместе с параметрами messageLength и blockSize передается функции getTextFromBlocks(), и результат возвращается в виде дешифрованного текста.

91. return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)

Теперь следует рассмотреть, каким образом функция readKeyFile() считывает открытый и закрытый ключи из файлов и создает кортежи, которые передаются функциям encryptMessage() и decryptMessage().