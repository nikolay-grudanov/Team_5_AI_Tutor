---
source_image: page_223.png
page_number: 223
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 65.20
tokens: 12608
characters: 4043
timestamp: 2025-12-24T05:41:54.164329
finish_reason: stop
---

Доказательство проводится индукцией по количеству сечений с формулой сечения C (назовем их C-сечениями). Базис индукции тривиален. Для обоснования индукционного перехода выберем в данном доказательстве C-сечение, выше которого нет других C-сечений, и запишем часть данного доказательства, которая заканчивается этим C-сечением, в виде

\[
\begin{array}{c}
\psi \\
\Delta \rightarrow \Lambda, C \\
\Delta, \Gamma \rightarrow \Theta, \Lambda
\end{array}
\]

Теперь вычеркнем из всех секвенций, входящих в доказательство правой посылки, все предки (указанного явно) антecedентного C и умножим все секвенции, содержащие такие предки, на \( \Delta \rightarrow \Lambda \). Полученная фигура превращается в (0, F)-доказательство старой секвенции \( \Delta, \Gamma \rightarrow \Theta, \Lambda \) после вычеркивания повторений и надписывания над старыми C-аксиомами вывода левой посылки рассматриваемого C-сечения:

\[
\begin{array}{c}
\psi \\
\Delta^o, \Gamma_1' \rightarrow \Lambda^o, \Theta_1 \\
\Delta, \Gamma_2' \rightarrow \Lambda, \Theta_2 \\
\Delta, \Gamma_3' \rightarrow \Lambda, \Theta_3', C \\
\Delta, E, \Gamma_4' \rightarrow \Lambda, \Theta_4, E \\
\Delta, \Gamma \rightarrow \Theta, \Lambda
\end{array}
\]

\( \Delta^o \) и \( \Lambda^o \) в фигуре, которая появилась на месте C-утончения, означают \( \Delta \) и \( \Lambda \), если \( \Gamma_1 \) содержало предки C (тогда новая фигура — просто повторение секвенций), и означают пустые списки в противном случае (в этом случае новая фигура — последовательность утончений, вводящих \( \Delta \) и \( \Lambda \)). Лемма доказана.

Лемма 3. Если \( |(k, F \cup \{C\})S| \) и степень формулы C равна k, то \( |(k, F)S| \).

Доказательство. В силу леммы 2 можно считать, что \( k > 0 \). Следует рассмотреть 7 случаев в зависимости от вида формулы. При этом используются соответствующие пункты леммы 1. Как и при доказательстве леммы 3, выбираем одно из самых верхних C-сечений и устраняем его; при этом, однако, оно разобьется на сечения меньшей степени.

Случай 1.

\[
\begin{array}{c}
& \rightarrow A, B, \Gamma_1 \rightarrow \Theta \\
A \& B, \Gamma_1 \rightarrow \Theta \\
\Delta \rightarrow \Lambda, A \& B & A \& B \Gamma \rightarrow \Theta \\
\Delta, \Gamma \rightarrow \Theta, \Lambda
\end{array}
\]

\[
\begin{array}{c}
\Delta \rightarrow \Lambda, A \\
\Delta, B, \Gamma_1' \rightarrow \Theta_1, \Lambda^o \\
\Delta, \Gamma_1' \rightarrow \Theta_1, \Lambda \\
\Delta, \Gamma \rightarrow \Theta, \Lambda
\end{array}
\]

(Сеч. Сокр.)

Верху показано данное доказательство, внизу — измененное. Все предки антecedентного A&B, имеющие вид A&B, вычеркнуты, а содержащие их секвенции домножены на \( \Delta \rightarrow \Lambda \). (k, F)-доказательства секвенций \( \Delta \rightarrow \Lambda; A \) и \( \Delta \rightarrow \Lambda, B \) получены из (k, F)-доказательства секвенции \( \Delta \rightarrow \Lambda, A \& B \) по лемме 1. Сокращения и аксиомы, содержащие предки A&B, рассматриваются так же, как в лемме 2. Смысл обозначений \( \Delta^o \) и \( \Lambda^o \) аналогичен их смыслу в лемме 2.

Случай 2. Слева данное доказательство, справа — измененное.

\[
\begin{array}{c}
A(t), \forall x A(x), \Gamma_1 \rightarrow \Theta_1 \\
\forall x A(x), \Gamma_1 \rightarrow \Theta_1 \\
\Delta \rightarrow \Lambda, A(t) \\
\Delta, \Gamma_1' \rightarrow \Theta_1, \Lambda \\
\Delta, \Gamma \rightarrow \Theta, \Lambda
\end{array}
\]

Для получения доказательства секвенции \( \Delta \rightarrow \Lambda, A(t) \) применяется случай 2 леммы 1.

Случай 6.

\[
\begin{array}{c}
\Delta_1 \rightarrow \Lambda_1, A, B \\
\Delta_1 \rightarrow \Lambda_1, A \vee B \\
\Delta \rightarrow \Lambda, A \vee B \\
\Delta, \Gamma \rightarrow \Theta, \Lambda
\end{array}
\]

\[
\begin{array}{c}
\Delta_1, \Gamma^o \rightarrow \Theta^o, \Lambda_1', A, B \\
\Delta_1, \Gamma \rightarrow \Theta, \Lambda_1', B \\
\Delta_1, \Gamma \rightarrow \Theta, \Lambda_1' \\
\Delta, \Gamma \rightarrow \Theta, \Lambda
\end{array}
\]

Остальные случаи рассматриваются аналогично. Два из них иллюстрированы ниже на примере.