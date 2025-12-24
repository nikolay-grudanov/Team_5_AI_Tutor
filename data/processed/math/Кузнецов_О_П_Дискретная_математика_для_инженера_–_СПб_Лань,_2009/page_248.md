---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.41
tokens: 5267
characters: 2141
timestamp: 2025-12-24T07:22:39.109341
finish_reason: stop
---

а не конкретные тождества, верные лишь для конкретных букв. Правило подстановки при этом подразумевается (см. гл. 3, § 3.2). Впрочем, достаточно очевидно, что переход от одного способа построения исчислений к другому не представляет труда.

Рассмотрим теперь примеры вывода в исчислении высказываний.

Пример 6.1. а. Покажем, что формула \( A \rightarrow A \) выводима из системы аксиом II:

\[
\vdash A \rightarrow A.
\]

1. \( (A \rightarrow ((A \rightarrow A) \rightarrow A)) \rightarrow ((A \rightarrow (A \rightarrow A)) \rightarrow (A \rightarrow A)) \)
(подстановка в аксиому II 2 \( A \rightarrow A \) вместо \( B \) и \( A \) вместо \( C \)).

2. \( A \rightarrow ((A \rightarrow A) \rightarrow A \) (подстановка в II 1 \( A \rightarrow A \) вместо \( B \)).

3. \( (A \rightarrow (A \rightarrow A)) \rightarrow (A \rightarrow A) \) (из шагов 2, 1 по правилу МР).

4. \( A \rightarrow (A \rightarrow A) \) (подстановка в II 1 \( A \) вместо \( B \)).

5. \( A \rightarrow A \) (из шагов 4, 3 по правилу МР).

б. \( A \vdash B \rightarrow A \).

Пусть \( A \) выводима. Тогда из \( A \) и аксиомы II 1 по правилу заключения получаем

\[
\frac{A,\ A \rightarrow (B \rightarrow A)}{B \rightarrow A},
\]

что и доказывает искомую выводимость.

Как уже отмечалось ранее, всякую доказанную в исчислении выводимость вида \( \Gamma \vdash \mathfrak{A} \), где \( \Gamma \) — список формул, \( \mathfrak{A} \) — формула, можно рассматривать как правило вывода

\[
\frac{\Gamma}{\mathfrak{A}},
\]

которое можно присоединить к уже имеющимся. Полученный нами вывод \( A \vdash B \rightarrow A \) вместе с правилом подстановки можно рассматривать как правило

\[
\frac{\mathfrak{A}}{\mathfrak{B} \rightarrow \mathfrak{A}}:
\]

«если формула \( \mathfrak{A} \) выводима, то выводима и формула \( \mathfrak{B} \rightarrow \mathfrak{A} \), где \( \mathfrak{B} \) — любая формула». Воспользуемся этим правилом в следующем примере.

в. \( A \rightarrow B, B \rightarrow C \vdash A \rightarrow C \).

1. \( B \rightarrow C \vdash A \rightarrow (B \rightarrow C) \), по новому правилу

\[
\frac{\mathfrak{A}}{\mathfrak{B} \rightarrow \mathfrak{A}}.
\]