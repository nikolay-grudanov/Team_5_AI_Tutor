---
source_image: page_360.png
page_number: 360
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.75
tokens: 7301
characters: 1526
timestamp: 2025-12-24T08:54:57.742551
finish_reason: stop
---

7. ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz.""""
8. hackedMessage = hackVigenereDictionary(ciphertext)
9.
10. if hackedMessage != None:
11.     print('Copying hacked message to clipboard:')
12.     print(hackedMessage)
13.     pyperclip.copy(hackedMessage)
14. else:
15.     print('Failed to hack encryption.')
16.
17.
18. def hackVigenereDictionary(ciphertext):
19.     fo = open('dictionary.txt')
20.     words = fo.readlines()
21.     fo.close()
22.
23.     for word in words:
24.         word = word.strip()  # удалить завершающий символ новой строки
25.         decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
26.         if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
27.             # Спросить у пользователя, найден ли ключ дешифрования
28.             print()
29.             print('Possible encryption break:')
30.             print('Key ' + str(word) + ': ' + decryptedText[:100])
31.             print()
32.             print('Enter D for done, or just press Enter to continue breaking:')
33.             response = input('>')
34.             if response.upper().startswith('D'):
35.                 return decryptedText
36.
37.
38. if __name__ == '__main__':
39.     main()

Пример выполнения программы Vigenere Dictionary Hacker

Выполнив программу, вы должны получить следующий результат.

Possible encryption break:
Key ASTROLOGY: The recl yecrets crk not the qnks I tell.

Enter D for done, or just press Enter to continue breaking:
>

Possible encryption break: