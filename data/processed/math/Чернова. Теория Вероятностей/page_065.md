---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 68.98
tokens: 11899
characters: 2568
timestamp: 2025-12-24T08:27:49.590810
finish_reason: stop
---

Показательное распределение не устойчиво по суммированию, однако его можно считать частным случаем гамма-распределения, которое уже в некотором смысле устойчиво относительно суммирования.

**Определение 38.** Случайная величина \( \xi \) имеет *гамма-распределение* \( \Gamma_{\alpha,\lambda} \) с параметрами \( \alpha > 0, \lambda > 0 \), если она имеет плотность распределения

\[
f_{\xi}(x) = \begin{cases}
0, & \text{при } x \leq 0, \\
c \cdot x^{\lambda-1} e^{-\alpha x}, & \text{при } x > 0,
\end{cases}
\]

где постоянная \( c \) вычисляется из условия \( \int_{-\infty}^{\infty} f_{\xi}(x) \, dx = c \int_{0}^{\infty} x^{\lambda-1} e^{-\alpha x} \, dx = 1 \),

то есть \( c = \frac{\alpha^{\lambda}}{\Gamma(\lambda)} \).

Здесь \( \Gamma(\lambda) = \int_{0}^{\infty} x^{\lambda-1} e^{-x} \, dx = (\lambda - 1)\Gamma(\lambda - 1) \) — *гамма-функция Эйлера*, при \( k \) целых \( \Gamma(k) = (k-1)! \) и \( \Gamma(1) = 1 \).

Заметим, что показательное распределение \( E_{\alpha} \) есть гамма-распределение \( \Gamma_{\alpha,1} \).

**Лемма 7.** *Пусть независимые случайные величины \( \xi_1, \ldots, \xi_n \) имеют показательное распределение \( E_{\alpha} = \Gamma_{\alpha,1} \). Тогда \( \xi_1 + \cdots + \xi_n \in \Gamma_{\alpha,n} \).*

**Доказательство.** Докажем утверждение по индукции. При \( n = 1 \) оно верно в силу равенства \( E_{\alpha} = \Gamma_{\alpha,1} \). Пусть утверждение леммы справедливо для \( n = k - 1 \). Докажем, что оно верно и для \( n = k \). По предположению индукции \( S_{k-1} = \xi_1 + \cdots + \xi_{k-1} \in \Gamma_{\alpha,k-1} \), то есть имеет плотность распределения

\[
f_{S_{k-1}}(x) = \begin{cases}
0, & \text{при } x \leq 0, \\
\frac{\alpha^{k-1}}{(k-2)!} \cdot x^{k-2} e^{-\alpha x}, & \text{при } x > 0.
\end{cases}
\]

Тогда по формуле свертки плотность суммы \( S_k = \xi_1 + \cdots + \xi_k \) равна

\[
f_{S_k}(x) = \int_{-\infty}^{\infty} f_{S_{k-1}}(u) f_{\xi_k}(x-u) \, du = \int_{0}^{\infty} \frac{\alpha^{k-1}}{(k-2)!} \cdot u^{k-2} e^{-\alpha u} f_{\xi_k}(x-u) \, du.
\]

Так как \( f_{\xi_k}(x-u) = 0 \) при \( x-u < 0 \), то есть при \( u > x \), то плотность под интегралом отлична от нуля, если переменная интегрирования изменяется в пределах \( 0 \leq u \leq x \). Поэтому

\[
f_{S_k}(x) = \int_{0}^{x} \frac{\alpha^{k-1}}{(k-2)!} \cdot u^{k-2} e^{-\alpha u} \cdot \alpha e^{-\alpha(x-u)} \, du = e^{-\alpha x} \int_{0}^{x} \frac{\alpha^k}{(k-2)!} \cdot u^{k-2} \, du = \frac{\alpha^k}{(k-1)!} \cdot x^{k-2} e^{-\alpha x}.
\]

То есть \( S_k \in \Gamma_{\alpha,k} \), что и требовалось доказать. □