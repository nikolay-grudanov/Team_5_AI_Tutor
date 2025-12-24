---
source_image: page_184.png
page_number: 184
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.50
tokens: 7782
characters: 2592
timestamp: 2025-12-24T02:26:18.894452
finish_reason: stop
---

**Judge Sentence**

You have already judged 14 of 3064 sentences, taking 86.4 seconds per sentence.

Source: les deux pays constituent plutôt un laboratoire nécessaire au fonctionnement interne de l’ue.

Reference: rather, the two countries form a laboratory needed for the internal working of the eu.

<table>
  <tr>
    <th>Translation</th>
    <th>Adequacy</th>
    <th>Fluency</th>
  </tr>
  <tr>
    <td>both countries are rather a necessary laboratory the internal operation of the eu.</td>
    <td>1 2 3 4 5</td>
    <td>1 2 3 4 5</td>
  </tr>
  <tr>
    <td>both countries are a necessary laboratory at internal functioning of the eu.</td>
    <td>1 2 3 4 5</td>
    <td>1 2 3 4 5</td>
  </tr>
  <tr>
    <td>the two countries are rather a laboratory necessary for the internal workings of the eu.</td>
    <td>1 2 3 4 5</td>
    <td>1 2 3 4 5</td>
  </tr>
  <tr>
    <td>the two countries are rather a laboratory for the internal workings of the eu.</td>
    <td>1 2 3 4 5</td>
    <td>1 2 3 4 5</td>
  </tr>
  <tr>
    <td>the two countries are rather a necessary laboratory internal workings of the eu.</td>
    <td>1 2 3 4 5</td>
    <td>1 2 3 4 5</td>
  </tr>
</table>

Annotator: Philipp Koehn Task: WMT06 French-English

Instructions

5= All Meaning
4= Most Meaning
3= Much Meaning
2= Little Meaning
1= None

5= Flawless English
4= Good English
3= Non-native English
2= Disfluent English
1= Incomprehensible

Рис. 8.10. Процесс оценки эффективности работы модели человеком (предоставлено Филиппом Кёном)

С другой стороны, автоматическая оценка проста и выполняется очень быстро. Существует два вида метрик для автоматической оценки сгенерированных предложений: метрики на основе пересечения n-грамм (n-gram overlap-based metrics) и перплексия (perplexity). Мы вновь воспользуемся в качестве примера машинным переводом, но эти метрики применимы к любой задаче, связанной с генерацией последовательностей. Метрики на основе пересечения n-грамм оценивают близость выходных данных к эталонным, вычисляя сводный показатель пересечения n-грамм. Примеры метрик на основе пересечения n-грамм: BLEU, ROUGE и METEOR. Из этих трех наиболее проверенной временем и предпочитаемой в литературе по машинному переводу является BLEU (BiLingual Evaluation Understudy)¹. Мы не станем приводить здесь точную формулировку BLEU и рекомендуем вам обратиться к статье Папинени и др. (Papineni et al., 2002). На практике

¹ Настолько, что исходная статья, в которой BLEU была предложена, получила в 2018 году премию Test-of-Time (https://naacl2018.wordpress.com/2018/03/22/test-of-time-award-papers/).