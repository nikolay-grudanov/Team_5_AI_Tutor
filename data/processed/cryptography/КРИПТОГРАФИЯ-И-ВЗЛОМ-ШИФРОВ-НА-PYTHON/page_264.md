---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.88
tokens: 7518
characters: 1767
timestamp: 2025-12-24T08:52:36.547049
finish_reason: stop
---

33. for key in range(len(affineCipher.SYMBOLS) ** 2):
34.     keyA = affineCipher.getKeyParts(key)[0]
35.     if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) !=1:
36.         continue
37.
38.     decryptedText = affineCipher.decryptMessage(key, message)
39.     if not SILENT_MODE:
40.         print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
41.
42.     if detectEnglish.isEnglish(decryptedText):
43.         # Подтвердить, что найден правильный ключ
44.         print()
45.         print('Possible encryption hack:')
46.         print('Key: %s' % (key))
47.         print('Decrypted message: ' + decryptedText[:200])
48.         print()
49.         print('Enter D if done, anything else to continue hacking:')
50.         response = input('>')
51.
52.     if response.strip().upper().startswith('D'):
53.         return decryptedText
54. return None

57. # Если файл affineHacker.py выполняется как программа
58. # (а не импортируется как модуль), вызвать функцию main():
59. if __name__ == '__main__':
60.     main()

Пример выполнения программы Affine Hacker

Запустите программу, нажав клавишу <F5>. Вы должны получить примерно следующее.

Hacking...
(Press Ctrl-C or Ctrl-D to quit at any time.)
Tried Key 66... ("5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQA)
Tried Key 67... ("4PF8nk2KZ5PH82 wPwZhZ5eZPK8PcZPFz ZwP.)
Tried Key 68... ("3OE7mj1JY4OG710vOvYgY4dYOJ7ObYOEy00YvO?)
--опущено--
Tried Key 2892... ("UQw970A.y!QC9A6xQxy?y!ByQ.9QvyQwu66yxQ3)
Tried Key 2893... ("rnFRPSXWHUnZRXOGnGHVHUYHnWRnEHnFDOOHGnL)
Tried Key 2894... ("A computer would deserve to be called i)

Possible encryption hack:
Key: 2894
Decrypted message: "A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing