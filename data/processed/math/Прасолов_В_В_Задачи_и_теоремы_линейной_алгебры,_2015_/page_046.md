---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.73
tokens: 6436
characters: 2007
timestamp: 2025-12-24T08:08:43.897216
finish_reason: stop
---

Теорема 2.3.1 (формула Бине–Коши). Пусть \( A \) и \( B \) — матрицы размера \( n \times m \) и \( m \times n \) соответственно, причём \( n \leq m \). Тогда

\[
\det AB = \sum_{1 \leq k_1 < \ldots < k_n \leq m} A_{k_1 \ldots k_n} B^{k_1 \ldots k_n},
\]

где \( A_{k_1 \ldots k_n} \) — минор, полученный из столбцов матрицы \( A \) с номерами \( k_1, \ldots, k_n \), а \( B^{k_1 \ldots k_n} \) — минор, полученный из строк матрицы \( B \) с номерами \( k_1, \ldots, k_n \).

Доказательство. Пусть \( C = AB \), \( c_{ij} = \sum_{k=1}^m a_{ik} b_{kj} \). Тогда

\[
\det C = \sum_{\sigma} (-1)^{\sigma} \cdot a_{1k_1} b_{k_1 \sigma(1)} \cdots \cdot a_{nk_n} b_{k_n \sigma(n)} =
\]
\[
= \sum_{k_1, \ldots, k_n=1}^m a_{1k_1} \ldots a_{nk_n} \sum_{\sigma} (-1)^{\sigma} b_{k_1 \sigma(1)} \ldots b_{k_n \sigma(n)} =
\]
\[
= \sum_{k_1, \ldots, k_n=1}^m a_{1k_1} \ldots a_{nk_n} B^{k_1 \ldots k_n}.
\]

Минор \( B^{k_1 \ldots k_n} \) отличен от нуля, только если числа \( k_1, \ldots, k_n \) попарно различны, поэтому суммирование можно вести по попарно различным \( k_1, \ldots, k_n \). А так как \( B^{\tau(k_1) \ldots \tau(k_n)} = (-1)^{\tau} B^{k_1 \ldots k_n} \) для любой перестановки \( \tau \) чисел \( k_1, \ldots, k_n \), то

\[
\sum_{k_1, \ldots, k_n=1}^n a_{1k_1} \ldots a_{nk_n} B^{k_1 \ldots k_n} = \sum_{k_1 < k_2 < \ldots < k_n} (-1)^{\tau} a_{1\tau(1)} \ldots a_{n\tau(n)} B^{k_1 \ldots k_n} =
\]
\[
= \sum_{1 \leq k_1 < \ldots < k_n \leq m} A_{k_1 \ldots k_n} B^{k_1 \ldots k_n}. \quad \Box
\]

Замечание. Другое доказательство формулы Бине–Коши см. в решении задачи 30.8.

2.4. Алгебраическое дополнение минора

Напомним формулу разложения определителя по \( i \)-й строке:

\[
|a_{ij}|_1^n = \sum_{j=1}^n (-1)^{i+j} a_{ij} M_{ij},
\]

где \( M_{ij} \) — определитель матрицы, полученной из матрицы \( A = |a_{ij}|_1^n \) вычёркиванием \( i \)-й строки и \( j \)-го столбца. Число \( A_{ij} = (-1)^{i+j} M_{ij} \) называют алгебраическим дополнением элемента \( a_{ij} \) в матрице \( A \); ясно,