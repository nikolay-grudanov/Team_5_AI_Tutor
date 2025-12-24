---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.54
tokens: 5006
characters: 983
timestamp: 2025-12-24T07:31:05.988133
finish_reason: stop
---

11.
\[
\begin{cases}
\frac{\partial M_1}{\partial t} - v_1 \frac{\partial M_1}{\partial t} = -\alpha M_1 + \alpha M_2, \\
\frac{\partial M_2}{\partial t} + v_2 \frac{\partial M_2}{\partial x} = \beta M_1 - \beta M_2,
\end{cases}
\]
\[
\begin{cases}
\frac{dm_1}{dt} = -\alpha m_1 + \alpha m_2 + v_1, & m_k(t) = M_k(t, 0), \\
\frac{dm_2}{dt} = \beta m_1 - \beta m_2 - v_2, & \text{где} \\
& m_1(0) = m_2(0) = 0.
\end{cases}
\]

13.
\[
\begin{cases}
M_1(t, x) = e^{-\alpha t}(x + vt) + \int_0^t \alpha e^{-\alpha u} M_2(t-u, x+vu) du, \\
M_2(t, x) = e^{-\beta t} \left(x - \frac{\alpha t^2}{2}\right) + \int_0^t \beta e^{-\beta u} M_1(t-u, x-\frac{\alpha u^2}{2}) du,
\end{cases}
\]
\[
\begin{cases}
m_1(t) = \frac{v}{\alpha} (1 - e^{-\alpha t}) + \int_0^t \beta e^{-\beta u} m_1(t-u) du, \\
m_2(t) = -\frac{2}{\beta^2} [1 - (1+\beta t) e^{-\beta t}] + \int_0^t \beta e^{-\beta u} m_1(t-u) du,
\end{cases}
\]
где \( m_k(t) = M_k(t, 0) \), \( M_k(t, x) = x + m_k(t) \), \( m_k(0) = 0 \).