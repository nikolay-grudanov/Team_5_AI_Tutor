---
source_image: page_335.png
page_number: 335
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.24
tokens: 6413
characters: 2171
timestamp: 2025-12-24T08:16:45.053489
finish_reason: stop
---

Оказывается, что при \( p \geq 3 \) неверны свойства, сформулированные в следствиях 1 и 2. Но прежде чем перейти к изучению свойств тензорного ранга, расскажем, чем был вызван интерес к нему.

**33.2. Алгоритм Штрассена**

В пространстве матриц порядка \( n \) выберем базис \( e_{\alpha \beta} = \| \delta_{i \alpha} \delta_{j \beta} \|_1^n \); пусть \( \varepsilon_{\alpha \beta} \) — двойственный базис. Тогда \( A = \bullet_{i,j} a_{ij} e_{ij}, B = \bullet_{i,j} b_{ij} e_{ij} \) и
\[
AB = \bullet_{i,j,k} a_{ik} b_{kj} e_{ij} = \bullet_{i,j,k} \varepsilon_{ik}(A) \varepsilon_{kj}(B) e_{ij}.
\]
Таким образом, вычисление произведения двух матриц порядка \( n \) сводится к вычислению \( n^3 \) произведений линейных функций \( \varepsilon_{ik}(A) \varepsilon_{kj}(B) \). Но является ли число \( n^3 \) минимальным? Оказывается, что нет. Например, для матриц порядка 2 можно указать 7 пар линейных функций \( f_p \) и \( g_p \) и 7 матриц \( E_p \), для которых \( AB = \bullet_{p=1}^7 f_p(A) g_p(B) E_p \). Это разложение было построено в работе [St1]. Вычисление наименьшего числа таких троек \( (f_p, g_p, E_p) \) эквивалентно вычислению ранга тензора
\[
\bullet_{i,j,k} \varepsilon_{ik} \otimes \varepsilon_{kj} \otimes e_{ij} = \bullet_p f_p \otimes g_p \otimes E_p.
\]

Отождествим векторы и ковекторы и введём для краткости обозначения \( a = e_{11}, b = e_{12}, c = e_{21} \) и \( d = e_{22} \). Тогда для матриц порядка 2 получаем
\[
\bullet_{i,j,k} \varepsilon_{ik} \otimes \varepsilon_{kj} \otimes e_{ij} = (a \otimes a + b \otimes c) \otimes a + (a \otimes b + b \otimes d) \otimes b +
+ (c \otimes a + d \otimes c) \otimes c + (c \otimes b + d \otimes d) \otimes d.
\]
Разложение Штрассена имеет вид
\[
\bullet_{i,j,k} \varepsilon_{ik} \otimes \varepsilon_{kj} \otimes e_{ij} = \bullet_{p=1}^7 T_p,
\]
где
\[
\begin{align*}
T_1 &= (a - d) \otimes (a - d) \otimes (a + d), & T_2 &= d \otimes (a + c) \otimes (a + c), \\
T_3 &= (a - b) \otimes d \otimes (a - b), & T_4 &= a \otimes (b + d) \otimes (b + d), \\
T_5 &= (c - d) \otimes a \otimes (c - d), & T_6 &= (b - d) \otimes (c + d) \otimes a, \\
T_7 &= (c - a) \otimes (a + b) \otimes d.
\end{align*}
\]