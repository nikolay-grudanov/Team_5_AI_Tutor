---
source_image: page_373.png
page_number: 373
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.03
tokens: 7351
characters: 1809
timestamp: 2025-12-24T08:55:14.117495
finish_reason: stop
---

```python
# Сортировка по оценкам частотного соответствия
freqScores.sort(key=getItemAtIndexOne, reverse=True)
allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

if not SILENT_MODE:
    for i in range(len(allFreqScores)):
        # Используем i + 1, чтобы первая буква не считалась 0-й
        print('Possible letters for letter %s of the key:' % (i + 1), end='')
        for freqScore in allFreqScores[i]:
            print('%s ' % freqScore[0], end='')
        print()  # переход на новую строку

# Проверяем все комбинации наиболее вероятных букв
# для каждой позиции в ключе
for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
    # Создаем возможный ключ из букв в списке allFreqScores
    possibleKey = ''
    for i in range(mostLikelyKeyLength):
        possibleKey += allFreqScores[i][indexes[i]][0]
    if not SILENT_MODE:
        print('Attempting with key: %s' % (possibleKey))
    decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)
    if detectEnglish.isEnglish(decryptedText):
        # Задаем исходный регистр букв во взломанном шифротексте
        origCase = []
        for i in range(len(ciphertext)):
            if ciphertext[i].isupper():
                origCase.append(decryptedText[i].upper())
            else:
                origCase.append(decryptedText[i].lower())
        decryptedText = ''.join(origCase)
        # Спросить у пользователя, найден ли ключ дешифрования
        print('Possible encryption hack with key %s:' % (possibleKey))
        print(decryptedText[:200])  # выводим первые 200 символов
        print()
        print('Enter D if done, anything else to continue hacking:')
        response = input('> ')
        if response.strip().upper().startswith('D'):
            return decryptedText
```