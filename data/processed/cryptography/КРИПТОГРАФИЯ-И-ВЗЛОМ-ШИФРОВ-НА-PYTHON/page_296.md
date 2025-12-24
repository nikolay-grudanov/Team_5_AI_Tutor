---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.78
tokens: 7344
characters: 1769
timestamp: 2025-12-24T08:53:12.663379
finish_reason: stop
---

```python
intersectedMapping[letter].append(mappedLetter)
return intersectedMapping

def removeSolvedLettersFromMapping(letterMapping):
    # Шифробуквы, транслируемые только в одну букву, считаются дешифрованными, и соответствующие буквы могут быть удалены из остальных списков. Например, если 'A' транслируется в ['M', 'N'], а 'B' - в ['N'], то мы знаем, что 'B' соответствует 'N', поэтому 'N' можно удалить из списка для 'A'. Это также означает, что 'A' транслируется в ['M']. А поскольку 'A' теперь соответствует единственной букве, можно удалить 'M' из остальных списков (вот почему словарь сокращается в цикле).
loopAgain = True
while loopAgain:
    # Сначала предполагаем, что цикл не будет выполнен повторно
    loopAgain = False
    solvedLetters = []
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            solvedLetters.append(letterMapping[cipherletter][0])
    # Если буква установлена, то она не может быть вариантом дешифрования для другой шифробуквы, поэтому она должна быть удалена из других списков
    for cipherletter in LETTERS:
        for s in solvedLetters:
            if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                letterMapping[cipherletter].remove(s)
                if len(letterMapping[cipherletter]) == 1:
                    # Дешифрована новая буква, продолжаем цикл
                    loopAgain = True
return letterMapping

def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Получить новый дешифровальный словарь для каждого шифрослова
        candidateMap = getBlankCipherletterMapping()
```