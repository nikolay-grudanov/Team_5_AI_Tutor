---
source_image: page_395.png
page_number: 395
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.11
tokens: 7384
characters: 1677
timestamp: 2025-12-24T08:55:57.275693
finish_reason: stop
---

>>> allFreqScores[1][0]
('S', 10)
>>> allFreqScores[1][1]
('D', 4)

Поскольку эти значения являются кортежами, для получения самой буквы без оценки ее частотного соответствия потребуется обратиться к первому элементу кортежа. Таким образом, для доступа к наиболее вероятной букве второго подключа мы должны использовать элемент allFreqScores[1][0][0], для доступа ко второй наиболее вероятной букве этого же подключа — элемент allFreqScores[1][1][0] и т.д.

>>> allFreqScores[1][0][0]
'S'
>>> allFreqScores[1][1][0]
'D'

Разобравшись с доступом к потенциальным подключам, содержащимся в списке allFreqScores, мы должны скомбинировать их для нахождения потенциальных ключей.

Создание комбинаций подключей с помощью функции itertools.product()

Каждый из кортежей, созданных с помощью функции itertools.product(), представляет один ключ, причем позиция в кортеже соответствует первому индексу, по которому мы получаем доступ к списку allFreqScores, а целые числа в кортеже представляют второй индекс в списке allFreqScores.

Поскольку ранее мы установили для константы NUM_MOST_FREQ_LETTERS значение 4, вызов itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength) в строке 188 означает, что для каждого значения переменной indexes в цикле for мы получаем кортеж целых чисел (от 0 до 3), представляющих четыре наиболее вероятные буквы для каждого подключа.

188.    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS),
        repeat=mostLikelyKeyLength):
189.    # Создаем возможный ключ из букв в списке allFreqScores
190.    possibleKey = ''
191.    for i in range(mostLikelyKeyLength):
192.        possibleKey += allFreqScores[i][indexes[i]][0]