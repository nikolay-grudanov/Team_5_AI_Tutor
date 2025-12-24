---
source_image: page_246.png
page_number: 246
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.06
tokens: 5230
characters: 2204
timestamp: 2025-12-24T07:22:35.340281
finish_reason: stop
---

Система аксиом I.
I 1. \( A \rightarrow (B \rightarrow A) \);
I 2. \( (A \rightarrow B) \rightarrow ((A \rightarrow (B \rightarrow C)) \rightarrow (A \rightarrow C)) \);
I 3. \( (A \& B) \rightarrow A \);
I 4. \( (A \& B) \rightarrow B \);
I 5. \( A \rightarrow (B \rightarrow (A \& B)) \);
I 6. \( A \rightarrow (A \vee B) \);
I 7. \( B \rightarrow (A \vee B) \);
I 8. \( (A \rightarrow C) \rightarrow ((B \rightarrow C) \rightarrow ((A \vee B) \rightarrow C)) \);
I 9. \( (A \rightarrow B) \rightarrow ((A \rightarrow \neg B) \rightarrow \neg A) \);
I 10. \( \neg \neg A \rightarrow A \).

Другая система использует только две связки \( \neg \) и \( \rightarrow \); при этом сокращается алфавит исчисления (выбрасываются знаки \( \vee, \& \)) и, соответственно, определение формулы. Операции \( \vee, \& \) рассматриваются не как связки исчисления высказываний, а как сокращения (употреблять которые удобно, но не обязательно) для некоторых его формул: \( A \vee B \) заменяет \( \neg A \rightarrow B \), \( A \& B \) заменяет \( \neg (A \rightarrow \neg B) \). В результате система аксиом становится намного компактнее.

Система аксиом II.
II 1. \( A \rightarrow (B \rightarrow A) \);
II 2. \( (A \rightarrow (B \rightarrow C)) \rightarrow ((A \rightarrow B) \rightarrow (A \rightarrow C)) \);
II 3. \( (\neg A \rightarrow \neg B) \rightarrow ((\neg A \rightarrow B) \rightarrow A) \).

Приведенные системы аксиом равносильны в том смысле, что порождают одно и то же множество формул. Разумеется, такое утверждение нуждается в доказательстве, которое заключается в том, что показывается выводимость всех аксиом системы II из аксиом системы I и, наоборот, системы I из системы II (с учетом замечаний относительно \( \vee \) и \( \& \)). Доказательство этих выводимостей предоставляется читателю после того, как он познакомится с примерами вывода в исчислении высказываний (см. также пример 6.2, а).

Возможны и другие системы аксиом, равносильные первым двум системам.

Какая из систем лучше? Это зависит от точки зрения. Система II компактнее и обозримее; соответственно более компактны и доказательства различных ее свойств. С другой стороны, в более богатой системе I короче выводы различных формул.