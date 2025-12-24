---
source_image: page_328.png
page_number: 328
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.30
tokens: 6529
characters: 2631
timestamp: 2025-12-24T08:16:26.999130
finish_reason: stop
---

32.2. Соотношения Плюккера

Исходя непосредственно из определения разложимого кососимметрического тензора, за конечное число операций нельзя выяснить, разложим ли данный кососимметрический тензор

\[
\bullet \quad a_{i_1 \ldots i_k} e_{i_1} \wedge \ldots \wedge e_{i_k}.
\]

Мы покажем, что условие разложимости кососимметрического тензора эквивалентно некоторой системе уравнений для его координат \(a_{i_1 \ldots i_k}\) (соотношения Плюккера). Предварительно сделаем несколько замечаний.

Пусть \(\alpha \in \Lambda^p V^*\). Зададим отображение

\[
i(\alpha): \Lambda^k V \to \Lambda^{k-p} V
\]

так, чтобы для всех \(T \in \Lambda^k V\) и \(f \in \Lambda^{k-p} V^*\) выполнялось равенство \(\langle i(\alpha)T, f \rangle = \langle T, \alpha \wedge f \rangle\). Аналогично для \(\omega \in \Lambda^p V\) зададим отображение

\[
i(\omega): \Lambda^k V^* \to \Lambda^{k-p} V^*
\]

так, чтобы для всех \(f \in \Lambda^k V^*\) и \(T \in \Lambda^{k-p} V\) выполнялось равенство \(\langle i(\omega)f, T \rangle = \langle f, \omega \wedge T \rangle\).

Будем говорить, что подпространство \(W \subset U\) обёртывает кососимметрический тензор \(\omega \in \Lambda^k V\), если \(\omega \in \Lambda^k W\), т. е. \(\omega\) представляется в виде суммы внешних произведений элементов \(W\). Если \(\omega\) — разложимый кососимметрический тензор, соответствующий подпространству \(U\), то \(W\) обёртывает \(\omega\) тогда и только тогда, когда \(W \supset U\), т. е. \(U\) — минимальное обёртывающее подпространство для \(\omega\). Покажем, что для любого \(\omega \in \Lambda^k V\) существует минимальное обёртывающее подпространство \(W\), причём \(\dim W = k\) тогда и только тогда, когда \(\omega\) разложим (если \(\omega\) неразложим, то \(\dim W > k\)).

Теорема 32.2.1. Пространство \(W\) обёртывает \(\omega \in \Lambda^k V\) тогда и только тогда, когда \(i(\alpha)\omega \in W\) для любого \(\alpha \in \Lambda^{k-1} V^*\).

Доказательство. Пусть \(e_1, \ldots, e_m\) — базис пространства \(W\). Дополним его до базиса \(e_1, \ldots, e_n\) пространства \(V\) и рассмотрим двойственный базис \(\varepsilon_1, \ldots, \varepsilon_n\).

Пусть \(\omega = \bullet x_{i_1 \ldots i_k} e_{i_1} \wedge \ldots \wedge e_{i_k}\) и \(\alpha = \varepsilon_{j_1} \wedge \ldots \wedge \varepsilon_{j_{k-1}}\). Тогда

\[
\langle i(\alpha)\omega, \varepsilon_j \rangle = \langle \omega, \alpha \wedge \varepsilon_j \rangle =
\]
\[
= \left\langle \bullet x_{i_1 \ldots i_k} e_{i_1} \wedge \ldots \wedge e_{i_k}, \varepsilon_{j_1} \wedge \ldots \wedge \varepsilon_{j_{k-1}} \wedge \varepsilon_j \right\rangle = \pm \frac{1}{k!} x_{i_1 \ldots i_k},
\]