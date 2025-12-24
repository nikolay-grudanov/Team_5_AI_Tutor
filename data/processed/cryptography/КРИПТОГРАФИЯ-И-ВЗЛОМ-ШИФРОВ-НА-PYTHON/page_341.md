---
source_image: page_341.png
page_number: 341
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.42
tokens: 7541
characters: 1769
timestamp: 2025-12-24T08:54:30.325843
finish_reason: stop
---

Исходный код программы Frequency Analysis

Откройте в редакторе файлов новое окно, выбрав пункты меню File→New File. Введите в этом окне приведенный ниже код и сохраните его в файле freqAnalysis.py. Запустите программу, нажав клавишу <F5>.

freqAnalysis.py

1. # Определение частотности букв
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
5. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
6.
7. def getLetterCount(message):
8.     # Возвращает словарь, ключами которого являются буквы,
9.     # а значениями - частотность каждой буквы в строке message
10.    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
11.         'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
12.         'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
13.         'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
14.    for letter in message.upper():
15.        if letter in LETTERS:
16.            letterCount[letter] += 1
17.    return letterCount
18.
19. def getItemAtIndexZero(items):
20.    return items[0]
21.
22.
23. def getFrequencyOrder(message):
24.     # Возвращает строку букв алфавита, расположенных в порядке
25.     # убывания их частотности в строке message.
26.
27.     # Во-первых, получаем словарь частотности букв
28.     letterToFreq = getLetterCount(message)
29.
30.     # Во-вторых, создаем словарь счетчиков частотности
31.     # со списком букв по каждому счетчику
32.     freqToLetter = {}
33.     for letter in LETTERS:
34.         if letterToFreq[letter] not in freqToLetter:
35.             freqToLetter[letterToFreq[letter]] = [letter]
36.         else:
37.             freqToLetter[letterToFreq[letter]].append(letter)
38.
39.     # В-третьих, изменяем порядок букв в каждом списке на