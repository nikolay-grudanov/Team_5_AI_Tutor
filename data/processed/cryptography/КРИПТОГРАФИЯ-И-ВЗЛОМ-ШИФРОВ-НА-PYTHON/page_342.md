---
source_image: page_342.png
page_number: 342
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.25
tokens: 7468
characters: 1710
timestamp: 2025-12-24T08:54:30.525793
finish_reason: stop
---

40. # обратный порядку "ETAOIN" и превращаем списки в строки
41. for freq in freqToLetter:
42.     freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
43.     freqToLetter[freq] = ''.join(freqToLetter[freq])
44.
45. # В-четвертых, преобразуем словарь freqToLetter в список
46. # кортежей (ключ, значение) и сортируем его
47. freqPairs = list(freqToLetter.items())
48. freqPairs.sort(key=getItemAtIndexZero, reverse=True)
49.
50. # В-пятых, после того как буквы были упорядочены по частотности,
51. # извлекаем все буквы для формирования окончательной строки
52. freqOrder = []
53. for freqPair in freqPairs:
54.     freqOrder.append(freqPair[1])
55.
56. return ''.join(freqOrder)
57.
58.
59. def englishFreqMatchScore(message):
60.     # Возвращает оценку частотного соответствия для строки
61.     # message. Совпадения проверяются по шести наиболее
62.     # и наименее часто встречающимся буквам в строке
63.     # и в английском языке в целом.
64.
65. freqOrder = getFrequencyOrder(message)
66.
67. matchScore = 0
68. # Число совпадений для шести наиболее часто встречающихся букв
69. for commonLetter in ETAOIN[:6]:
70.     if commonLetter in freqOrder[:6]:
71.         matchScore += 1
72. # Число совпадений для шести наименее часто встречающихся букв
73. for uncommonLetter in ETAOIN[-6:]:
74.     if uncommonLetter in freqOrder[-6:]:
75.         matchScore += 1
76.
77. return matchScore

Сохранение букв алфавита в порядке ETAOIN

В строке 4 создается переменная ETAOIN, в которой сохраняются 26 букв алфавита, расположенных в порядке убывания их частотности.

1. # Определение частотности букв
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'