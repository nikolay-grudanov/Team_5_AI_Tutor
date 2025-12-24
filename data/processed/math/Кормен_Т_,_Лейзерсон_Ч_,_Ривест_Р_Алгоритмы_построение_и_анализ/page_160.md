---
source_image: page_160.png
page_number: 160
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 64.25
tokens: 11644
characters: 1744
timestamp: 2025-12-24T06:27:50.495345
finish_reason: stop
---

Используя это, получим

\[
T(n) \leq \frac{2a}{n} \left( \frac{1}{2} n^2 \lg n - \frac{1}{8} n^2 \right) + \frac{2b}{n}(n-1) + \Theta(n)
\]
\[
\leq an \lg n - \frac{a}{4} n + 2b + \Theta(n)
\]
\[
= an \lg n + b + \left( \Theta(n) + b - \frac{a}{4} n \right) \leq an \lg n + b,
\]

если выбрать \( a \) так, чтобы \( \frac{a}{4} n \) было больше \( \Theta(n) + b \). Следовательно, среднее время работы есть \( O(n \lg n) \).

Доказательство оценки для суммы

Осталось доказать оценку (8.5). Поскольку каждое слагаемое не превышает \( n \lg n \), получаем оценку

\[
\sum_{k=1}^{n-1} k \lg k \leq n^2 \lg n.
\]

Для наших целей она не подходит — нам необходима более точная оценка \( \frac{1}{2} n^2 \lg n - \Omega(n^2) \).

Если в предыдущей оценке заменять лишь \( \lg k \) на \( \lg n \), оставив \( k \) в неприкосновенности, получим оценку

\[
\sum_{k=1}^{n-1} k \lg k \leq \lg n \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2} \lg n \leq \frac{1}{2} n^2 \lg n.
\]

Осталось лишь заметить, что заменяя \( \lg k \) на \( \lg n \), мы прибавили по крайней мере по \( k \cdot 1 \) к каждому слагаемом первой половины суммы (где \( k \leq n/2 \)), всего примерно \( (n/2)^2 / 2 = n^2 / 8 \).

Более формально,

\[
\sum_{k=1}^{n-1} k \lg k = \sum_{k=1}^{\lceil n/2 \rceil - 1} k \lg k + \sum_{k=\lceil n/2 \rceil}^{n-1} k \lg k
\]

При \( k < \lceil n/2 \rceil \) имеем \( \lg k \leq \lg(n/2) = \lg n - 1 \). Поэтому

\[
\sum_{k=1}^{n-1} k \lg k \leq (\lg n - 1) \sum_{k=1}^{\lceil n/2 \rceil - 1} k + \lg n \sum_{k=\lceil n/2 \rceil}^{n-1} k
\]
\[
= \lg n \sum_{k=1}^{n-1} k - \sum_{k=1}^{\lceil n/2 \rceil - 1} k \leq \frac{1}{2} n(n-1) \lg n - \frac{1}{2} \left( \frac{n}{2} - 1 \right) \frac{n}{2}
\]
\[
\leq \frac{1}{2} n^2 \lg n - \frac{1}{8} n^2
\]