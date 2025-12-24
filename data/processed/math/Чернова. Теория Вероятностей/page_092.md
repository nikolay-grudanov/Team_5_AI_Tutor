---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.19
tokens: 11657
characters: 2076
timestamp: 2025-12-24T08:28:43.860769
finish_reason: stop
---

Заметим, что если с. в. одинаково распределены, то математические ожидания у них одинаковы (и равны, например, \( \mathbb{E} \xi_1 \)), поэтому свойство (22) можно записать в виде
\[
\frac{\xi_1 + \cdots + \xi_n}{n} \xrightarrow{p} \mathbb{E} \xi_1.
\]
Итак, законы больших чисел.

**Теорема 29 (ЗБЧ в форме Чебышёва).**

Для любой последовательности независимых и одинаково распределенных случайных величин с конечным вторым моментом \( \mathbb{E} \xi_1^2 < \infty \) имеет место сходимость:
\[
\frac{\xi_1 + \cdots + \xi_n}{n} \xrightarrow{p} \mathbb{E} \xi_1.
\]

ЗБЧ утверждает, что среднее арифметическое большого числа случайных слагаемых «стабилизируется» с ростом этого числа. Как бы сильно каждая с. в. не отклонялась от своего среднего значения, при суммировании эти отклонения «взаимно гасятся», так что среднее арифметическое приближается к постоянной величине.

В дальнейшем мы увидим, что требование конечности второго момента (или дисперсии) связано исключительно со способом доказательства, и что утверждение остается верным если требовать существования только первого момента.

**Доказательство.** Обозначим через \( S_n = \xi_1 + \cdots + \xi_n \) сумму первых \( n \) с. в., а через \( \frac{S_n}{n} = \frac{\xi_1 + \cdots + \xi_n}{n} \) — их среднее арифметическое. Тогда
\[
\mathbb{E} \left( \frac{S_n}{n} \right) = \frac{\mathbb{E} \xi_1 + \cdots + \mathbb{E} \xi_n}{n} = \frac{n \cdot \mathbb{E} \xi_1}{n} = \mathbb{E} \xi_1.
\]
Пусть \( \varepsilon > 0 \). Воспользуемся неравенством Чебышёва (следствие 16):
\[
\mathbb{P} \left( \left| \frac{S_n}{n} - \mathbb{E} \left( \frac{S_n}{n} \right) \right| > \varepsilon \right) \leq \frac{\mathbb{D} \left( \frac{S_n}{n} \right)}{\varepsilon^2} =
\]
\[
= \frac{\mathbb{D} S_n}{n^2 \varepsilon^2} \stackrel{\text{независ.}}{=} \frac{\mathbb{D} \xi_1 + \cdots + \mathbb{D} \xi_n}{n^2 \varepsilon^2} \stackrel{\text{ог.распрег.}}{=} \frac{n \mathbb{D} \xi_1}{n^2 \varepsilon^2} = \frac{\mathbb{D} \xi_1}{n \varepsilon^2} \to 0
\]
при \( n \to \infty \), поскольку \( \mathbb{D} \xi_1 \), по условию, конечна. □