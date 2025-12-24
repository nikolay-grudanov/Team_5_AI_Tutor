---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 63.85
tokens: 12811
characters: 3370
timestamp: 2025-12-24T07:05:06.239076
finish_reason: stop
---

критерии вида

\[
\begin{cases}
\text{если } \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} < c & \Longrightarrow \delta(\vec{X}) = H_1 \\
\text{если } \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c & \Longrightarrow \delta(\vec{X}) = H_2 \\
\text{если } \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = c & \Longrightarrow \left\{ \begin{array}{ll}
\delta(\vec{X}) = H_2 & \text{с вероятностью } p, \\
\delta(\vec{X}) = H_1 & \text{с вероятностью } 1 - p,
\end{array} \right.
\end{cases}
\]

и убедимся, что лишь один из них имеет заданный уровень. Сначала рассмотрим нерандомизированные критерии.

1. \( c < 0 \). В этом случае \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} > c \) при любом \( X_1 \), и критерий отношения правдоподобия имеет вид:

\[
\delta_1(X_1) = H_2 \quad \text{при любом } X_1.
\]

Его уровень \( \alpha(\delta_1) = P_{H_1}(\delta_1(X_1) = H_2) = 1 \) — не то.

2. \( 0 < c < 2 \). В этом случае \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} > c \) при \( X_1 \in [0, 2] \), и \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} < c \) при \( X_1 \in (2, 5] \). Критерий отношения правдоподобия имеет вид:

\[
\delta_2(X_1) = \begin{cases}
H_2 & \text{при } X_1 \in [0, 2] \\
H_1 & \text{при } X_1 \in (2, 5].
\end{cases}
\]

Его уровень \( \alpha(\delta_2) = P_{H_1}(\delta_2(X_1) = H_2) = P_{H_1}(X_1 \in [0, 2]) = P_{H_1}(X_1 \in [1, 2]) = 1/4 \) — не то.

3. \( 2 < c < \infty \). В этом случае \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} > c \) при \( X_1 \in [0, 1] \), и \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} < c \) при \( X_1 \in (1, 5] \). Критерий отношения правдоподобия имеет вид:

\[
\delta_3(X_1) = \begin{cases}
H_2 & \text{при } X_1 \in [0, 1] \\
H_1 & \text{при } X_1 \in (1, 5].
\end{cases}
\]

Его уровень \( \alpha(\delta_3) = P_{H_1}(\delta_3(X_1) = H_2) = P_{H_1}(X_1 \in [0, 1]) = 0 \) — не то.

Таким образом, ни один из нерандомизированных критериев не имеет нужного уровня. Посмотрим на рандомизированные.

4. \( c = 0 \). В этом случае \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} > c \) при \( X_1 \in [0, 2] \), и \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} = c \) при \( X_1 \in (2, 5] \). Критерий отношения правдоподобия имеет вид:

\[
\begin{cases}
\text{если } X_1 \in [0, 2] & \Longrightarrow \delta_4(X_1) = H_2 \\
\text{если } X_1 \in (2, 5] & \Longrightarrow \left\{ \begin{array}{ll}
\delta_4(X_1) = H_2 & \text{с вероятностью } p, \\
\delta_4(X_1) = H_1 & \text{с вероятностью } 1 - p.
\end{array} \right.
\end{cases}
\]

Его уровень \( \alpha(\delta_4) = P_{H_1}(\delta_4(X_1) = H_2) = P_{H_1}(X_1 \in [0, 2]) + pP_{H_1}(X_1 \in [2, 5]) = 1/4 + p3/4 \neq 1/5 \) — не то.

5. \( c = 2 \). В этом случае \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} > c \) при \( X_1 \in [0, 1] \), \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} < c \) при \( X_1 \in [2, 5] \), \( \frac{\Psi_2(X_1)}{\Psi_1(X_1)} = c \) при \( X_1 \in (1, 2) \). Критерий отношения правдоподобия имеет вид:

\[
\begin{cases}
\text{если } X_1 \in [0, 1] & \Longrightarrow \delta_5(X_1) = H_2 \\
\text{если } X_1 \in [2, 5] & \Longrightarrow \delta_5(X_1) = H_1 \\
\text{если } X_1 \in (1, 2) & \Longrightarrow \left\{ \begin{array}{ll}
\delta_5(X_1) = H_2 & \text{с вероятностью } p, \\
\delta_5(X_1) = H_1 & \text{с вероятностью } 1 - p.
\end{array} \right.
\end{cases}
\]

Его уровень \( \alpha(\delta_5) = P_{H_1}(\delta_5(X_1) = H_2) = P_{H_1}(X_1 \in [0, 1]) + pP_{H_1}(X_1 \in (1, 2)) = 0 + p1/4 = 1/5 \) при \( p = 4/5 \) — требуемый уровень.