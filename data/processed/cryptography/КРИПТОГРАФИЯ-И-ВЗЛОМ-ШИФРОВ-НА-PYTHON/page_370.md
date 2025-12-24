---
source_image: page_370.png
page_number: 370
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.38
tokens: 7606
characters: 2309
timestamp: 2025-12-24T08:55:23.143373
finish_reason: stop
---

28. def findRepeatSequencesSpacings(message):
29.     # Находит в сообщении любые 3-, 4- и 5-буквенные повторяющиеся
30.     # последовательности. Возвращает словарь, в котором ключи — это
31.     # последовательности, а значения — списки интервалов повторения.
32.
33.     # Используем регулярное выражение для удаления небуквенных символов
34.     message = NONLETTERS_PATTERN.sub('', message.upper())
35.
36.     # Получение списка последовательностей, найденных в сообщении
37.     seqSpacings = {}  # ключи — последовательности, значения —
38.                                 списки интервалов повторения
39.     for seqLen in range(3, 6):
40.         for seqStart in range(len(message) - seqLen):
41.             # Получение очередной последовательности
42.             seq = message[seqStart:seqStart + seqLen]
43.             # Поиск этой последовательности в остальной части сообщения
44.             for i in range(seqStart + seqLen, len(message) - seqLen):
45.                 if message[i:i + seqLen] == seq:
46.                     # Найдена повторяющаяся последовательность
47.                     if seq not in seqSpacings:
48.                         seqSpacings[seq] = []  # пустой список
49.                         # Добавить интервал повторения между исходной
50.                         # и повторившейся последовательностями
51.                         seqSpacings[seq].append(i - seqStart)
52.
53.     return seqSpacings
54.
55.
56. def getUsefulFactors(num):
57.     # Возвращает список полезных множителей параметра num. Полезными
58.     # считаются множители от 2 до MAX_KEY_LENGTH. Например, вызов
59.     # getUsefulFactors(144) вернет [2, 3, 4, 6, 8, 9, 12, 16].
60.
61.     if num < 2:
62.         return []  # числа, меньше 2, не имеют полезных множителей
63.
64.     factors = []  # список найденных множителей
65.
66.     # При поиске множителей необходимо проверять лишь целые
67.     # числа вплоть до MAX_KEY_LENGTH
68.     for i in range(2, MAX_KEY_LENGTH + 1):  # множитель 1 бесполезен
69.         if num % i == 0:
70.             factors.append(i).
71.             otherFactor = int(num / i)
72.             if otherFactor < MAX_KEY_LENGTH + 1 and otherFactor != 1:
73.                 factors.append(otherFactor)
74.     return list(set(factors))  # удаляем дубликаты