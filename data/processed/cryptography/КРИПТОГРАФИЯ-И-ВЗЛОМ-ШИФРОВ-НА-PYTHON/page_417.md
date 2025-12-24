---
source_image: page_417.png
page_number: 417
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.51
tokens: 7479
characters: 1665
timestamp: 2025-12-24T08:56:34.047688
finish_reason: stop
---

55. # Делим s на 2 до тех пор, пока не получим нечетное
56. # число (используя t для подсчета таких делений)
57. s = s // 2
58. t += 1
59. for trials in range(5): # пытаемся фальсифицировать проверку простоты числа num 5 раз
60.     a = random.randrange(2, num - 1)
61.     v = pow(a, s, num)
62.     if v != 1: # тест неприменим, если v равно 1
63.         i = 0
64.         while v != (num - 1):
65.             if i == t - 1:
66.                 return False
67.             else:
68.                 i = i + 1
69.                 v = (v ** 2) % num
70.     return True
71.
72. # Обычно можно быстро определить, что num не является простым числом,
73. # разделив его на первые несколько десятков простых чисел. Это быстрее,
74. # чем вызывать функцию rabinMiller(), но годится не всегда.
75. LOW_PRIMES = primeSieve(100)
76.
77.
78. def isPrime(num):
79.     # Возвращает True, если num — простое число. Сначала выполняются
80.     # быстрые проверки перед вызовом функции rabinMiller().
81.     if (num < 2):
82.         return False # 0, 1 и отрицательные числа не являются простыми
83.     # Проверяем, делится ли параметр num на простые числа из списка
84.     for prime in LOW_PRIMES:
85.         if (num == prime):
86.             return True
87.         if (num % prime == 0):
88.             return False
89.     # В остальных случаях вызываем функцию rabinMiller()
90.     return rabinMiller(num)
91.
92.
93. def generateLargePrime(keysize=1024):
94.     # Возвращает случайное простое число размером keysize бит
95.     while True:
96.         num = random.randrange(2**(keysize-1), 2**(keysize))
97.         if isPrime(num):
98.             return num