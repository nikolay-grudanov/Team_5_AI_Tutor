---
source_image: page_436.png
page_number: 436
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.05
tokens: 7507
characters: 1787
timestamp: 2025-12-24T08:57:04.839849
finish_reason: stop
---

Обратите внимание на то, что число \( n \) используется в обоих ключах. Число \( d \) должно храниться в тайне, поскольку оно позволяет дешифровывать сообщения. Теперь все готово для написания программы, которая будет генерировать эти ключи.

Исходный код программы Make Public Private Keys

Откройте в редакторе файлов новое окно, выбрав пункты меню File⇒New File. Введите в этом окне приведенный ниже код и сохраните его в файле makePublicPrivateKeys.py. Убедитесь в том, что модули primeNum.py и cryptomath.py находятся в той же самой папке.

makePublicPrivateKeys.py

1. # Генератор ключей для программы шифрования с открытым ключом
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import random, sys, os, primeNum, cryptomath
5.
6.
7. def main():
8.     # Создаем пару "открытый/закрытый ключ", используя 1024-битовые ключи
9.     print('Making key files...')
10.    makeKeyFiles('al_sweigart', 1024)
11.    print('Key files made.')
12.
13. def generateKey(keySize):
14.     # Создает открытый и закрытый ключи длиной keySize бит
15.     p = 0
16.     q = 0
17.     # Шаг 1: создаем два простых числа p and q и вычисляем n = p * q
18.     print('Generating p & q primes...')
19.     while p == q:
20.         p = primeNum.generateLargePrime(keySize)
21.         q = primeNum.generateLargePrime(keySize)
22.         n = p * q
23.
24.     # Шаг 2: создаем число e, взаимно простое с (p-1)*(q-1)
25.     print('Generating e that is relatively prime to (p-1)*(q-1)...')
26.     while True:
27.         # Перебираем случайные числа для e, пока не найдем допустимое
28.         e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
29.         if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
30.             break
31.
32.     # Шаг 3: вычисляем d - модульное обращение e