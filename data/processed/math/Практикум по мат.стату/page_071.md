---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.35
tokens: 6342
characters: 2443
timestamp: 2025-12-24T07:39:46.875324
finish_reason: stop
---

7. Примеры

Оценка вероятности успеха \( \hat{p} \) в ячейке К4 вычисляется по формуле

СУММПРОИЗВ (B2:B12; C2:C12)/(K1*K2)

В ячейке Н14 вычисляется наблюдаемое значение статистики, команда СУММ (H2:H12) — сумма значений по строкам столбца Н. Получено значение \( \chi^2_{\text{набл}} = 7164,54 \).

Так как в 1, 2, 3 и 11 группах (ячейки E2–E4 и E12) теоретическая частота \( n p_i < 5 \), то группы 1, 2 и 3 объединяем с 4-й, а группу 11 объединяем с 10-й. В результате, получим

<table>
  <tr>
    <th>A</th>
    <th>B</th>
    <th>C</th>
    <th>D</th>
    <th>E</th>
    <th>R</th>
    <th>G</th>
    <th>H</th>
  </tr>
  <tr>
    <th>i</th>
    <th>x<sub>i</sub></th>
    <th>n<sub>i</sub></th>
    <th>p<sub>i</sub></th>
    <th>N*p<sub>i</sub></th>
    <th>n<sub>i</sub> – Np<sub>i</sub></th>
    <th>(n<sub>i</sub> – Np<sub>i</sub>)<sup>2</sup></th>
    <th>(n<sub>i</sub> – Np<sub>i</sub>)<sup>2</sup>/Np<sub>i</sub></th>
  </tr>
  <tr>
    <td>1–4</td>
    <td>0–3</td>
    <td>80</td>
    <td>0,052</td>
    <td>15,626</td>
    <td>64,374</td>
    <td>4144,018</td>
    <td>265,201</td>
  </tr>
  <tr>
    <td>5</td>
    <td>4</td>
    <td>10</td>
    <td>0,108</td>
    <td>32,426</td>
    <td>–22,426</td>
    <td>502,924</td>
    <td>15,510</td>
  </tr>
  <tr>
    <td>6</td>
    <td>5</td>
    <td>9</td>
    <td>0,198</td>
    <td>59,267</td>
    <td>–50,267</td>
    <td>2526,741</td>
    <td>42,633</td>
  </tr>
  <tr>
    <td>7</td>
    <td>6</td>
    <td>40</td>
    <td>0,251</td>
    <td>75,226</td>
    <td>–35,226</td>
    <td>1240,849</td>
    <td>16,495</td>
  </tr>
  <tr>
    <td>8</td>
    <td>7</td>
    <td>51</td>
    <td>0,218</td>
    <td>65,473</td>
    <td>–14,473</td>
    <td>209,478</td>
    <td>3,199</td>
  </tr>
  <tr>
    <td>9</td>
    <td>8</td>
    <td>45</td>
    <td>0,125</td>
    <td>37,397</td>
    <td>7,603</td>
    <td>57,811</td>
    <td>1,546</td>
  </tr>
  <tr>
    <td>10–11</td>
    <td>9–10</td>
    <td>65</td>
    <td>0,049</td>
    <td>14,586</td>
    <td>50,414</td>
    <td>2541,602</td>
    <td>174,253</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>300</td>
    <td>1</td>
    <td>300</td>
    <td>0</td>
    <td></td>
    <td><b>518,84</b></td>
  </tr>
</table>

P-value = 7Е-110.

Сумма значений по столбцу Н дает наблюдаемое значение статистики

\[
\chi^2_{\text{набл}} = 514,94.
\]

Р-значение вычисляется по команде

P-value = ХИ2.РАСП.ПХ (518,84; 5) = 7Е-110.