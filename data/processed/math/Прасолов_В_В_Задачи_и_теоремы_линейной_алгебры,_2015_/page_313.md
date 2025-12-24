---
source_image: page_313.png
page_number: 313
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.35
tokens: 6525
characters: 2297
timestamp: 2025-12-24T08:16:04.430242
finish_reason: stop
---

§ 30. Симметрические и кососимметрические тензоры

\( e_1^{k_1} \ldots e_n^{k_n} \) и \( e_1^{l_1} \ldots e_n^{l_n} \) являются линейными комбинациями двух непересекающихся подмножеств базисных элементов пространства \( T^q_0(V) \). Для тензоров вида \( e_{i_1} \wedge \ldots \wedge e_{i_q} \) доказательство аналогично.

Следствие. \( \dim \Lambda^q(V) = \binom{n}{q} \) и \( \dim S^q(V) = \binom{n+q-1}{q} \).

Доказательство. Ясно, что количество наборов \( 1 \leq i_1 < \ldots < i_q \leq n \) равно \( \binom{n}{q} \). Для вычисления количества наборов \( k_1 + \ldots + k_n = q \) поступим следующим образом. Каждому такому набору сопоставим последовательность из \( q + n - 1 \) шаров, среди которых \( q \) белых и \( n - 1 \) чёрных; в этой последовательности сначала идёт \( k_1 \) белых шаров, за ними один чёрный, за ним \( k_2 \) белых, за ними один чёрный и т. д. Из \( n + q - 1 \) шаров \( q \) белых шаров можно выбрать \( \binom{n+q-1}{q} \) способами.

30.2. Алгебра Грамсмана

В пространстве
\[
\Lambda(V) = \bigoplus_{q=0}^n \Lambda^q(V)
\]
можно ввести операцию внешнего произведения \( T_1 \wedge T_2 = A(T_1 \otimes T_2) \) для \( T_1 \in \Lambda^p(V) \) и \( T_2 \in \Lambda^q(V) \); на \( \Lambda(V) \) эта операция продолжается по линейности. Полученную алгебру \( \Lambda(V) \) называют внешней алгеброй или алгеброй Грамсмана пространства \( V \).

Теорема 30.2.1. Алгебра \( \Lambda(V) \) ассоциативна и косокоммутативна, т. е. \( T_1 \wedge T_2 = (-1)^{pq} T_2 \wedge T_1 \) для \( T_1 \in \Lambda^p(V) \) и \( T_2 \in \Lambda^q(V) \).

Доказательство. Докажем сначала, что
\[
A(T_1 \otimes T_2) = A(A(T_1) \otimes T_2).
\]
Для этого достаточно рассмотреть случай, когда \( T_1 = x_1 \otimes \ldots \otimes x_p \) и \( T_2 = x_{p+1} \otimes \ldots \otimes x_{p+q} \). Так как
\[
A(x_1 \otimes \ldots \otimes x_p) = \frac{1}{p!} \sum_{\sigma \in S_p} (-1)^{\sigma} x_{\sigma(1)} \otimes \ldots \otimes x_{\sigma(p)},
\]
то
\[
A(A(T_1) \otimes T_2) = A\left( \frac{1}{p!} \sum_{\sigma \in S_p} (-1)^{\sigma} x_{\sigma(1)} \otimes \ldots \otimes x_{\sigma(p)} \otimes x_{p+1} \otimes \ldots \otimes x_{p+q} \right) =
\]
\[
= \frac{1}{p! (p+q)!} \sum_{\sigma \in S_p} \sum_{\tau \in S_{p+q}} (-1)^{\sigma \tau} x_{\tau(\sigma(1))} \otimes \ldots \otimes x_{\tau(p+q)}.
\]