---
source_image: page_275.png
page_number: 275
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.71
tokens: 7214
characters: 1338
timestamp: 2025-12-24T08:52:39.304447
finish_reason: stop
---

```python
if not keyIsValid(myKey):
    sys.exit('There is an error in the key or symbol set.')
if myMode == 'encrypt':
    translated = encryptMessage(myKey, myMessage)
elif myMode == 'decrypt':
    translated = decryptMessage(myKey, myMessage)
print('Using key %s' % (myKey))
print('The %sed message is:' % (myMode))
print(translated)
pyperclip.copy(translated)
print()
print('This message has been copied to the clipboard.')

def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    return keyList == lettersList

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # Для дешифрования можно использовать тот же самый код,
        # нужно лишь поменять местами строки key и LETTERS
        charsA, charsB = charsB, charsA
    # Цикл по всем символам сообщения
    for symbol in message:
        if symbol.upper() in charsA:
            # Шифрование/дешифрование символа
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
```