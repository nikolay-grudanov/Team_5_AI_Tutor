---
source_image: page_295.png
page_number: 295
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.33
tokens: 7544
characters: 2019
timestamp: 2025-12-24T08:53:21.695917
finish_reason: stop
---

29. pyperclip.copy(hackedMessage)
30. print(hackedMessage)

33. def getBlankCipherletterMapping():
34.     # Возвращает пустой дешифровальный словарь
35.     return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 
36.             'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 
37.             'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 
38.             'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 
39.             'X': [], 'Y': [], 'Z': []}

38. def addLettersToMapping(letterMapping, cipherword, candidate):
39.     # Параметр letterMapping - это дешифровальный словарь,
40.     # обрабатываемый данной функцией.
41.     # Параметр cipherword - это строковое значение шифрослова.
42.     # Параметр candidate - это английское слово-кандидат,
43.     # в которое может быть дешифровано данное шифрослово.
44. 
45.     # Функция добавляет в дешифровальный словарь
46.     # буквы слова-кандидата в качестве вариантов
47.     # дешифрования шифробукв.

50. for i in range(len(cipherword)):
51.     if candidate[i] not in letterMapping[cipherword[i]]:
52.         letterMapping[cipherword[i]].append(candidate[i])

56. def intersectMappings(mapA, mapB):
57.     # Чтобы построить пересечение словарей, создаем пустой словарь и
58.     # добавляем в него только варианты, существующие в ОБОИХ словарях
59.     intersectedMapping = getBlankCipherletterMapping()
60.     for letter in LETTERS:
61. 
62.         # Пустой список означает "возможна любая буква";
63.         # в этом случае копируем список целиком
64.         if mapA[letter] == []:
65.             intersectedMapping[letter] = copy.deepcopy(mapB[letter])
66.         elif mapB[letter] == []:
67.             intersectedMapping[letter] = copy.deepcopy(mapA[letter])
68.         else:
69.             # Если буква из словаря mapA[letter] существует в словаре
70.             # mapB[letter], добавляем ее в intersectedMapping[letter]
71.             for mappedLetter in mapA[letter]:
72.                 if mappedLetter in mapB[letter]: