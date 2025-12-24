---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.67
tokens: 7629
characters: 2165
timestamp: 2025-12-24T02:22:15.145233
finish_reason: stop
---

Наконец, рассмотрим следующий твит.

![Твит с текстом: #Jesus @TheLordHasSpoke · 2h Snow White and the Seven Degrees #MakeAMovieCold @midnight](https://i.imgur.com/3Q5z5QG.png)

Токенизация твитов требует сохранения хештегов и дескрипторов имен пользователей, а также трактовки смайликов, таких как :-), и URL в качестве одного элемента. Следует ли рассматривать хештег #MakeAMovieCold как один токен или четыре? Большинство научных статей не уделяет особого внимания подобным вопросам, да и вообще, правила токенизации зачастую выбираются произвольно, хотя на практике выбор влияет на точность больше, чем можно предположить. Большинство пакетов NLP с открытым исходным кодом учитывают сложность работы по предварительной обработке данных и предоставляют неплохие инструменты для токенизации. Пример 2.1 демонстрирует листинги из двух часто применяемых пакетов обработки текстов — NLTK (http://www.nltk.org/) и spaCy¹ (https://spacy.io/).

Пример 2.1. Токенизация текста

<table>
  <tr>
    <th>Input[0]</th>
    <td>
      import spacy<br>
      nlp = spacy.load('en')<br>
      text = "Mary, don't slap the green witch"<br>
      print([str(token) for token >in nlp(text.lower())])
    </td>
  </tr>
  <tr>
    <th>Output[0]</th>
    <td>
      ['mary', ',', 'do', "n't", 'slap', 'the', 'green', 'witch', '.']
    </td>
  </tr>
  <tr>
    <th>Input[1]</th>
    <td>
      from nltk.tokenize import TweetTokenizer<br>
      tweet=u"Snow White and the Seven Degrees #MakeAMovieCold@midnight:-)"<br>
      tokenizer = TweetTokenizer()<br>
      print(tokenizer.tokenize(tweet.lower()))
    </td>
  </tr>
  <tr>
    <th>Output[1]</th>
    <td>
      ['snow', 'white', 'and', 'the', 'seven', 'degrees', '#makeamoviecold', '@midnight', ':-)']
    </td>
  </tr>
</table>

Уникальные токены из корпуса называются типами. Множество всех типов в корпусе называется его словарем (vocabulary) или лексиконом (lexicon). Слова делятся на значимые (content words) и стоп-слова (stopwords). Такие стоп-слова,

¹ Для их использования понадобится не только установить соответствующие пакеты, но и отдельно загрузить модель en для spaCy: python -m spacy download en. — Примеч. пер.