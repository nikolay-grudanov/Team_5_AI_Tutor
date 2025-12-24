---
source_image: page_299.png
page_number: 299
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.51
tokens: 5545
characters: 1438
timestamp: 2025-12-24T04:15:47.444099
finish_reason: stop
---

обратное значение). Каждая из них применит указанную команду [cmd] к каждой строке, не соответствующей заданному шаблону. В следующем рецепте будут представлены примеры использования обеих команд, :global и :vglobal.

Команда :global выполняет обработку строк в указанном диапазоне [range] в два прохода. На первом проходе отмечаются строки, соответствующие шаблону {pattern}. На втором проходе к отмеченным строкам применяется команда [cmd]. Команда [cmd] может принимать собственный диапазон, что дает возможность воздействовать на многострочные области. Этот мощнейший прием демонстрируется в рецепте 100.

Рецепт 98. Удаление строк, соответствующих шаблону

Комбинация команд :global и :delete позволяет быстро сокращать файлы в размерах. С помощью этой комбинации можно удалить или оставить строки, соответствующие шаблону {pattern}.

Следующий файл содержит ссылки на первые несколько видео-уроков в архиве сайта Vimcasts.org:

global/episodes.html
http://media.pragprog.com/titles/dnvim/code/global/episodes.html

<ol>
<li>
<a href="/episodes/show-invisibles/">Show invisibles</a>
</li>
<li>
<a href="/episodes/tabs-and-spaces/">Tabs and Spaces</a>
</li>
<li>
<a href="/episodes/whitespace-preferences-and-filetypes/">Whitespace preferences and filetypes</a>
</li>
</ol>

Каждый элемент списка состоит из двух частей: названия видео-урока и его адреса URL. Мы собираемся использовать команду :global для выявления каждой из частей.