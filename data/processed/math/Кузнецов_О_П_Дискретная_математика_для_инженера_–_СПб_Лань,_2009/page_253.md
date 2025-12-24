---
source_image: page_253.png
page_number: 253
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.91
tokens: 5574
characters: 2783
timestamp: 2025-12-24T07:22:50.678876
finish_reason: stop
---

Полный перебор всех случаев для системы аксиом II можно найти в [20]. □

Теоремы исчисления высказываний в терминах истинности характеризуются довольно просто.

Теорема 6.3. Всякая теорема исчисления высказываний является тождественно-истинным высказыванием.

Тождественная истинность аксиом проверяется либо прямым вычислением на всех наборах, либо приведением их к константе 1 путем тождественных преобразований булевой алгебры. Очевидно, что любая подстановка в тождественно-истинную формулу также даст тождественно-истинную формулу.

Остается показать, что правило МР сохраняет тождественную истинность. Пусть формулы \( \mathfrak{A} \) и \( \mathfrak{A} \rightarrow \mathfrak{B} \) тождественно-истинны, т. е. \( \mathfrak{A} \equiv 1, \mathfrak{A} \rightarrow \mathfrak{B} \equiv 1 \).

Так как \( A \rightarrow B \equiv \neg A \lor B \), то \( 0 \lor \mathfrak{B} \equiv 1 \) и \( \mathfrak{B} \equiv 1 \), т. е. формула \( \mathfrak{B} \), выводимая из \( \mathfrak{A} \) и \( \mathfrak{A} \rightarrow \mathfrak{B} \) по правилу МР, также тождественно-истинна.

Итак, аксиомы тождественно-истинны, а правила вывода сохраняют тождественную истинность; поэтому любая доказуемая формула тождественно-истинна. □

Справедлива и обратная теорема.

Теорема 6.4. Всякая тождественно-истинная формула является теоремой исчисления высказываний.

Пусть \( \mathfrak{A}(A_1, ..., A_n) \) — тождественно-истинная формула. Тогда по теореме 6.2 \( A^{\sigma_1}, ..., A^{\sigma_n} \vdash \mathfrak{A} \) для всех \( 2^n \) наборов \( (\sigma_1, ..., \sigma_n) \). Применив \( n \) раз теорему дедукции, получим \( 2^n \) выводимостей

\[
\vdash A_1^{\sigma_1} \rightarrow (A_2^{\sigma_2} \rightarrow (... \rightarrow (A_n^{\sigma_n} \rightarrow \mathfrak{A}))...).
\]

Подставим в аксиому I 8 \( \neg A \) вместо \( B \). Получим \( (A \rightarrow C) \rightarrow ((\neg A \rightarrow C) \rightarrow ((A \lor \neg A) \rightarrow C)) \). Из этой формулы и правила МР (учитывая, что \( A \lor \neg A \) — теорема: см. пример 6.2, в) получаем производное правило: если \( \vdash A \rightarrow C \) и \( \vdash \neg A \rightarrow C \), то \( \vdash C \). Для любого набора \( (\sigma_2, ..., \sigma_n) \) имеем при \( \sigma_1 = 1 \vdash A_1 \rightarrow (A_2^{\sigma_2} \rightarrow (... \rightarrow (A_n^{\sigma_n} \rightarrow \mathfrak{A}))...) \), а при \( \sigma_1 = 0 \vdash \neg A_1 \rightarrow (A_2^{\sigma_2} \rightarrow (... \rightarrow (A_n^{\sigma_n} \rightarrow \mathfrak{A}))...) \). Применяя к этим формулам только что доказанное правило, получаем \( \vdash (A_2^{\sigma_2} \rightarrow ... \rightarrow (A_n^{\sigma_n} \rightarrow \mathfrak{A})...) \), т. е. первая посылка «длинной импликации» удалена. Применяя это удаление еще \( n - 1 \) раз, получаем \( \vdash \mathfrak{A} \). □