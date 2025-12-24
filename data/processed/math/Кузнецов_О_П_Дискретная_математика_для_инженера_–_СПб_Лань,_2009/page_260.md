---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.29
tokens: 5438
characters: 2231
timestamp: 2025-12-24T07:23:01.077460
finish_reason: stop
---

Продемонстрируем это доказательство на примере.
Пусть \( F(A) = \forall y(P_1(y) \lor \neg \exists x P_2(x, y)) \), \( A = \neg \exists x P_2(x, y) \).
В качестве эквивалентности \( A \sim B \) возьмем эквивалентность \( \neg \exists x P_2(x, y) \sim \forall x \neg P_2(x, y) \), верную в логике предикатов [см. соотношение (3.31)] и, следовательно, в силу теоремы 6.7 доказуемую в исчислении предикатов.
1. \( \neg \exists P_2(x, y) \sim \forall x \neg P_2(x, y) \) (исходная эквивалентность \( A \sim B \)).
2. \( (P_1(y) \lor \neg \exists x P_2(x, y)) \sim (P_1(y) \lor \forall x \neg P_2(x, y)) \) (правило 2).
3. \( \forall y(P_1(y) \lor \neg \exists x P_2(x, y)) \sim \forall y(P_1(y) \lor \forall x \neg P_2(x, y)) \) (правило 5).
Формула из шага 3 и есть искомая эквивалентность \( F(A) \sim F(B) \).
Приведем теперь без доказательства некоторые важные эквивалентности, выводимые в исчислении предикатов (в них \( A \) и \( B \) — формулы, не содержащие свободных вхождений \( x \)):

\[
A \& \forall x F(x) \sim \forall x (A \& F(x)); \tag{6.5}
\]
\[
A \lor \exists x F(x) \sim \exists x (A \lor F(x)); \tag{6.6}
\]
\[
A \& \exists x F(x) \sim \exists x (A \& F(x)); \tag{6.7}
\]
\[
A \lor \forall x F(x) \sim \forall x (A \lor F(x)); \tag{6.8}
\]
\[
A \rightarrow \forall x F(x) \sim \forall x (A \rightarrow F(x)); \tag{6.9}
\]
\[
A \rightarrow \exists x F(x) \sim \exists x (A \rightarrow F(x)); \tag{6.10}
\]
\[
\forall x F(x) \rightarrow B \sim \exists x (F(x) \rightarrow B)); \tag{6.11}
\]
\[
\exists x F(x) \rightarrow B \sim \forall x (F(x) \rightarrow B)). \tag{6.12}
\]

Эквивалентности (6.5)-(6.12), а также полученные ранее эквивалентности (3.33) и (3.34) позволяют выносить кванторы вперед. Используя при этом соотношения (3.31) и (3.32), позволяющие заменять один квантор другим и «спускать» отрицание внутрь области действия квантора, а также правила переименования переменных (примеры 6.3, а, б), кванторы можно вынести вперед для любой формулы. Формула, имеющая вид \( Q_1 x_1 Q_2 x_2 ... Q_n x_n F \), где \( Q_1, ..., Q_n \) — кванторы, а \( F \) — формула, не имеющая кванторов (и являющаяся областью действия всех \( n \) кванторов), называется предваренной формой, или формулой в предваренной форме.