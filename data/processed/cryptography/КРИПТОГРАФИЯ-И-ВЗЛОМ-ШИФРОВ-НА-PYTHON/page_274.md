---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.38
tokens: 7519
characters: 1999
timestamp: 2025-12-24T08:52:51.834348
finish_reason: stop
---

Чтобы зашифровать сообщение, найдите букву открытого текста в верхнем ряду и подставьте вместо нее соответствующую букву из нижнего ряда. Таким образом, 'A' превращается в 'V', 'T' — в 'C', 'C' — в 'Z' и т.д. В результате сообщение "Attack at dawn." шифруется как "Vccvzi vc bvax.".

Чтобы расшифровать зашифрованное сообщение, найдите букву из шифротекста в нижнем ряду и замените ее соответствующей буквой из верхнего ряда. Таким образом, 'V' превращается в 'A', 'C' — в 'T', 'Z' — в 'C' и т.д.

В отличие от шифра Цезаря, в котором нижний ряд сдвинут, но сохраняет прежний алфавитный порядок, в простом подстановочном шифре нижний ряд полностью перемешан. Как следствие, количество возможных ключей резко возрастает, что дает огромные преимущества. Недостаток лишь один: запомнить ключ длиной 26 символов намного сложнее. Вероятно, ключ придется записать, но в таком случае необходимо позаботиться о том, чтобы никто не смог его прочитать!

Исходный код программы Simple Substitution Cipher

Откройте в редакторе файлов новое окно, выбрав пункты меню File⇒New File. Введите в этом окне приведенный ниже код и сохраните его в файле simpleSubCipher.py. Убедитесь в том, что файл pyperclip.py находится в той же самой папке. Запустите программу, нажав клавишу <F5>.

simpleSubCipher.py

1. # Простой подстановочный шифр
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip, sys, random
5.
6.
7. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
8.
9. def main():
10.     myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
11.     myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
12.     myMode = 'encrypt'  # задать 'encrypt' или 'decrypt'