---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.54
tokens: 7309
characters: 1558
timestamp: 2025-12-24T08:51:24.058444
finish_reason: stop
---

32. decryptedText = transpositionDecrypt.decryptMessage(key, message)
33.
34. if detectEnglish.isEnglish(decryptedText):
35.     # Запросить у пользователя подтверждение корректности ключа
36.     print()
37.     print('Possible encryption hack:')
38.     print('Key %s: %s' % (key, decryptedText[:100]))
39.     print()
40.     print('Enter D if done, anything else to continue hacking:')
41.     response = input('>')
42.
43.     if response.strip().upper().startswith('D'):
44.         return decryptedText
45.
46. return None
47.
48. if __name__ == '__main__':
49.     main()

Пример выполнения программы Transposition Hacker

Выполнив программу transpositionHacker.py, вы должны получить следующие результаты.

Hacking...
(Press Ctrl-C (on Windows) or Ctrl-D (on macOS and Linux) to quit at any time.)
Trying key #1...
Trying key #2...
Trying key #3...
Trying key #4...
Trying key #5...
Trying key #6...

Possible encryption hack:
Key 6: Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 – 27 November 1852) was an English mat

Enter D if done, anything else to continue hacking:
> D
Copying hacked message to clipboard:
Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 – 27 November 1852) was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognised as the first algorithm intended to be carried out by a machine. As a result, she is often regarded as the first computer programmer.