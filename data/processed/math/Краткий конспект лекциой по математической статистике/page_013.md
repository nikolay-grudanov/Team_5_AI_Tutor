---
source_image: page_013.png
page_number: 13
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 90.30
tokens: 12526
characters: 3125
timestamp: 2025-12-24T07:03:07.996208
finish_reason: stop
---

Пример 4. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \), все \( X_i \in U_{0,\theta} \), где \( \theta > 0 \).
Найдем оценку метода моментов (ОММ) по первому моменту:

\[
E_\theta X_1 = \frac{\theta}{2} \implies \theta = 2E_\theta X_1 \implies \theta_1^* = 2\overline{X}.
\]

Найдем оценку метода моментов (ОММ) по \( k \)-му моменту:

\[
E_\theta X_1^k = \int_0^\theta y^k \frac{1}{\theta} dy = \frac{\theta^k}{k+1} \implies \theta = \sqrt[k]{(k+1)E_\theta X_1^k} \implies \theta_k^* = \sqrt[k]{(k+1)\overline{X}^k}.
\]

Проверим свойства полученных оценок.
Несмещённость:

1. По определению, \( E_\theta \theta_1^* = E_\theta 2\overline{X} = 2E_\theta \overline{X} = (по лемме 1) = 2\theta/2 = \theta \implies \theta_1^* = 2\overline{X} \) — несмещённая.

2. Рассмотрим оценку \( \theta_2^* \). Заметим, что \( E_\theta \theta_2^* = E_\theta \sqrt{3\overline{X}^2} \), тогда как \( \theta = \sqrt{3E_\theta X_1^2} = \sqrt{3E_\theta \overline{X}^2} \) (по лемме 1).

Равенство \( E_\theta \theta_2^* = \theta \) означало бы, что для с.в. \( \xi = 3\overline{X}^2 \) выполнено \( E_\theta \sqrt{\xi} = \sqrt{E_\theta \xi} \), а для величины \( \eta = \sqrt{\xi} \) выполнено \( E_\theta \eta^2 = (E_\theta \eta)^2 \).

Вспомните тот единственный случай, когда это возможно, чтобы согласиться с выводом: оценка \( \theta_2^* = \sqrt{3\overline{X}^2} \) — смещенная (как, впрочем, и оценки \( \theta_k^*, k > 2 \)).

Состоятельность:

1. По ЗБЧ, \( \theta_1^* = 2\overline{X} \xrightarrow{p} 2E_\theta X_1 = 2\theta/2 = \theta \implies \theta_1^* = 2\overline{X} \) — состоятельная.

2. Заметим, что по ЗБЧ (или по лемме 3 — только для тех, кто ее доказал) при \( n \to \infty \)

\[
\overline{X}^k \xrightarrow{p} E_\theta X_1^k = \frac{\theta^k}{k+1}.
\]

Поскольку функция \( \sqrt[k]{(k+1)y} \) непрерывна для всех \( y > 0 \), то при \( n \to \infty \)

\[
\theta_k^* = \sqrt[k]{(k+1)\overline{X}^k} \xrightarrow{p} \sqrt[k]{(k+1)\frac{\theta^k}{k+1}} = \theta.
\]

Упражнение. Зачем нужна ссылка на непрерывность функции \( \sqrt[k]{(k+1)y} \)?

То есть вся последовательность \( \{ \theta_k^* \}_{k=1}^\infty = \{ \sqrt[k]{(k+1)\overline{X}^k} \} \) состоит из состоятельных оценок, при этом только оценка \( \theta_1^* = 2\overline{X} \) — несмещённая.

Замечание 7. Может случиться так, что оценка \( \theta^* \notin \Theta \), тогда как \( \theta \in \Theta \). В этом случае в качестве оценки берут ближайшую к \( \theta^* \) точку из \( \Theta \), на худой конец — из замыкания \( \Theta \), если \( \Theta \) не замкнуто.

Пример 5. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \), все \( X_i \in N_{a,1} \), где по какой-то причине \( a \geq 0 \).
Ищем оценку для \( a \) по первому моменту:

\[
E_a X_1 = a \implies a^* = \overline{X}.
\]

Однако по условию \( a \geq 0 \), тогда как \( \overline{X} \) может быть и отрицательно. Понятно, что если \( \overline{X} < 0 \), то в качестве оценки для положительного параметра \( a \) более подойдет 0. Если же \( \overline{X} > 0 \), в качестве оценки нужно брать \( \overline{X} \). Итого: \( a^* = \max\{0, \overline{X}\} \) — оценка метода моментов.