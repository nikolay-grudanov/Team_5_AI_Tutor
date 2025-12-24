---
source_image: page_488.png
page_number: 488
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.94
tokens: 6424
characters: 1915
timestamp: 2025-12-24T08:20:50.814680
finish_reason: stop
---

Теорема 55.1.2. Для любого многочлена \( f(x) = x^n + c_1 x^{n-1} + \ldots + c_n \) и любой матрицы \( B \) порядка \( n - 1 \), характеристический многочлен которой совпадает с минимальным многочленом, существует такая матрица \( A \), что \( B \) является подматрицей \( A \) и характеристический многочлен \( A \) равен \( f \).

Доказательство [Fa2]. Пусть \( A = \begin{pmatrix} B & P \\ Q^T & b \end{pmatrix} \), где \( P \) и \( Q \) — произвольные столбцы длиной \( n - 1 \), \( b \) — произвольное число. Ясно, что
\[
\det (xI_n - A) = (x - b) \det (xI_{n-1} - B) - Q^T \operatorname{adj}(xI_{n-1} - B)P
\]
(см. теорему 3.1.3). Докажем, что
\[
\operatorname{adj}(xI_{n-1} - B) = \sum_{r=0}^{n-2} u_r(x) B^r,
\]
где многочлены \( u_0, \ldots, u_{n-2} \) образуют базис пространства многочленов степени не более \( n - 2 \). Пусть \( g(x) = \det(xI_{n-1} - B) = x^{n-1} + t_1 x^{n-2} + \ldots \) и \( \varphi(x, \lambda) = (g(x) - g(\lambda))/(x - \lambda) \). Тогда
\[
(xI_{n-1} - B) \varphi(x, B) = g(x) I_{n-1} - g(B) = g(x) I_{n-1},
\]
так как по теореме Гамильтона—Кэли \( g(B) = 0 \). Поэтому
\[
\varphi(x, B) = g(x)(xI_{n-1} - B)^{-1} = \operatorname{adj}(xI_{n-1} - B).
\]
Кроме того, так как \( (x^k - \lambda^k)/(x - \lambda) = \sum_{s=0}^{k-1} x^{k-1-s} \lambda^s \), то
\[
\varphi(x, \lambda) = \sum_{r=0}^{n-2} t_{n-r-2} \sum_{s=0}^r x^{r-s} \lambda^s = \sum_{s=0}^{n-2} \lambda^s \sum_{r=s}^{n-2} t_{n-r-2} x^{r-s},
\]
а значит,
\[
\varphi(x, \lambda) = \sum_{s=0}^{n-2} \lambda^s u_s(x),
\]
где \( u_s = x^{n-s-2} + t_1 x^{n-s-3} + \ldots + t_{n-s-2} \). Итак,
\[
\det(xI_n - A) = (x - b)(x^{n-1} + t_1 x^{n-2} + \ldots) - \sum_{s=0}^{n-2} u_s Q^T B^s P =
\]
\[
= x^n + (t_1 - b)x^{n-1} + h(x) - \sum_{s=0}^{n-2} u_s Q^T B^s P,
\]
где \( h \) — многочлен степени не более \( n - 2 \) и многочлены \( u_0, \ldots, u_{n-2} \) образуют базис пространства многочленов степени не более \( n - 2 \).