---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.27
tokens: 5715
characters: 3149
timestamp: 2025-12-24T07:22:53.832686
finish_reason: stop
---

2. Из \( A \rightarrow (B \rightarrow C) \) и аксиомы II 2 по правилу МР следует \( (A \rightarrow B) \rightarrow (A \rightarrow C) \); следовательно,
\[
B \rightarrow C \vdash (A \rightarrow B) \rightarrow (A \rightarrow C).
\]
3. Из \( (A \rightarrow B) \) и \( (A \rightarrow B) \rightarrow (A \rightarrow C) \) по правилу МР следует \( A \rightarrow C \); учитывая 2, получаем искомую выводимость.
При переходе от 1 к 2 неявно использовалось следующее свойство выводимости: если \( \Gamma \vdash \mathcal{A} \) (\( \Gamma \) — список формул), а \( \mathcal{A} \vdash \mathcal{B} \), то \( \Gamma \vdash \mathcal{B} \). Это свойство (транзитивность отношения выводимости) непосредственно следует из определения выводимости.

Основные метатеоремы исчисления высказываний. Для получения выводов в исчислении высказываний оказывается крайне полезной следующая метатеорема.

Теорема 6.1а (теорема дедукции).
Если \( \Gamma, \mathcal{A} \vdash \mathcal{B} \), то \( \Gamma \vdash \mathcal{A} \rightarrow \mathcal{B} \) (\( \Gamma \) — множество формул, \( \mathcal{A}, \mathcal{B} \) — формулы).

Будем исходить из систем аксиом II и рассматривать их как схемы аксиом (т. е. не пользоваться правилом подстановки).

Пусть \( \Gamma, \mathcal{A} \vdash \mathcal{B} \). Тогда существует вывод \( \mathcal{B}_1, ..., \mathcal{B}_n \) из \( \Gamma, \mathcal{A} \), такой, что \( \mathcal{B}_n = \mathcal{B} \). Докажем по индукции, что для любого \( k \leq n \) \( \Gamma \vdash \mathcal{A} \rightarrow \mathcal{B}_k \).

Рассмотрим сначала \( \mathcal{B}_1 \). \( \mathcal{B}_1 \), как первая формула вывода, должна либо быть аксиомой, либо содержаться в \( \Gamma \), либо совпадать с \( \mathcal{A} \). Из схемы аксиом II 1 следует, что \( \mathcal{B}_1 \rightarrow (\mathcal{A} \rightarrow \mathcal{B}_1) \) является аксиомой. Если \( \mathcal{B}_1 \) — аксиома или содержится в \( \Gamma \), то по правилу МР \( \mathcal{A} \rightarrow \mathcal{B}_1 \) выводима из \( \Gamma \). Если же \( \mathcal{B}_1 = \mathcal{A} \), то из примера 6.7, а имеем \( \mathcal{A} \rightarrow \mathcal{A} \), т. е. \( \mathcal{A} \rightarrow \mathcal{B}_1 \). В любом случае получаем \( \Gamma \vdash \mathcal{A} \rightarrow \mathcal{B}_1 \).

Предположим теперь, что \( \Gamma \vdash \mathcal{A} \rightarrow \mathcal{B}_i \) для любого \( i < k \), и рассмотрим \( \mathcal{B}_k \). Возможны четыре случая: а) \( \mathcal{B}_k \) — аксиома; б) \( \mathcal{B}_k \in \Gamma \); в) \( \mathcal{B}_k = \mathcal{A} \); г) \( \mathcal{B}_k \) выводимо из некоторых предшествующих формул \( \mathcal{B}_j, \mathcal{B}_l \) по правилу МР; но тогда \( \mathcal{B}_l \) должно иметь вид \( \mathcal{B}_j \rightarrow \mathcal{B}_k \). В случаях «а»—«в» доказательство точно такое же, как и для \( \mathcal{B}_1 \) (случаи «а», «б» — с помощью аксиомы II 1; случай «в» — с помощью примера 6.1, а). В случае «г» по индуктивному предположению имеем:
\[
\Gamma \vdash \mathcal{A} \rightarrow \mathcal{B}_j \tag{6.1}
\]
и \( \Gamma \vdash \mathcal{A} \rightarrow \mathcal{B}_l \), т. е.
\[
\Gamma \vdash \mathcal{A} \rightarrow (\mathcal{B}_j \rightarrow \mathcal{B}_k). \tag{6.2}
\]