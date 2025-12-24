---
source_image: page_533.png
page_number: 533
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 81.91
tokens: 7839
characters: 4401
timestamp: 2025-12-24T08:06:21.143307
finish_reason: stop
---

Команды в Minitab обычно запускаются при помощи меню; они записываются в рабочем окне вместе с результатами, которые могут быть выражены в виде текста; фрагмент рабочего окна с бинарным логистическим регрессионным анализом показан на рис. В.2. Каждый графический результат записывается в отдельном окне (что может привести к значительному разрастанию числа открытых окон во время анализа!). Все результаты вместе с набором данным, использованным при анализе, можно сохранить в виде проекта Minitab, а наборы данных и диаграммы можно сохранить в виде отдельных файлов разных форматов.

MTB > B logistic 'CHD' = CHD CAT AGE CHL SMK ECG;
T

Results for: evans
Binary Logistic Regression: CHD versus CAT. AGE. CHL. SMK. ECG
Link Function: Logit

Response Information
Variable Value Count
CHD 1 71 (Event)
0 538
Total 609

Logistic Regression Table

<table>
  <tr>
    <th>Predictor</th>
    <th>Coef</th>
    <th>SE Coef</th>
    <th>Z</th>
    <th>P</th>
    <th>Odds Ratio</th>
    <th>95% CI Lower</th>
    <th>95% CI Upper</th>
  </tr>
  <tr>
    <td>Constant</td>
    <td>-6.76472</td>
    <td>1.13218</td>
    <td>-5.97</td>
    <td>0.000</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CAT</td>
    <td>0.776079</td>
    <td>0.333091</td>
    <td>2.33</td>
    <td>0.020</td>
    <td>2.17</td>
    <td>1.13</td>
    <td>4.17</td>
  </tr>
  <tr>
    <td>AGE</td>
    <td>0.0325374</td>
    <td>0.0151541</td>
    <td>2.15</td>
    <td>0.032</td>
    <td>1.03</td>
    <td>1.00</td>
    <td>1.06</td>
  </tr>
  <tr>
    <td>CHL</td>
    <td>0.0093670</td>
    <td>0.0032332</td>
    <td>2.90</td>
    <td>0.004</td>
    <td>1.01</td>
    <td>1.00</td>
    <td>1.02</td>
  </tr>
  <tr>
    <td>SMK</td>
    <td>0.828039</td>
    <td>0.304211</td>
    <td>2.72</td>
    <td>0.006</td>
    <td>2.29</td>
    <td>1.26</td>
    <td>4.15</td>
  </tr>
  <tr>
    <td>ECG</td>
    <td>0.416540</td>
    <td>0.292459</td>
    <td>1.42</td>
    <td>0.154</td>
    <td>1.52</td>
    <td>0.85</td>
    <td>2.69</td>
  </tr>
</table>

Log-Likelihood = -201.337
Test that all slopes are zero: G = 35.884, DF = 5, P-Value = 0.000

Goodness-of-Fit Tests
<table>
  <tr>
    <th>Method</th>
    <th>Chi-Square</th>
    <th>DF</th>
    <th>P</th>
  </tr>
  <tr>
    <td>Pearson</td>
    <td>588.700</td>
    <td>586</td>
    <td>0.461</td>
  </tr>
  <tr>
    <td>Deviance</td>
    <td>397.129</td>
    <td>586</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>Hosmer-Lemeshow</td>
    <td>16.062</td>
    <td>8</td>
    <td>0.041</td>
  </tr>
</table>

Table of Observed and Expected Frequencies:
(See Hosmer-Lemeshow Test for the Pearson Chi-Square Statistic)

<table>
  <tr>
    <th rowspan="2">Value</th>
    <th colspan="10">Group</th>
    <th rowspan="2">Total</th>
  </tr>
  <tr>
    <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td><td>2</td><td>5</td><td>9</td><td>6</td><td>8</td><td>8</td><td>4</td><td>6</td><td>23</td><td>71</td>
  </tr>
  <tr>
    <td>Exp</td>
    <td>1.8</td><td>2.8</td><td>3.7</td><td>4.4</td><td>5.2</td><td>6.3</td><td>7.3</td><td>8.8</td><td>11.5</td><td>19.2</td>
  </tr>
  <tr>
    <td>0</td>
    <td>60</td><td>59</td><td>56</td><td>52</td><td>55</td><td>53</td><td>53</td><td>57</td><td>55</td><td>38</td><td>538</td>
  </tr>
  <tr>
    <td>Exp</td>
    <td>58.2</td><td>58.2</td><td>57.3</td><td>56.6</td><td>55.8</td><td>54.7</td><td>53.7</td><td>52.2</td><td>49.5</td><td>41.8</td>
  </tr>
  <tr>
    <td>Total</td>
    <td>60</td><td>61</td><td>61</td><td>61</td><td>61</td><td>61</td><td>61</td><td>61</td><td>61</td><td>61</td><td>609</td>
  </tr>
</table>

Measures of Association:
(Between the Response Variable and Predicted Probabilities)

<table>
  <tr>
    <th>Pairs</th>
    <th>Number</th>
    <th>Percent</th>
    <th>Summary Measures</th>
  </tr>
  <tr>
    <td>Concordant</td>
    <td>25869</td>
    <td>67.7</td>
    <td>Somers' D</td>
    <td>0.36</td>
  </tr>
  <tr>
    <td>Discordant</td>
    <td>11933</td>
    <td>31.2</td>
    <td>Goodman-Kruskal Gamma</td>
    <td>0.37</td>
  </tr>
  <tr>
    <td>Ties</td>
    <td>396</td>
    <td>1.0</td>
    <td>Kendall's Tau-a</td>
    <td>0.08</td>
  </tr>
  <tr>
    <td>Total</td>
    <td>38198</td>
    <td>100.0</td>
    <td></td>
    <td></td>
  </tr>
</table>

Рис. В.2. Рабочее окно Minitab