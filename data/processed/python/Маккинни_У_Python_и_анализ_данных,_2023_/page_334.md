---
source_image: page_334.png
page_number: 334
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 88.95
tokens: 9347
characters: 5118
timestamp: 2025-12-24T02:50:08.996090
finish_reason: stop
---

10.3. Метод apply: общий принцип разделения–применения–объединения

Если теперь сгруппировать по столбцу smoker и вызвать метод apply, передав ему эту функцию, то получим следующее:

In [84]: tips.groupby("smoker").apply(top)
Out[84]:

<table>
  <tr>
    <th>total_bill</th>
    <th>tip</th>
    <th>smoker</th>
    <th>day</th>
    <th>time</th>
    <th>size</th>
    <th>tip_pct</th>
  </tr>
  <tr>
    <th>smoker</th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td>No</td>
    <td>232</td>
    <td>11.61</td>
    <td>3.39</td>
    <td>No</td>
    <td>Sat</td>
    <td>Dinner</td>
    <td>2</td>
    <td>0.291990</td>
  </tr>
  <tr>
    <td></td>
    <td>149</td>
    <td>7.51</td>
    <td>2.00</td>
    <td>No</td>
    <td>Thur</td>
    <td>Lunch</td>
    <td>2</td>
    <td>0.266312</td>
  </tr>
  <tr>
    <td></td>
    <td>51</td>
    <td>10.29</td>
    <td>2.60</td>
    <td>No</td>
    <td>Sun</td>
    <td>Dinner</td>
    <td>2</td>
    <td>0.252672</td>
  </tr>
  <tr>
    <td></td>
    <td>185</td>
    <td>20.69</td>
    <td>5.00</td>
    <td>No</td>
    <td>Sun</td>
    <td>Dinner</td>
    <td>5</td>
    <td>0.241663</td>
  </tr>
  <tr>
    <td></td>
    <td>88</td>
    <td>24.71</td>
    <td>5.85</td>
    <td>No</td>
    <td>Thur</td>
    <td>Lunch</td>
    <td>2</td>
    <td>0.236746</td>
  </tr>
  <tr>
    <td>Yes</td>
    <td>172</td>
    <td>7.25</td>
    <td>5.15</td>
    <td>Yes</td>
    <td>Sun</td>
    <td>Dinner</td>
    <td>2</td>
    <td>0.710345</td>
  </tr>
  <tr>
    <td></td>
    <td>178</td>
    <td>9.60</td>
    <td>4.00</td>
    <td>Yes</td>
    <td>Sun</td>
    <td>Dinner</td>
    <td>2</td>
    <td>0.416667</td>
  </tr>
  <tr>
    <td></td>
    <td>67</td>
    <td>3.07</td>
    <td>1.00</td>
    <td>Yes</td>
    <td>Sat</td>
    <td>Dinner</td>
    <td>1</td>
    <td>0.325733</td>
  </tr>
  <tr>
    <td></td>
    <td>183</td>
    <td>23.17</td>
    <td>6.50</td>
    <td>Yes</td>
    <td>Sun</td>
    <td>Dinner</td>
    <td>4</td>
    <td>0.280535</td>
  </tr>
  <tr>
    <td></td>
    <td>109</td>
    <td>14.31</td>
    <td>4.00</td>
    <td>Yes</td>
    <td>Sat</td>
    <td>Dinner</td>
    <td>2</td>
    <td>0.279525</td>
  </tr>
</table>

Что здесь произошло? Сначала объект DataFrame tips разбит на группы по значению smoker. Затем для каждой группы вызывается функция top, после чего результаты склеиваются методом pandas.concat, а частям сопоставляются метки, совпадающие с именами групп. Поэтому результат имеет иерархический индекс, внутренний уровень которого содержит индексные значения из исходного объекта DataFrame.

Если передать методу apply функцию, которая принимает еще какие-то позиционные или именованные аргументы, то их можно передать вслед за самой функцией:

In [85]: tips.groupby(["smoker", "day"]).apply(top, n=1, column="total_bill")
Out[85]:

<table>
  <tr>
    <th>total_bill</th>
    <th>tip</th>
    <th>smoker</th>
    <th>day</th>
    <th>time</th>
    <th>size</th>
    <th>tip_pct</th>
  </tr>
  <tr>
    <th>smoker</th>
    <th>day</th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td>No</td>
    <td>Fri</td>
    <td>94</td>
    <td>22.75</td>
    <td>3.25</td>
    <td>No</td>
    <td>Fri</td>
    <td>Dinner</td>
    <td>2</td>
    <td>0.142857</td>
  </tr>
  <tr>
    <td></td>
    <td>Sat</td>
    <td>212</td>
    <td>48.33</td>
    <td>9.00</td>
    <td>No</td>
    <td>Sat</td>
    <td>Dinner</td>
    <td>4</td>
    <td>0.186220</td>
  </tr>
  <tr>
    <td></td>
    <td>Sun</td>
    <td>156</td>
    <td>48.17</td>
    <td>5.00</td>
    <td>No</td>
    <td>Sun</td>
    <td>Dinner</td>
    <td>6</td>
    <td>0.103799</td>
  </tr>
  <tr>
    <td></td>
    <td>Thur</td>
    <td>142</td>
    <td>41.19</td>
    <td>5.00</td>
    <td>No</td>
    <td>Thur</td>
    <td>Lunch</td>
    <td>5</td>
    <td>0.121389</td>
  </tr>
  <tr>
    <td>Yes</td>
    <td>Fri</td>
    <td>95</td>
    <td>40.17</td>
    <td>4.73</td>
    <td>Yes</td>
    <td>Fri</td>
    <td>Dinner</td>
    <td>4</td>
    <td>0.117750</td>
  </tr>
  <tr>
    <td></td>
    <td>Sat</td>
    <td>170</td>
    <td>50.81</td>
    <td>10.00</td>
    <td>Yes</td>
    <td>Sat</td>
    <td>Dinner</td>
    <td>3</td>
    <td>0.196812</td>
  </tr>
  <tr>
    <td></td>
    <td>Sun</td>
    <td>182</td>
    <td>45.35</td>
    <td>3.50</td>
    <td>Yes</td>
    <td>Sun</td>
    <td>Dinner</td>
    <td>3</td>
    <td>0.077178</td>
  </tr>
  <tr>
    <td></td>
    <td>Thur</td>
    <td>197</td>
    <td>43.11</td>
    <td>5.00</td>
    <td>Yes</td>
    <td>Thur</td>
    <td>Lunch</td>
    <td>4</td>
    <td>0.115982</td>
  </tr>
</table>

Это лишь простейшие приемы, а вообще возможности apply ограничены только вашей изобретательностью. Что именно делает переданная функция, решать вам, требуется лишь, чтобы она возвращала объект pandas или скалярное значение. Далее в этой главе будут в основном примеры, показывающие, как решать различные задачи с помощью groupby.

Вы, наверное, помните, что выше я вызывал метод describe от имени объекта GroupBy: