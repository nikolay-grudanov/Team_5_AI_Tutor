---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.08
tokens: 6561
characters: 2451
timestamp: 2025-12-24T08:09:43.128713
finish_reason: stop
---

Теорема 4.6.1 ( тождество Якоби–Труди ). Пусть \( \delta \) — разбиение вида \( (n-1, n-2, \ldots, 1, 0) \). Тогда

\[
s_{\lambda} = \frac{a_{\lambda+\delta}}{a_{\delta}}, \quad \text{т. е.} \quad |p_{\lambda_i+j-i}|_1^n = \frac{|x_i^{\lambda_j+n-j}|_1^n}{|x_i^{n-j}|_1^n}.
\]

Доказательство. Пусть \( \alpha = (\alpha_1, \ldots, \alpha_n) \) — некоторое разбиение. Рассмотрим матрицы \( A_{\alpha} = \| x_j^{\alpha_i} \|_1^n \) и \( H_{\alpha} = \| p_{\alpha_i-n+j} \|_1^n \). Рассмотрим также матрицу \( M = \| (-1)^{n-i} \sigma_{n-i}(\hat{x}_j) \|_1^n \), где \( \hat{x}_j = (x_1, \ldots, x_{j-1}, x_{j+1}, \ldots, x_n) \). Покажем, что эти три матрицы связаны соотношением

\[
H_{\alpha} M = A_{\alpha}.
\] (1)

Пусть

\[
\sigma^{(j)}(t) = \sum_{k=0}^{n-1} \sigma_k(\hat{x}_j)t^k = \frac{1}{(1+x_l t)} \quad \text{и} \quad p(t) = \sum_{k=0}^{\infty} p_k t^k = \frac{1}{(1-x_l t)^{-1}}.
\]

Тогда

\[
p(t)\sigma^{(j)}(-t) = (1 - x_j t)^{-1}.
\]

Сравнивая коэффициенты при \( t^{\alpha_i} \) в обеих частях этого равенства, получаем

\[
\sum_{l=1}^n p_{\alpha_i-n+l}(-1)^{n-l} \sigma_{n-l}(\hat{x}_j) = x_j^{\alpha_i}.
\]

Это и есть требуемое соотношение (1).

Из (1), в частности, следует, что

\[
\det H_{\alpha} \det M = \det A_{\alpha}.
\] (2)

Чтобы вычислить \( \det M \), положим \( \alpha = \delta = (n-1, n-2, \ldots, 1, 0) \). В таком случае матрица \( H_{\alpha} \) имеет вид \( \| p_{j-i} \|_i^n \). Эта матрица треугольная с элементами \( p_0 = 1 \) на диагонали. Поэтому \( \det H_{\delta} = 1 \), а значит, \( \det M = \det A_{\delta} = a_{\delta} \). А так как \( \det H_{\alpha} = s_{\alpha-\delta} \), то при \( \alpha = \lambda + \delta \) равенство (2) принимает вид \( s_{\lambda} a_{\delta} = a_{\lambda+\delta} \), т. е. \( s_{\lambda} = a_{\lambda+\delta}/a_{\delta} \).

Теорема 4.6.2. Любой симметрический многочлен с вещественными коэффициентами однозначно представляется в виде \( \bullet \ t_{\lambda} s_{\lambda} \), \( t_{\lambda} \in \mathbb{R} \). При этом если коэффициенты многочлена целые, то \( t_{\lambda} \in \mathbb{Z} \).

Доказательство. Согласно теореме 4.2.2 отображение \( f \mapsto a_{\delta} f \) устанавливает взаимно однозначное соответствие между симметрическими и кососимметрическими многочленами. Поэтому согласно тождеству Якоби–Труди достаточно проверить, что любой кососимметрический многочлен однозначно представляется в виде \( \bullet \ t_{\lambda} a_{\lambda+\delta} \), но это очевидно.