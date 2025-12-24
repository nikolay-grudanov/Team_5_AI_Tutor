---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.11
tokens: 11611
characters: 1539
timestamp: 2025-12-24T09:32:41.849794
finish_reason: stop
---

to Heaven, we were all going direct the other way—in short, the period wassofar like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.</p>
</blockquote>
<p>It's amazing what you can fit into one sentence…</p>

На рис. 5.9 показано, как этот текст выглядит в браузере.

![Элемент <blockquote> задает отступы для среднего абзаца](image.png)

Рис. 5.9. Элемент <blockquote> задает отступы для среднего абзаца

Порой разработчики используют элемент <blockquote> исключительно из-за его возможностей форматирования — им нравится, как он выводит на экран текст. Конечно, это дискредитирует идею элемента и лучше применять таблицы стилей для получения аналогичного результата.

Элемент <blockquote> — блочный, т. е. он всегда вставляется наравне с другими блочными элементами, такими как абзац или заголовки. У элемента <blockquote> есть одно дополнительное ограничение: он может содержать только другие блочные элементы, что означает необходимость помещать ваш текст в абзацы, а не просто вводить его между начальным и конечным тегами <blockquote>.

Если вместо длинной цитаты из одного или нескольких абзацев вы хотите вставить простую однстрочную цитату, HTML предоставит все необходимое. В нем определен строчный элемент для коротких цитат, которые можно вложить в блочный элемент. Это элемент <q> (сокращение от "quotation" — цитата):

<p>As Charles Dickens once wrote, <q>It was the best of times, it was the worst of times</q>.</p>