---
source_image: page_214.png
page_number: 214
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 84.44
tokens: 13174
characters: 5407
timestamp: 2025-12-24T05:41:34.645315
finish_reason: stop
---

Применение \( \rightarrow \forall \) в случае 9а законно, так как r не входит свободно в \( \forall x A(x), \Gamma_E \rightarrow \Theta_E \). По аналогичной причине законно \( \exists \rightarrow \) в случае 9б (когда r свободно входит в \( A(r), \Gamma_E \rightarrow \Theta_E \) и \( J(r) \), но не в \( \forall x A(x), \Gamma_F \rightarrow \Theta_F \)). В более общем случае исчисления предикатов с функциями (включая индивидуальные символы), r может содержать свободные переменные \( c_1, \ldots, c_m \) и индивидуальные символы \( e_{m+1}, \ldots, e_n \), которые являются параметрами формулы J для посылки, но не являются общими для E-части и F-части заключения (случаи 9а', 9б'). Запишем r в виде «r(\( c_1, \ldots, c_m, e_{m+1}, \ldots, e_n \))» и J для посылки в виде «J(\( c_1, \ldots, c_m, e_{m+1}, \ldots, e_n \))». Для случая 9а' (\( \forall x A(x), \Gamma_E \rightarrow \Theta_E \) не содержит \( c_1, \ldots, c_m, e_{m+1}, \ldots, e_n \) в качестве параметров) мы можем заменить \( e_{m+1}, \ldots, e_n \) во всем уже построенном E-доказательстве посылки на соответствующие различные переменные \( c_{m+1}, \ldots, c_{m+n} \), не входившие в это доказательство, и получить доказательство секвенции

\[
A(r(c_1, \ldots, c_n)), \forall x A(x), \Gamma_E \rightarrow \Theta_E, J(c_1, \ldots, c_n).
\]

Теперь вместо того, чтобы вывести \( \forall y J(y) \) как главную формулу из боковой формулы J(r) путем одного применения правила в каждом из доказательств (случай 9а), мы можем вывести \( \forall y_1 \ldots \forall y_n J(y_1, \ldots, y_n) \) из J(\( c_1, \ldots, c_n \)) в E-доказательстве и из J(\( c_1, \ldots, c_m, e_{m+1}, \ldots, e_n \)) в F-доказательстве с помощью n применений тех же правил, что и раньше.

Правила \( \exists \rightarrow \) и \( \rightarrow \exists \) рассматриваются аналогично, частично в рамках старых случаев, а частично в качестве новых случаев 10а, 10b, 10a', 10b'.

Суммируя, мы исправляем E-часть или F-часть, или обе, получаем E-доказательство или F-доказательство, или оба, спускаясь вниз по данному доказательству шаг за шагом и применяя на каждом шаге подходящий случай. Это эффективным образом приводит к одному из трех результатов, описанных в случаях (EF), (E) и (F) теоремы, в зависимости от данного доказательства и данного анализа этого доказательства. Эта процедура может включать ненужную работу по исправлению верхних частей ветвей, которые потом все равно будут выброшены при рассмотрении двухпосылочных правил, подпадающих под случаи 3а, 3б. Если мы заранее распределим аксиомы по классам EF, E и F, а применения двухпосылочных правил по классам E и F, то мы сможем спланировать работу и предвидеть, какие ветви будут выброшены.

Пример 11. Сначала мы приводим данное доказательство секвенции E \( \rightarrow \) F в G4а. E-часть напечатана обычным шрифтом, F-часть — жирным. Для каждой занумерованной секвенции \( \Delta \rightarrow \Lambda \) из этого доказательства имеется секвенция с тем же номером в E-доказательстве и в F-доказательстве под ним. Это результаты исправления соответствующих секвенций \( \Delta_E \rightarrow \Lambda_E, \Delta_F \rightarrow \Lambda_F \) из E-части и F-части¹).

EF-аксиома

1. \( P(a), S, R \rightarrow \exists x P(x), P(a) \rightarrow \exists \)
2. \( P(a), S, R \rightarrow \exists x P(x) \rightarrow \exists \)
3. \( P(a), S \rightarrow R \supset \exists x P(x) \rightarrow \supset \)
4. \( S \& P(a) \rightarrow R \supset \exists x P(x) \& \rightarrow \)
5. \( S \& P(a) \rightarrow R \supset \exists x P(x), S \& Q(b) \rightarrow y \)

F-аксиома

6. \( S, Q(b), P(a) \rightarrow S \)
7. \( Q(b), S, P(a) \rightarrow Q(b) \rightarrow \& \)
8. \( S, Q(b), P(a) \rightarrow S \& Q(b) \& \rightarrow \)
9. \( Q(b), S \& P(a) \rightarrow S \& Q(b) \)
10. \( (R \supset \exists x P(x)) \supset Q(b), S \& P(a) \rightarrow S \& Q(b) \rightarrow \supset \)
11. \( (R \supset \exists x P(x)) \supset Q(b) \rightarrow S \& P(a) \supset S \& Q(b) \rightarrow \forall \)
12. \( (R \supset \exists x P(x)) \supset Q(b) \rightarrow \forall x (S \& P(x) \supset S \& Q(b)) \rightarrow V \)

Е-доказательство: формулы, вставленные вместо F-части, выделены жирным шрифтом.

\[
P(a), R \rightarrow \exists x P(x), P(a) \rightarrow \neg
1. R \rightarrow \exists x P(x), P(a), \neg P(a) \rightarrow \exists
R \rightarrow \exists x P(x), \neg P(a) \rightarrow \forall
2. R \rightarrow \exists x P(x), \forall x \neg P(x) \rightarrow \supset
3, 4, 5. \rightarrow R \supset \exists x P(x), \forall x \neg P(x) \rightarrow \supset
(R \supset \exists x P(x)) \supset Q(b) \rightarrow \forall x \neg P(x), Q(b)
7, 8, 9. Q(b) \rightarrow Q(b) \supset \rightarrow
10, 11, 12. (R \supset \exists x P(x)) \supset Q(b) \rightarrow \forall x \neg P(x) \vee Q(b) \rightarrow V
\]

F-доказательство: формулы, вставленные вместо E-части, напечатаны обычным шрифтом.

\[
P(a), S \rightarrow P(a)
1. \neg P(a), P(a), S \rightarrow \neg \rightarrow
2, 3. \forall x \neg P(x), P(a), S \rightarrow \forall \rightarrow
4. \forall x \neg P(x), S \& P(a) \rightarrow \& \rightarrow
5. \forall x \neg P(x), S \& P(a) \rightarrow S \& Q(b) \rightarrow y
\]

¹) В этом примере устраняются только повторения. Никакая исправленная секвенция не выбрасывается впоследствии в рамках случаи 3а или 3б для двухпосылочного правила и не меняется при подстановке \( c_{m+1}, \ldots, c_n \) вместо \( e_{m+1}, \ldots, e_n \) в случаях 9а', 9б', 10а' или 10б'.