---
source_image: page_325.png
page_number: 325
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.68
tokens: 6664
characters: 2530
timestamp: 2025-12-24T08:16:26.653889
finish_reason: stop
---

Доказательство. Применим индукцию по \( k \). Ясно, что \( P_{\sigma_1 \sigma_2} = m_{\sigma_1 \sigma_2} = (-1)^{\sigma_1 + \sigma_2 + 1} \). Знак перестановки, соответствующей \( \{ \sigma_1, \sigma_2 \} \), равен \( (-1)^a \), где \( a = (\sigma_1 - 1) + (\sigma_2 - 2) \equiv (\sigma_1 + \sigma_2 + 1) \mod 2 \).

Воспользовавшись результатом задачи 31.1, легко проверить, что

\[
P_{\sigma_1 \ldots \sigma_{2k}} = \sum_{i=2}^{2k} (-1)^i P_{\sigma_1 \sigma_i} P_{\sigma_2 \ldots \hat{\sigma}_i \ldots \sigma_{2k}}.
\]

По предположению индукции

\[
P_{\sigma_2 \ldots \hat{\sigma}_i \ldots \sigma_{2k}} = (-1)^{\tau},
\]

где \( \tau = (\sigma_2 \ldots \hat{\sigma}_i \ldots \sigma_{2k} \ 1\ 2\ldots 2m) \). Знаки перестановок \( \sigma \) и \( \tau \) равны \( (-1)^a \) и \( (-1)^b \), где \( a = (\sigma_1 - 1) + \ldots + (\sigma_{2k} - 2k) \) и

\[
b = (\sigma_2 - 1) + (\sigma_3 - 2) + \ldots + (\sigma_{i-1} - i + 2) + (\sigma_{i+1} - i + 1) + \ldots + (\sigma_{2k} - 2k + 2),
\]

т. е. \( (-1)^{\tau} = (-1)^{\sigma}(-1)^{\sigma_1 + \sigma_i + 1} \). Значит,

\[
P_{\sigma_1 \ldots \sigma_{2k}} = \sum_{i=2}^{2k} (-1)^i (-1)^{\sigma_1 + \sigma_i + 1} (-1)^{\sigma}(-1)^{\sigma_1 + \sigma_i + 1} =
= (-1)^{\sigma} \sum_{i=2}^{2k} (-1)^i = (-1)^{\sigma}.
\]

Теорема 31.2.2. Пусть \( M \) — определённая выше матрица, \( A \) — кососимметрическая матрица порядка \( 2n \). Тогда \( \mathrm{Pf}\,(A + \lambda^2 M) = \sum_{k=0}^n \lambda^{2k} P_k \), где

\[
P_k = \sum_{\sigma} A \begin{pmatrix} \overline{\sigma}_1 & \ldots & \overline{\sigma}_{2(n-k)} \\ \overline{\sigma}_1 & \ldots & \overline{\sigma}_{2(n-k)} \end{pmatrix}
\]

Доказательство [Ka2]. Матрицы \( A \) и \( M \) будем рассматривать как элементы \( \sum_{i<j} a_{ij} e_i \wedge e_j \) и \( \sum_{i<j} m_{ij} e_i \wedge e_j \) в \( \Lambda^2 V \). Так как \( A \wedge M = M \wedge A \), справедлива формула бинома Ньютона:

\[
\Lambda^n(A + \lambda^2 M) = \sum_{k=0}^n \binom{n}{k} \lambda^{2k} (\Lambda^k M) \wedge (\Lambda^{n-k} A) =
= \sum_{k=0}^n \binom{n}{k} \lambda^{2k} \cdot (k! \ P_{\sigma_1 \ldots \sigma_{2k}})((n-k)! \ P_k) e_{\sigma_1} \wedge \ldots \wedge e_{\sigma_{2k}} \wedge e_{\overline{\sigma}_1} \wedge \ldots \wedge e_{\overline{\sigma}_{2(n-k)}}
\]

Согласно теореме 31.2.1 \( P_{\sigma_1 \ldots \sigma_{2k}} = (-1)^{\sigma} \); ясно также, что

\[
e_{\sigma_1} \wedge \ldots \wedge e_{\sigma_{2k}} \wedge e_{\overline{\sigma}_1} \wedge \ldots \wedge e_{\overline{\sigma}_{2(n-k)}} = (-1)^{\sigma} e_1 \wedge \ldots \wedge e_{2n}.
\]