---
source_image: page_224.png
page_number: 224
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 83.35
tokens: 12897
characters: 4513
timestamp: 2025-12-24T05:42:21.577114
finish_reason: stop
---

Теорема 1 (о нормальной форме в G4a). По всякому доказательству в G4a с сечением можно построить доказательство той же секвенции, не содержащее сечений.

Для данного доказательства через k обозначим максимальную степень сечения, а через F — список формул сечения, имеющих степень k.

Теорема доказывается индукцией по k. Как базис, так и индукционный переход обосновываются индукцией по числу членов списка F (внутренняя индукция). Базис внутренней индукции очевиден: в случае k = 0 данное доказательство уже не содержит сечений, а в случае k > 0 данное доказательство является (k-1, G)-доказательством для некоторого списка G. Индукционный переход внутренней индукции проводится с помощью леммы 2 (при k = 0) и леммы 3 (при k > 0). Теорема доказана.

Пример. Рассмотрим следующее рассуждение, обосновывающее формулу \( \exists x \forall y (P(x) \lor \neg P(y)) \): если \( \exists x P(x) \), то \( \forall y (P(a) \lor \neg P(y)) \), где a — такой объект, что P(a). Если же \( \neg \exists x P(x) \), то для любого d имеет место \( \neg P(d) \) и, значит, при любом c \( \forall y (P(c) \lor \neg P(y)) \). В обоих случаях имеем \( \exists x \forall y (P(x) \lor \neg P(y)) \).
Соответствующее доказательство в G4a с сечением таково:

\[
\begin{array}{ll}
P(g) \rightarrow P(g), \exists x P(x) \\
\hline
P(g) \rightarrow \exists x P(x)
\end{array}
\]

1. \( \exists x P(x) \rightarrow \exists x P(x) \)
\[
\begin{array}{ll}
\rightarrow \exists x P(x), \neg \exists x P(x) \\
\hline
\rightarrow \exists x P(x) \lor \neg \exists x P(x)
\end{array}
\]
0. \( \rightarrow \exists x P(x) \lor \neg \exists x P(x) \)
\[
\begin{array}{ll}
P(a) \rightarrow E, P(a), \neg P(b) \\
\hline
P(a) \rightarrow E, P(a) \lor \neg P(b)
\end{array}
\]
\[
\begin{array}{ll}
P(a) \rightarrow E, \forall y (P(a) \lor \neg P(y)) \\
\hline
P(a) \rightarrow \exists x \forall y (P(x) \lor \neg P(y))
\end{array}
\]
2. \( \exists x P(x) \rightarrow \exists x \forall y (P(x) \lor \neg P(y)) \)
\[
\begin{array}{ll}
0. \exists x P(x) \lor \neg \exists x P(x) \rightarrow \exists x \forall y (P(x) \lor \neg P(y)) \\
\hline
\rightarrow \exists x \forall y (P(x) \lor \neg P(y))
\end{array}
\]
[Через E обозначена доказываемая формула \( \exists x \forall y (P(x) \lor \neg P(y)) \).]
Устраняем (единственное) сечение, заменяя его двумя сечениями по подформулам старой формулы сечения:
1. \( \exists x P(x) \rightarrow \exists x P(x) \)
\[
\begin{array}{ll}
\rightarrow \exists x P(x), \neg \exists x P(x) \\
\hline
\rightarrow \neg \exists x P(x), E
\end{array}
\]
2. \( \exists x P(x) \rightarrow E \)
3. \( \rightarrow E, \exists x P(x) \)
\[
\begin{array}{ll}
\rightarrow \neg \exists x P(x), E \\
\hline
\rightarrow E
\end{array}
\]
(Сеч. Сокр.)

Имеется в виду, что над секвенциями 1, 2, 3 надписаны их доказательства.
Согласно доказательству теоремы о нормальной форме, устраним сечение наибольшей степени, т. е. \( \neg \exists x P(x) \)-сечение:
1. \( \exists x P(x) \rightarrow \exists x P(x) \)
2. \( \exists x P(x) \rightarrow E \)
3. \( \rightarrow E, \exists x P(x) \)
\[
\begin{array}{ll}
\rightarrow E \\
\hline
\rightarrow E
\end{array}
\]
Вычеркнем верхнее \( \exists x P(x) \)-сечение, воспользовавшись тем, что его левая посылка имеет вид C → C, так что заключение совпадает с правой посылкой.
\[
\begin{array}{ll}
P(d) \rightarrow E, P(c), \exists x P(x), P(d) \\
\hline
P(d) \rightarrow E, P(c), \exists x P(x) \\
\rightarrow E, P(c), \neg P(d), \exists x P(x) \\
\rightarrow E, P(c) \lor \neg P(d), \exists x P(x) \\
\rightarrow E, \forall y (P(c) \lor \neg P(y)), \exists x P(x) \\
3. \rightarrow E, \exists x P(x) \\
\hline
5. P(a) \rightarrow E \\
2. \exists x P(x) \rightarrow E \quad (\text{Сеч. Сокр.})
\end{array}
\]
Устраняем оставшееся \( \exists x P(x) \)-сечение, заменяя a на d в выводе секвенции 5:
\[
\begin{array}{ll}
P(d) \rightarrow E, P(c), P(d) \quad 5'. P(d) \rightarrow E \\
\hline
P(d) \rightarrow E, P(c) \\
\rightarrow E, P(c), \neg P(d) \\
\rightarrow E, P(c) \lor \neg P(d) \\
\rightarrow E, \forall y (P(c) \lor \neg P(y)) \\
\rightarrow E
\end{array}
\]
Наконец, устраняем последнее P(d)-сечение по лемме 2 и получаем вывод без сечения:
\[
\begin{array}{ll}
P(d) \rightarrow E, P(d), \neg P(b), P(c) \\
P(d) \rightarrow E, P(d) \lor \neg P(b), P(c) \\
P(d) \rightarrow E, \forall y (P(d) \lor \neg P(y)), P(c) \\
P(d) \rightarrow E, P(c) \\
\rightarrow E, P(c), \neg P(d) \\
\rightarrow E, P(c) \lor \neg P(d) \\
\rightarrow E, \forall y (P(c) \lor \neg P(y)) \\
\rightarrow E
\end{array}
\]