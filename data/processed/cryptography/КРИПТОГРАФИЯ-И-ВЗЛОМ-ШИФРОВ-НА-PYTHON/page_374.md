---
source_image: page_374.png
page_number: 374
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.42
tokens: 7518
characters: 1997
timestamp: 2025-12-24T08:55:25.212679
finish_reason: stop
---

218.
219.    # Получить осмысленный текст не удалось, поэтому возвращаем None
220.    return None
221.
222.
223. def hackVigenere(ciphertext):
224.    # Прежде всего, необходимо применить метод Касиски
225.    # для выяснения возможной длины ключа
226.    allLikelyKeyLengths = kasiskiExamination(ciphertext)
227.    if not SILENT_MODE:
228.        keyLengthStr = ''
229.        for keyLength in allLikelyKeyLengths:
230.            keyLengthStr += '%s ' % (keyLength)
231.        print('Kasiski examination results say the most likely key lengths are: ' + keyLengthStr + '\n')
232.    hackedMessage = None
233.    for keyLength in allLikelyKeyLengths:
234.        if not SILENT_MODE:
235.            print('Attempting hack with key length %s (%s possible keys) ...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
236.        hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
237.        if hackedMessage != None:
238.            break
239.
240.    # Если ни один из найденных с помощью метода Касиски вариантов длины ключа не сработал, начать атаку методом грубой силы
241.    if hackedMessage == None:
242.        if not SILENT_MODE:
243.            print('Unable to hack message with likely key length(s). Brute-forcing key length...')
244.        for keyLength in range(1, MAX_KEY_LENGTH + 1):
245.            # Не перепроверять длину ключа, уже опробованную методом Касиски
246.            if keyLength not in allLikelyKeyLengths:
247.                if not SILENT_MODE:
248.                    print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
249.            hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
250.            if hackedMessage != None:
251.                break
252.        return hackedMessage
253.
254.
255. # Если файл vigenereHacker.py выполняется как программа
256. # (а не импортируется как модуль), вызвать функцию main():
257. if __name__ == '__main__':
258.     main()