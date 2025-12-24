---
source_image: page_126.png
page_number: 126
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.98
tokens: 7580
characters: 1882
timestamp: 2025-12-24T02:24:34.893970
finish_reason: stop
---

existing_words = set([word1, word2, word3])
closest_words = [word for word in closest_words
                 if word not in existing_words]

if len(closest_words) == 0:
    print("Could not find nearest neighbors for the vector!")
    return

for word4 in closest_words:
    print("{0} : {1} :: {2} : {3}".format(word1, word2, word3, word4))

Что интересно, с помощью простой словесной аналогии можно продемонстрировать, как вложения слов способны улавливать разнообразные семантические и синтаксические связи (пример 5.3).

Пример 5.3. Кодирование с помощью вложений слов множества лингвистических связей на примере задач на аналогии SAT

<table>
  <tr>
    <th>Input[0]</th>
    <td># Связь 1: связь между гендерно-дифференцированными существительными и местоимениями<br>embeddings.compute_and_print_analogy('man', 'he', 'woman')</td>
  </tr>
  <tr>
    <th>Output[0]</th>
    <td>man : he :: woman : she</td>
  </tr>
  <tr>
    <th>Input[1]</th>
    <td># Связь 2: связи "глагол — существительное"<br>embeddings.compute_and_print_analogy('fly', 'plane', 'sail')</td>
  </tr>
  <tr>
    <th>Output[1]</th>
    <td>fly : plane :: sail : ship</td>
  </tr>
  <tr>
    <th>Input[2]</th>
    <td># Связь 3: связи "существительное — существительное"<br>embeddings.compute_and_print_analogy('cat', 'kitten', 'dog')</td>
  </tr>
  <tr>
    <th>Output[2]</th>
    <td>cat : kitten :: dog : puppy</td>
  </tr>
  <tr>
    <th>Input[3]</th>
    <td># Связь 4: гиперонимия (обобщение)<br>embeddings.compute_and_print_analogy('blue', 'color', 'dog')</td>
  </tr>
  <tr>
    <th>Output[3]</th>
    <td>blue : color :: dog : animal</td>
  </tr>
  <tr>
    <th>Input[4]</th>
    <td># Связь 5: меронимия (отношение "часть — целое")<br>embeddings.compute_and_print_analogy('toe', 'foot', 'finger')</td>
  </tr>
  <tr>
    <th>Output[4]</th>
    <td>toe : foot :: finger : hand</td>
  </tr>
</table>