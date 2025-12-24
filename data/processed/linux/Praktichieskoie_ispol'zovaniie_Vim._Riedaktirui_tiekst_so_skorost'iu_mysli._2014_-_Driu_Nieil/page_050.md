---
source_image: page_050.png
page_number: 50
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.64
tokens: 5864
characters: 2296
timestamp: 2025-12-24T04:10:46.943360
finish_reason: stop
---

Будьте экономны: выполняйте поиск без ввода лишних символов

Возможно, вы уже догадались, что команда «точка» — моя любимица. На втором месте у меня стоит команда *. Она выполняет поиск слова под курсором (см. :h * http://vimdoc.sourceforge.net/htmldoc/pattern.html#star).

Мы можем выполнить поиск слова «content», напечатав его в строке приглашения к вводу:

⇒ /content

или просто поместив курсор в требуемое слово и нажав клавишу *. Взгляните, как выглядит весь процесс:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>...We’re waiting for content before the site can go live...<br>...If you are content with this, let’s go ahead with it...<br>...We’ll launch as soon as we have the content...</td>
  </tr>
  <tr>
    <td>*</td>
    <td>...We’re waiting for content before the site can go live...<br>...If you are content with this, let’s go ahead with it...<br>...We’ll launch as soon as we have the content...</td>
  </tr>
  <tr>
    <td>cwcopy<Esc></td>
    <td>...We’re waiting for content before the site can go live...<br>...If you are content with this, let’s go ahead with it...<br>...We’ll launch as soon as we have the copy...</td>
  </tr>
  <tr>
    <td>n</td>
    <td>...We’re waiting for content before the site can go live...<br>...If you are content with this, let’s go ahead with it...<br>...We’ll launch as soon as we have the content...</td>
  </tr>
  <tr>
    <td>.</td>
    <td>...We’re waiting for copy before the site can go live...<br>...If you are content with this, let’s go ahead with it...<br>...We’ll launch as soon as we have the content...</td>
  </tr>
</table>

Процесс начинается с установки курсора в слово «content», после чего вызывается команда * поиска. Попробуйте сами выполнить это упражнение. В результате случится следующее: курсор перепрыгнет вперед, к следующему совпадению, и все найденные вхождения будут выделены цветом. Если вы не увидите подсвеченные совпадения, попробуйте выполнить команду :set hls и затем обратиться к рецепту 80 в главе 13 за более подробными разъяснениями.

Выполнив поиск слова «content», перейти к следующему совпадению можно простым нажатием клавиши n. В данном случае нажатие *nn выполнит обход всех совпадений и вернет нас туда, откуда мы начали.