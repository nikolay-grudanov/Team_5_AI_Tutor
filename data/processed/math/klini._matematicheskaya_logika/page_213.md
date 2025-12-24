---
source_image: page_213.png
page_number: 213
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 74.05
tokens: 12950
characters: 4628
timestamp: 2025-12-24T05:41:19.609584
finish_reason: stop
---

**Пропозициональные и структурные правила и некоторые предикатные правила (пояснения ниже)**

Е-доказательство | F-доказательство

**Случай 4а. Однопосылочное E-применение с E-посылкой**

\[
\frac{\Sigma_1, \Gamma_E \rightarrow \Theta_E, \Sigma_2}{\Pi_1, \Gamma_E \rightarrow \Theta_E, \Pi_2}
\]

**Случай 5а. Однопосылочное E-применение с EF-посылкой**

\[
\frac{\Sigma_1, \Gamma_E \rightarrow \Theta_E, \Sigma_2, J}{\Pi_1, \Gamma_E \rightarrow \Theta_E, \Pi_2, J} \quad J, \Gamma_F \rightarrow \Theta_F
\]

**Случай 6а. E-применение с двумя E-посылками**

\[
\frac{\Sigma_1, \Gamma_E \rightarrow \Theta_E, \Sigma_2}{\Pi_1, \Gamma_E \rightarrow \Theta_E, \Pi_2}
\]
\[
\frac{\Sigma_3, \Gamma_E \rightarrow \Theta_E, \Sigma_4}{\Pi_3, \Gamma_E \rightarrow \Theta_E, \Pi_4}
\]

**Случай 7а. E-применение с EF-посылкой (например, первой) и E-посылкой**

\[
\frac{\Sigma_1, \Gamma_E \rightarrow \Theta_E, \Sigma_2, J}{\Pi_1, \Gamma_E \rightarrow \Theta_E, \Pi_2, J}
\]
\[
\frac{\Sigma_3, \Gamma_E \rightarrow \Theta_E, \Sigma_4}{J, \Gamma_F \rightarrow \Theta_F}
\]

**Случай 8а. E-применение с двумя EF-посылками**

\[
\frac{\Sigma_1, \Gamma_E \rightarrow \Theta_E, \Sigma_2, J_1}{\Pi_1, \Gamma_E \rightarrow \Theta_E, \Pi_2, J_1}
\]
\[
\frac{\Sigma_3, \Gamma_E \rightarrow \Theta_E, \Sigma_4, J_2}{\Pi_3, \Gamma_E \rightarrow \Theta_E, \Pi_4, J_2}
\]
\[
\frac{J_1, \Gamma_F \rightarrow \Theta_F}{J_1 \lor J_2, \Gamma_F \rightarrow \Theta_F}
\]
\[
\frac{J_2, \Gamma_F \rightarrow \Theta_F}{J_1 \lor J_2, \Gamma_F \rightarrow \Theta_F}
\]

**Случай 8b. F-применение с двумя EF-посылками**

\[
\frac{\Gamma_E \rightarrow \Theta_E, J_1, \Gamma_E \rightarrow \Theta_E, J_2}{\Gamma_E \rightarrow \Theta_E, J_1 \& J_2}
\]
\[
\frac{J_1, \Sigma_1, \Gamma_F \rightarrow \Theta_F, \Sigma_2}{J_1, J_2, \Pi_1, \Gamma_F \rightarrow \Theta_F, \Pi_2}
\]
\[
\frac{J_2, \Sigma_3, \Gamma_F \rightarrow \Theta_F, \Sigma_4}{J_2, \Pi_1, \Gamma_F \rightarrow \Theta_F, \Pi_2}
\]
\[
\frac{J_1 \& J_2, \Pi_1, \Gamma_F \rightarrow \Theta_F, \Pi_2}{J_1 \& J_2, \Pi_1, \Gamma_F \rightarrow \Theta_F, \Pi_2}
\]

Е-доказательство | F-доказательство

**Случай 9а. E-применение с EF-посылкой**

\[
A(r), \forall x A(x), \Gamma_E \rightarrow \Theta_E, J(r) \rightarrow \forall x A(x), \Gamma_E \rightarrow \Theta_E, J(r)
\]
\[
\forall y J(y), \Gamma_F \rightarrow \Theta_E \rightarrow \forall y J(y), \Gamma_F \rightarrow \Theta_E
\]

**Случай 9b. F-применение с EF-посылкой**

\[
\Gamma_E \rightarrow \Theta_E, J(r) \rightarrow \exists y J(y)
\]
\[
\Gamma_E \rightarrow \Theta_E, \exists y J(y) \rightarrow \exists y J(y), \forall x A(x), \Gamma_F \rightarrow \Theta_F
\]

Если b не входит в \( \Gamma_F \rightarrow \Theta_F \) (F-часть посылки \( \Delta_1 \rightarrow \Lambda_1 \)); если рассматривается F-применение, то в \( \Gamma_E \rightarrow \Theta_E \). Следовательно, при EF-посылке (случаи 5а, 5б) J не содержит b свободно, так как для этой посылки выполнено условие (1) из случая (EF) теоремы. Поэтому для нового \( \rightarrow \forall \) выполнено ограничение на переменные, а для заключения снова выполнено (1)¹.

Теперь рассмотрим \( \forall \rightarrow \). Если не имеют места обстоятельства, описываемые ниже, то это правило можно рассмотреть в рамках случаев 3а—5б, с очевидной модификацией в случаях 4а—5б, когда \( \Pi_1, \Pi_2 \) (в действительности \( \Pi_2 \) пусто) появляются также и в посылке (случаи 4а'—5а'). Допустим, что посылка — это EF-посылка, и A(x) содержит x свободно. В исчислении предикатов без функций r должно быть просто переменной. Пусть рассматривается E-применение, и эта переменная r входит свободно в \( \Gamma_F \rightarrow \Theta_F \), но не в \( \forall x A(x), \Gamma_E \rightarrow \Theta_E \). Тогда в силу условия (1) из (EF)-случая формула J для заключения (но не для посылки) не должна содержать r свободно. Предполагая, что J для посылки действительно содержит r свободно (случай 9а), запишем ее в виде «J(r)». Пусть y — переменная (возможно, x), свободная для r в J(r) и не входящая свободно в J(r).

\( \forall \rightarrow \) в случае, когда r — это переменная, входящая свободно в J для посылки, но не входящая свободно F-доказательство в E-часть или F-часть заключения тельство

1) Мы добавили к нашему первоначальному плану (второй абзац параграфа) выполнение (1). Индивидные параметры, не являющиеся общими для E-части и F-части, удаляются из формулы J, как только они перестают быть общими, при рассмотрении \( \forall \rightarrow \) и \( \rightarrow \exists \). В противном случае нам пришлось бы удалять b, если она присутствует, при рассмотрении \( \rightarrow \forall \) и \( \rightarrow \exists \).