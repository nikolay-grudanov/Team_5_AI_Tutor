---
source_image: page_371.png
page_number: 371
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.74
tokens: 7679
characters: 2238
timestamp: 2025-12-24T08:55:26.535345
finish_reason: stop
---

77. def getItemAtIndexOne(x):
78.     return x[1]
79.
80.
81. def getMostCommonFactors(seqFactors):
82.     # Во-первых, подсчитываем повторы множителей в словаре seqFactors
83.     factorCounts = {}  # ключ - множитель; значение - число повторений
84.
85.     # Ключи словаря seqFactors - это цепочки букв, а значения - списки
86.     # множителей интервалов повторения. Словарь выглядит примерно так:
87.     # {'GFD': [2, 3, 4, 6, 9, 12, 18, 23, 36, 46, 69, 92, 138, 207],
88.         'ALW': [2, 3, 4, 6, ...], ...}
89.     for seq in seqFactors:
90.         factorList = seqFactors[seq]
91.         for factor in factorList:
92.             if factor not in factorCounts:
93.                 factorCounts[factor] = 0
94.                 factorCounts[factor] += 1
95.
96.     # Во-вторых, объединяем множители и счетчики повторений в кортежи
97.     # и создаем список таких кортежей, чтобы их можно было сортировать
98.     factorsByCount = []
99.     for factor in factorCounts:
100.         # Исключаем множители, которые больше, чем MAX_KEY_LENGTH
101.         if factor <= MAX_KEY_LENGTH:
102.             # factorsByCount - список кортежей (множитель, счетчик).
103.             # Типичный вид: [(3, 497), (2, 487), ...]
104.             factorsByCount.append( (factor, factorCounts[factor]) )
105.
106.     # Сортировка списка по счетчикам повторений
107.     factorsByCount.sort(key=getItemAtIndexOne, reverse=True)
108.
109.     return factorsByCount
110.
111. def kasiskiExamination(ciphertext):
112.     # Находим последовательности длиной от 3 до 5 букв, встречающиеся
113.     # в шифротексте неоднократно. Словарь repeatedSeqSpacings выглядит
114.     # примерно так: {'EXG': [192], 'NAF': [339, 972, 633], ... }
115.     repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)
116.
117.     # См. описание словаря seqFactors в функции getMostCommonFactors()
118.     seqFactors = {}
119.     for seq in repeatedSeqSpacings:
120.         seqFactors[seq] = []
121.         for spacing in repeatedSeqSpacings[seq]:
122.             seqFactors[seq].extend(getUsefulFactors(spacing))
123.
124.     # См. описание factorsByCount в функции getMostCommonFactors()
125.     factorsByCount = getMostCommonFactors(seqFactors)