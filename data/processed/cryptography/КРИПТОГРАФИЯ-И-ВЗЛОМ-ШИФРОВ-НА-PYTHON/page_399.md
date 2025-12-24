---
source_image: page_399.png
page_number: 399
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.38
tokens: 7435
characters: 1881
timestamp: 2025-12-24T08:56:09.498170
finish_reason: stop
---

В строке 236 для каждой возможной длины ключа вызывается функция attemptHackWithKeyLength(). Если она не вернула значение None, то взлом считается успешным, и программа выходит из цикла в строке 238.

Тестирование всех остальных вариантов длины ключа методом грубой силы

Если попытки взлома с использованием всех возможных вариантов длины ключа, возвращаемых функцией kasiskiExamination(), оказались неудачными, то в строке 242 переменная hackedMessage окажется равна None. В этом случае проверяются все остальные варианты длины ключа вплоть до MAX_KEY_LENGTH. Другими словами, если с помощью метода Касиски не удалось вычислить корректную длину ключа, то мы выполняем полный перебор вариантов в цикле for (строка 245).

242. if hackedMessage == None:
243.     if not SILENT_MODE:
244.         print('Unable to hack message with likely key length(s).
245.             Brute-forcing key length...')
246.         # Не перепроверять длину ключа, уже опробованную
247.         if keyLength not in allLikelyKeyLengths:
248.             if not SILENT_MODE:
249.                 print('Attempting hack with key length %s (%s possible keys)...' % (keyLength,
250.                     NUM_MOST_FREQ_LETTERS ** keyLength))
251.                 hackedMessage = attemptHackWithKeyLength(ciphertext,
252.                     keyLength)
253.                 if hackedMessage != None:
254.                     break

В строке 245 начинается цикл for, в котором для каждого значения переменной keyLength (имеющей значения от 1 до MAX_KEY_LENGTH) вызывается функция attemptHackWithKeyLength(), при условии, что это значение не содержится в списке allLikelyKeyLengths. Причина заключается в том, что значения длины ключа, содержащиеся в переменной allLikelyKeyLengths, ранее уже были проверены (строки 233–238).

Наконец, значение hackedMessage возвращается в строке 253:

253. return hackedMessage