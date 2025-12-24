---
source_image: page_336.png
page_number: 336
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.38
tokens: 6750
characters: 2537
timestamp: 2025-12-24T08:16:57.575187
finish_reason: stop
---

Оно приводит к следующему алгоритму вычисления произведения матриц \( A = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix} \) и \( B = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} \):

\[
S_1 = a_1 - d_1, \qquad S_2 = a_2 - d_2, \qquad S_3 = a_1 - b_1,
\]
\[
S_4 = b_1 - d_1, \qquad S_5 = c_2 + d_2, \qquad S_6 = a_2 + c_2,
\]
\[
S_7 = b_2 + d_2, \qquad S_8 = c_1 - d_1, \qquad S_9 = c_1 - a_1, \qquad S_{10} = a_2 + b_2;
\]
\[
P_1 = S_1 S_2, \qquad P_2 = S_3 d_2, \qquad P_3 = S_4 S_5, \qquad P_4 = d_1 S_6,
\]
\[
P_5 = a_1 S_7, \qquad P_6 = S_8 a_2, \qquad P_7 = S_9 S_{10};
\]
\[
S_{11} = P_1 + P_2, \qquad S_{12} = S_{11} + P_3, \qquad S_{13} = S_{12} + P_4,
\]
\[
S_{14} = P_5 - P_2, \qquad S_{15} = P_4 + P_6, \qquad S_{16} = P_1 + P_5,
\]
\[
S_{17} = S_{16} - P_6, \qquad S_{18} = S_{17} + P_7.
\]

Тогда \( AB = \begin{pmatrix} S_{13} & S_{14} \\ S_{15} & S_{18} \end{pmatrix} \). При вычислении \( AB \) по алгоритму Штрассена требуется 7 умножений и 18 сложений (или вычитаний).

**33.3. Тензорный ранг в \( V_1 \otimes V_2 \otimes V_3 \)**

Пусть \( V \) — двумерное пространство с базисом \( \{e_1, e_2\} \). Рассмотрим тензор \( T = e_1 \otimes e_1 \otimes e_1 + e_1 \otimes e_2 \otimes e_2 + e_2 \otimes e_1 \otimes e_2 \).

**Теорема 33.3.1. Ранг тензора \( T \) равен 3, но существует последовательность тензоров ранга не более 2, сходящаяся к \( T \).**

**Доказательство.** Пусть
\[
T_\lambda = \lambda^{-1} [e_1 \otimes e_1 \otimes (-e_2 + \lambda e_1) + (e_1 + \lambda e_2) \otimes (e_1 + \lambda e_2) \otimes e_2].
\]
Тогда \( T_\lambda - T = \lambda e_2 \otimes e_2 \otimes e_2 \), поэтому \( \lim_{\lambda \to 0} |T_\lambda - T| = 0 \).

Предположим, что
\[
T = a \otimes b \otimes c + u \otimes v \otimes w =
\]
\[
= (\alpha_1 e_1 + \alpha_2 e_2) \otimes b \otimes c + (\lambda_1 e_1 + \lambda_2 e_2) \otimes v \otimes w =
\]
\[
= e_1 \otimes (\alpha_1 b \otimes c + \lambda_1 v \otimes w) + e_2 \otimes (\alpha_2 b \otimes c + \lambda_2 v \otimes w).
\]
Тогда \( e_1 \otimes e_1 + e_2 \otimes e_2 = \alpha_1 b \otimes c + \lambda_1 v \otimes w \) и \( e_1 \otimes e_2 = \alpha_2 b \otimes c + \lambda_2 v \otimes w \). Следовательно, линейно независимые тензоры \( b \otimes c \) и \( v \otimes w \) ранга 1 принадлежат пространству \( \langle e_1 \otimes e_1 + e_2 \otimes e_2, e_1 \otimes e_2 \rangle \). Последнее пространство можно отождествить с пространством матриц вида \( \begin{pmatrix} x & y \\ 0 & x \end{pmatrix} \). Но все такие матрицы ранга 1 линейно зависимы. Получено противоречие. □