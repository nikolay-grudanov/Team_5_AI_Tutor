---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.10
tokens: 5456
characters: 2473
timestamp: 2025-12-24T07:22:46.981143
finish_reason: stop
---

Подставив в схему аксиом II 2 \( \mathfrak{B}_j \) вместо \( \mathfrak{B} \) и \( \mathfrak{B}_k \) вместо \( \mathfrak{C} \), получим:

\[
(\mathfrak{A} \rightarrow (\mathfrak{B}_j \rightarrow \mathfrak{B}_k)) \rightarrow ((\mathfrak{A} \rightarrow \mathfrak{B}_j) \rightarrow (\mathfrak{A} \rightarrow \mathfrak{B}_k)). \tag{6.3}
\]

Применив правило МР к (6.2) и (6.3), получим:

\[
\Gamma \vdash (\mathfrak{A} \rightarrow \mathfrak{B}_j) \rightarrow (\mathfrak{A} \rightarrow \mathfrak{B}_k), \tag{6.4}
\]

а применив то же правило к (6.1) и (6.4), имеем: \( \Gamma \vdash \mathfrak{A} \rightarrow \mathfrak{B}_k \). Остается положить \( k = n \). \( \Box \)

Отметим, что при построении выводов использовались только аксиомы II 1 и II 2, которые содержатся и в системе аксиом I. Поэтому приведенное доказательство теоремы дедукции справедливо и для исчисления высказываний, основанного на системе I.

Теорема 6.1б. (обратная теорема о дедукции). Если существует вывод \( \Gamma \vdash A \rightarrow B \), то формула \( B \) выводима из \( \Gamma \) и \( A \), т. е. если \( \Gamma \vdash A \rightarrow B \), то \( \Gamma, A \vdash B \).

Доказательство. Пусть вывод формулы \( A \rightarrow B \) имеет вид: \( B_1, ..., B_{n-1}, A \rightarrow B \), где \( B_1, ..., B_{n-1} \) — формулы из множества \( \Gamma \). Тогда вывод формулы \( B \) из \( \Gamma \) и \( A \) будет иметь вид: \( B_1, ..., B_{n-1}, A \rightarrow B, A, B \), так как \( B \) следует из \( A \rightarrow B \) и \( A \) по правилу МР. \( \Box \)

Пример 6.2. а. В качестве первого применения теоремы дедукции покажем, что аксиома II 3 выводима из системы аксиом I.
1. Подставим в I 9 \( \neg A \) вместо \( A \). Получим:

\[
(\neg A \rightarrow B) \rightarrow ((\neg A \rightarrow \neg B) \rightarrow \neg \neg A).
\]

2. Двойное применение теоремы 6.1б к шагу 1 дает:

\[
\neg A \rightarrow B, \neg A \rightarrow \neg B \vdash \neg \neg A.
\]

3. Так как из аксиомы I 10 следует по правилу МР, что \( \neg \neg A \vdash A \), то по транзитивности выводимости (см. замечание к примеру 6.1, в) получим \( \neg A \rightarrow B; \neg A \rightarrow \neg B \vdash A \).

4. Переставим гипотезы в полученной выводимости (их порядок не важен, как видно из определения выводимости):

\[
\neg A \rightarrow \neg B; \neg A \rightarrow B \vdash A.
\]

5. Применив 2 раза к шагу 4 теорему дедукции, получим аксиому II 3:

\[
(\neg A \rightarrow \neg B) \rightarrow ((\neg A \rightarrow B) \rightarrow A).
\]