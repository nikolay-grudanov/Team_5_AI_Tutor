---
source_image: page_281.png
page_number: 281
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.03
tokens: 7443
characters: 2023
timestamp: 2025-12-24T08:52:59.593258
finish_reason: stop
---

import affineCipher, simpleSubCipher, transpositionCipher
--опущено--
ciphertext1 = affineCipher.encryptMessage(encKey1, 'Hello!')
ciphertext2 = transpositionCipher.encryptMessage(encKey2, 'Hello!')
ciphertext3 = simpleSubCipher.encryptMessage(encKey3, 'Hello!')

Соглашения об именах полезны тем, что, поработав с одной программой шифрования, можно легко перейти к использованию других аналогичных программ. Например, вы уже знаете, что первым аргументом функции всегда является ключ, а вторым — сообщение. Этого соглашения мы последовательно придерживаемся во всех программах шифрования, рассматриваемых в книге. Использование единой функции translateMessage() вместо отдельных функций encryptMessage() и decryptMessage() нарушило бы согласованность с другими программами.

Теперь перейдем к рассмотрению функции translateMessage().

Функция translateMessage()

Функция translateMessage() предназначена как для шифрования, так и для дешифрования сообщений.

45. def translateMessage(key, message, mode):
46.    translated = ''
47.    charsA = LETTERS
48.    charsB = key
49.    if mode == 'decrypt':
50.        # Для дешифрования можно использовать тот же самый код,
51.        # нужно лишь поменять местами строки key и LETTERS
52.        charsA, charsB = charsB, charsA

Обратите внимание на то, что у функции есть не только параметры key и message, но и третий параметр: mode. При вызове из функции encryptMessage() он равен 'encrypt', а при вызове из функции decryptMessage() — 'decrypt'. Именно так функция translateMessage() узнает, должна ли она шифровать или дешифровать переданное ей сообщение.

Сам процесс шифрования довольно прост: для каждой буквы, которая встречается в параметре message, функция определяет ее индекс в строке LETTERS и заменяет соответствующий символ буквой, которая встречается под тем же индексом в параметре key. В процессе дешифрования выполняется противоположное действие: находится индекс в параметре key и соответствующий символ заменяется буквой с тем же индексом в строке LETTERS.