---
source_image: page_372.png
page_number: 372
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.26
tokens: 7634
characters: 2180
timestamp: 2025-12-24T08:55:28.293618
finish_reason: stop
---

126.
127.    # Извлекаем множители из списка factorsByCount
128.    # и помещаем их в список allLikelyKeyLengths, чтобы
129.    # с ними было проще работать
130.    allLikelyKeyLengths = []
131.    for twoIntTuple in factorsByCount:
132.        allLikelyKeyLengths.append(twoIntTuple[0])
133.
134.    return allLikelyKeyLengths
135.
136.
137. def getNthSubkeysLetters(nth, keyLength, message):
138.    # Возвращает каждую n-ю букву из каждого набора длиной keyLength.
139.    # Так, getNthSubkeysLetters(1, 3, 'ABCABCABC') возвращает 'AAA',
140.    #     getNthSubkeysLetters(2, 3, 'ABCABCABC') возвращает 'BBB',
141.    #     getNthSubkeysLetters(3, 3, 'ABCABCABC') возвращает 'CCC',
142.    #     getNthSubkeysLetters(1, 5, 'ABCDEFGHI') возвращает 'AF'.
143.
144.    # Используем регулярное выражение для удаления небуквенных символов
145.    message = NONLETTERS_PATTERN.sub('', message)
146.
147.    i = nth - 1
148.    letters = []
149.    while i < len(message):
150.        letters.append(message[i])
151.        i += keyLength
152.    return ''.join(letters)
153.
154.
155. def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
156.    # Определяем наиболее вероятные буквы для каждого подключа
157.    ciphertextUp = ciphertext.upper()
158.    # allFreqScores - список длиной mostLikelyKeyLength,
159.    # элементами которого являются списки freqScores
160.    allFreqScores = []
161.    for nth in range(1, mostLikelyKeyLength + 1):
162.        nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength,
163.            ciphertextUp)
164.        # freqScores - список кортежей вида [(<буква>,
165.        # <оценка частотного соответствия>), ... ]. Список сортируется
166.        # по оценкам: чем выше, тем лучше. См. комментарии к функции
167.        # englishFreqMatchScore() в модуле freqAnalysis.py.
168.        freqScores = []
169.        for possibleKey in LETTERS:
170.            decryptedText = vigenereCipher.decryptMessage(possibleKey,
171.                nthLetters)
172.            keyAndFreqMatchTuple = (possibleKey,
173.                freqAnalysis.englishFreqMatchScore(decryptedText))
174.            freqScores.append(keyAndFreqMatchTuple)