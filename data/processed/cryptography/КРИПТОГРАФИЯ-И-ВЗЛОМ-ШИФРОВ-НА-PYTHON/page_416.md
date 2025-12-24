---
source_image: page_416.png
page_number: 416
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.27
tokens: 7401
characters: 1399
timestamp: 2025-12-24T08:56:31.221557
finish_reason: stop
---

7. def isPrimeTrialDiv(num):
8.     # Возвращает True, если num - простое число, иначе - False
9.
10.    # Использует алгоритм перебора делителей для проверки простоты числа
11.
12.    # Числа, меньше 2, не являются простыми
13.    if num < 2:
14.        return False
15.
16.    # Проверяем делимость на целые числа вплоть до квадратного корня из num
17.    for i in range(2, int(math.sqrt(num)) + 1):
18.        if num % i == 0:
19.            return False
20.    return True

23. def primeSieve(sieveSize):
24.     # Возвращает список простых чисел, вычисленных с помощью решета Эратосфена
25.
26.    sieve = [True] * sieveSize
27.    sieve[0] = False  # 0 и 1 не являются простыми числами
28.    sieve[1] = False
29.
30.    # Создаем решето
31.    for i in range(2, int(math.sqrt(sieveSize)) + 1):
32.        pointer = i * 2
33.        while pointer < sieveSize:
34.            sieve[pointer] = False
35.            pointer += i
36.
37.    # Формируем список простых чисел
38.    primes = []
39.    for i in range(sieveSize):
40.        if sieve[i] == True:
41.            primes.append(i)
42.
43.    return primes

46. def rabinMiller(num):
47.     # Возвращает True, если num - простое число
48.     if num % 2 == 0 or num < 2:
49.         return False  # тест не работает для четных чисел
50.     if num == 3:
51.         return True
52.     s = num - 1
53.     t = 0
54.     while s % 2 == 0: