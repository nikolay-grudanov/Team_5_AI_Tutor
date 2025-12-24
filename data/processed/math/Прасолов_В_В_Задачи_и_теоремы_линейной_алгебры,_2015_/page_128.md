---
source_image: page_128.png
page_number: 128
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.72
tokens: 6275
characters: 1900
timestamp: 2025-12-24T08:10:54.999592
finish_reason: stop
---

Для ядра отображения \( A : U \to V \) мы имеем точную последовательность \( 0 \to \mathrm{Ker}\,A \to U \xrightarrow{A} V \). Коядром отображения \( A : U \to V \) называют пространство \( \mathrm{Coker}\,A = V / \mathrm{Im}\,A \), для которого точна последовательность \( U \xrightarrow{A} V \to \mathrm{Coker}\,A \to 0 \). Соединяя эти две точные последовательности, мы получаем точную последовательность

\[
0 \to \mathrm{Ker}\,A \to U \xrightarrow{A} V \to \mathrm{Coker}\,A \to 0.
\]

**Теорема 6.5.1.** *При переходе к двойственным пространствам и двойственным отображениям точность последовательностей сохраняется.*

**Доказательство.** Рассмотрим последовательность отображений

\[
U \xrightarrow{A} V \xrightarrow{B} W
\]

и двойственную ей последовательность отображений

\[
U^* \xleftarrow{A^*} V^* \xleftarrow{B^*} W^*.
\]

Требуется доказать, что если \( \mathrm{Ker}\,B = \mathrm{Im}\,A \), то \( \mathrm{Im}\,B^* = \mathrm{Ker}\,A^* \). По определению

\[
\begin{align*}
\mathrm{Ker}\,A^* &= \{ f \in V^* \mid f(Au) = 0 \ \forall u \in U \}, \\
\mathrm{Im}\,B^* &= \{ f \in V^* \mid \exists g \in W^*: f(v) = g(Bv) \ \forall v \in V \}.
\end{align*}
\]

Легко видеть, что \( \mathrm{Im}\,B^* \subset \mathrm{Ker}\,A^* \). Действительно, если \( f(v) = g(Bv) \), то \( f(Au) = g(BAu) = 0 \), поскольку \( BA = 0 \). Далее, согласно теореме 6.2.1

\[
\dim \mathrm{Ker}\,A^* = \dim V - \dim \mathrm{Im}\,A = \dim V - \dim \mathrm{Ker}\,B = \dim \mathrm{Im}\,B^*.
\]

Поэтому \( \mathrm{Im}\,B^* = \mathrm{Ker}\,A^* \).

При переходе к двойственным пространствам точная последовательность

\[
0 \to \mathrm{Ker}\,A \to U \xrightarrow{A} V \to \mathrm{Coker}\,A \to 0
\]

переходит в точную последовательность

\[
0 \leftarrow (\mathrm{Ker}\,A)^* \leftarrow U^* \xleftarrow{A^*} V^* \leftarrow (\mathrm{Coker}\,A)^* \leftarrow 0,
\]

поэтому ядро и коядро являются двойственными понятиями.