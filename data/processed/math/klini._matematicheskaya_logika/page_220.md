---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 108.18
tokens: 13655
characters: 5202
timestamp: 2025-12-24T05:42:24.599310
finish_reason: stop
---

**Глава VI. Исчисление предикатов (дополнительные разделы)**

ром, имеется формула \( R(x_1, \ldots, x_n, p_0, \ldots, p_s) \), такая, что
\[
\vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset 
\supset [Q(x_1, \ldots, x_n) \sim R(x_1, \ldots, x_n, p_0, \ldots, p_s)],
\]
т. е. \( E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \) делает Q явно определимым через \( p_0, \ldots, p_s \).

(b) Если ни один из \( p_0, \ldots, p_s \) не является предикатным параметром, входящим в \( E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \), то
либо \( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset Q(x_1, \ldots, x_n) \),
либо \( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset \neg Q(x_1, \ldots, x_n) \),
т. е. \( E(Q, p_0, \ldots, p_s, r_0, r_t) \) определяет Q либо как постоянный предикат «истина», либо как постоянный предикат «ложь».

Доказательство. Используя главное условие теоремы вместе с исчислением высказываний, имеем
(i) \( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \& Q(x_1, \ldots, x_n) \supset 
\supset [E(Q', p_0, \ldots, p_s, r_0', \ldots, r_t') \supset Q'(x_1, \ldots, x_n)] \).
Это утверждение мы берем в качестве \( \vdash E \supset F \) для интерполяционной теоремы Крейга (теорема 41).

(a1) Допустим, что один из \( p_0, \ldots, p_s \) есть один из предикатных параметров, входящих в \( E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \). Тогда в силу (a) теоремы 41 имеется формула I, такая, что \( \vdash E \supset I \) и \( \vdash I \supset F \) и I содержит лишь общие параметры формул E и F. Но это могут быть самое большое \( x_1, \ldots, x_n, p_0, \ldots, p_s \). Взяв это I в качестве \( R(x_1, \ldots, x_n, p_0, \ldots, p_s) \), мы удовлетворим структурные требования, и
(ii) \( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \& Q(x_1, \ldots, x_n) \supset 
\supset R(x_1, \ldots, x_n, p_0, \ldots, p_s) \),
(iii) \( \vdash R(x_1, \ldots, x_n, p_0, \ldots, p_s) \supset 
\supset [E(Q', p_0, \ldots, p_s, r_0', \ldots, r_t') \supset Q'(x_1, \ldots, x_n)] \).
Доказательство формулы в (iii) останется доказательством после подстановки Q, \( r_0, \ldots, r_t \) вместо \( Q', r_0', \ldots, r_t' \)1). Поэтому
(iv) \( \vdash R(x_1, \ldots, x_n, p_0, \ldots, p_s) \supset 
\supset [E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset Q(x_1, \ldots, x_n)] \).
Из (ii) и (iv) в силу исчисления высказываний
(v) \( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset 
\supset [Q(x_1, \ldots, x_n) \sim R(x_1, \ldots, x_n, p_0, \ldots, p_s)] \).
(a2) Если один из \( p_0, \ldots, p_s \) — предикатный параметр, но ни один предикатный параметр из списка \( p_0, \ldots, p_s \) не входит в

Если \( E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \), то применим (устанавливаемый ниже) результат (b), после чего можно тривиально построить \( R(x_1, \ldots, x_n, p_0, \ldots, p_s) \).
(b) Допустим, что ни один предикатный параметр из списка \( p_0, \ldots, p_s \) не входит в \( E(Q, p_0, \ldots, p_s; r_0, \ldots, r_t) \). Тогда по теореме 41 (b)
(vi-1) либо \( \vdash \neg [E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \& Q(x_1, \ldots, x_n)] \),
(vi-2) либо \( \vdash E(Q', p_0, \ldots, p_s, r_0', \ldots, r_t') \supset Q'(x_1, \ldots, x_n) \).
Применяя исчисление высказываний (*60, *49 или *58b) к (vi-1) и подставляя в (vi-2):
(vii-1) либо \( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset \neg Q(x_1, \ldots, x_n) \),
(vii-2) либо \( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset Q(x_1, \ldots, x_n) \).
Теперь рассмотрим случай исчисления предикатов с равенством и функциональными символами. Параметр q в методе Падоа может быть теперь либо n-местным предикатным символом Q, либо n-местным функциональным символом g (при \( n \geq 0 \)).

Теорема 44. (Теорема Бета об определимости для исчисления предикатов с равенством и функциями.) В исчислении предикатов с равенствами и функциями (при объясненных выше обозначениях):
(A) Если
\( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \& E(Q', p_0, \ldots, p_s, r_0', \ldots, r_t') \supset 
\supset [Q(x_1, \ldots, x_n) \sim Q'(x_1, \ldots, x_n)] \),
то имеется формула \( R(x_1, \ldots, x_n, p_0, \ldots, p_s) \), такая, что
\( \vdash E(Q, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset 
\supset [Q(x_1, \ldots, x_n) \sim R(x_1, \ldots, x_n, p_0, \ldots, p_s)] \).
(B) Если
\( \vdash E(g, p_0, \ldots, p_s, r_0, \ldots, r_t) \& E(g', p_0, \ldots, p_s, r_0', \ldots, r_t') \supset 
\supset g(x_1, \ldots, x_{n-1}) = g'(x_1, \ldots, x_{n-1}) \),
то имеется формула \( R(x_1, \ldots, x_n, p_0, \ldots, p_s) \), такая, что
\( \vdash E(g, p_0, \ldots, p_s, r_0, \ldots, r_t) \supset 
\supset [g(x_1, \ldots, x_{n-1}) = x_n \sim R(x_1, \ldots, x_n, p_0, \ldots, p_s)] \).
Доказательство. (a) Проводится, как и раньше, за исключением того, что теперь использование теоремы 42 дает нам \( R(x_1, \ldots, x_n, p_0, \ldots, p_s) \) во всех случаях.
(b) в исчислении предикатов с равенством \( g(x_1, \ldots, x_{n-1}) = g'(x_1, \ldots, x_{n-1}) \) будет эквивалентно \( g(x_1, \ldots, x_{n-1}) = x_n \sim g'(x_1, \ldots, x_{n-1}) = x_n \). Теперь применимы те же рассуждения, что и раньше, с использованием \( g(x_1, \ldots, x_{n-1}) = x_n \) вместо \( Q(x_1, \ldots, x_n) \). Теорема доказана.

1) См. примечание на стр. 159