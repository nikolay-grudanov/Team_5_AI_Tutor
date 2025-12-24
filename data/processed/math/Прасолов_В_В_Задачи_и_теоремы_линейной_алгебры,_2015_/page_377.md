---
source_image: page_377.png
page_number: 377
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.96
tokens: 6855
characters: 3163
timestamp: 2025-12-24T08:18:06.885597
finish_reason: stop
---

вид

\[
\begin{pmatrix}
0 & A_{12} & 0 & \ldots & 0 \\
0 & 0 & A_{23} & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & A_{k-1, k} \\
A_{k1} & 0 & 0 & \ldots & 0
\end{pmatrix}.
\]

Доказательство. Наибольшие по модулю собственные значения матрицы \( A \) имеют вид \( \alpha_j = r \exp(i \varphi_j) \). Применив теорему 40.2.2 к матрице \( B = A \), получим \( A = \exp(i \varphi_j) \cdot D_j A D_j^{-1} \). Поэтому \( p(t) = |A - tI| = |\exp(i \varphi_j) \cdot D_j A D_j^{-1} - tI| = \lambda p(\exp(-i \varphi_j)t) \), где \( |\lambda| = 1 \). Числа \( \alpha_1, \ldots, \alpha_k \) являются корнями многочлена \( p \), поэтому они инвариантны относительно поворотов на углы \( \varphi_j \). Учитывая, что собственное значение \( r \) некратное (см. задачу 40.4), получаем \( \alpha_j = r \exp(2j \pi i / k) \). Пусть \( y_1 \) — собственный вектор, соответствующий собственному значению \( \alpha_1 = r \exp(2 \pi i / k) \). Тогда \( y_1^+ > 0 \) и \( y_1 = D_1 y_1^+ \) (см. доказательство теоремы 40.2.2). Существует такая матрица перестановки \( P \), что \( PD_1 P^T = \operatorname{diag}(e^{i \gamma_1} I_1, \ldots, e^{i \gamma_s} I_s) \), где числа \( e^{i \gamma_1}, \ldots, e^{i \gamma_s} \) попарно различны и \( I_1, \ldots, I_s \) — единичные матрицы. Если вместо вектора \( y_1 \) взять вектор \( e^{-i \gamma_1} y_1 \), то можно считать, что \( \gamma_1 = 0 \).

Разобьём матрицу \( PAP^T \) на блоки \( A_{pq} \) в соответствии с разбиением матрицы \( PD_1 P^T \). Так как \( A = \exp(i \varphi_j) D_j A D_j^{-1} \), то

\[
PAP^T = \exp(i \varphi_1)(PD_1 P^T)(PAP^T)(PD_1 P^T)^{-1},
\]

т. е. \( A_{pq} = \exp\left[i \left( \gamma_p - \gamma_q + \frac{2 \pi}{k} \right)\right] A_{pq} \). Значит, если \( \frac{2 \pi}{k} + \gamma_p \not\equiv \gamma_q \mod 2 \pi \), то \( A_{pq} = 0 \). Числа \( \gamma_i \) попарно различны, поэтому для любого \( p \) существует не более одного такого числа \( q \), что \( A_{pq} \neq 0 \) (при этом \( q \neq p \)). Из неразложимости матрицы \( A \) следует, что хотя бы одно такое число \( q \) существует. Следовательно, существует такое отображение \( p \mapsto q(p) \), что \( A_{p, q(p)} \neq 0 \) и \( \frac{2 \pi}{k} + \gamma_p \equiv \gamma_{q(p)} \mod 2 \pi \). Для \( p = 1 \) получаем \( \gamma_{q(1)} \equiv \frac{2 \pi}{k} \mod 2 \pi \). После перестановки строк и столбцов матрицы \( PAP^T \) можно считать, что \( \gamma_{q(1)} = \gamma_2 \). Продолжив аналогичные рассуждения, можно получить \( \gamma_{q(j-1)} = \gamma_j = 2 \pi (j-1)/k \) при \( 2 \leq j \leq \min(k, s) \). Докажем, что \( s = k \). Предположим сначала, что \( 1 < s < k \). Тогда \( \frac{2 \pi}{k} + \gamma_s - \gamma_r \not\equiv 0 \mod 2 \pi \) при \( 1 \leq r \leq s \). Поэтому \( A_{sr} = 0 \) для \( 1 \leq r \leq s \), т. е. матрица \( A \) приводима. Предположим теперь, что \( s > k \). Тогда \( \gamma_i = 2(i-1)\pi/k \) при \( 1 \leq i \leq k \). Числа \( \gamma_j \) попарно различны при \( 1 \leq j \leq s \) и для любого \( i \), где \( 1 \leq i \leq k \), найдётся такое число \( j \) (\( 1 \leq j \leq k \)), что \( \frac{2 \pi}{k} + \gamma_i \equiv \gamma_j \mod 2 \pi \).