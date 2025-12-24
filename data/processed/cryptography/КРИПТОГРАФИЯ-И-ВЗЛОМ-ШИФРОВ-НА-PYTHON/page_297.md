---
source_image: page_297.png
page_number: 297
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.96
tokens: 7297
characters: 1621
timestamp: 2025-12-24T08:53:10.871693
finish_reason: stop
---

wordPattern = makeWordPatterns.getWordPattern(cipherword)
if wordPattern not in wordPatterns.allPatterns:
    continue # этого слова нет в словаре, продолжаем
# Добавить буквы каждого слова-кандидата в словарь
for candidate in wordPatterns.allPatterns[wordPattern]:
    addLettersToMapping(candidateMap, cipherword, candidate)
# Найти пересечение нового словаря с существующим пересечением
intersectedMap = intersectMappings(intersectedMap, candidateMap)
# Удалить решенные буквы из других списков
return removeSolvedLettersFromMapping(intersectedMap)

def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Возвращает строку шифротекста, дешифрованную с помощью словаря шифробукв, в которой неоднозначности заменены подчеркиваниями
    # Сначала создаем ключ на основе словаря letterMapping
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # Если имеется только одна буква, добавляем ее в ключ
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)
    # Дешифруем шифротекст с помощью созданного ключа
    return simpleSubCipher.decryptMessage(key, ciphertext)

if __name__ == '__main__':
    main()

Пример выполнения программы Simple Substitution Hacker

Когда вы запустите программу, она попытается взломать шифротекст, хранящийся в переменной message. Вы должны получить следующий результат.