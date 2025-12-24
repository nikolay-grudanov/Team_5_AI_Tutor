---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.69
tokens: 11880
characters: 1380
timestamp: 2025-12-24T07:37:31.906899
finish_reason: stop
---

ПРИЛОЖЕНИЕ

Таблица 1. Основные дискретные распределения

<table>
  <tr>
    <th>Распределение, обозначение, параметры</th>
    <th>Возможные значения k</th>
    <th>P( = k)</th>
    <th>E</th>
    <th>D</th>
  </tr>
  <tr>
    <td>Вырожденное I<sub>c</sub>, c ∈ ℝ</td>
    <td>c</td>
    <td>P( = c) = 1</td>
    <td>c</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Бернулли B<sub>p</sub> p ∈ (0, 1)</td>
    <td>k = 0, 1</td>
    <td>P( = 0) = 1 - p,<br>P( = 1) = p</td>
    <td>p</td>
    <td>p(1 - p)</td>
  </tr>
  <tr>
    <td>Биномиальное B<sub>n, p</sub> p ∈ (0, 1)<br>n = 1, 2, ...</td>
    <td>k = 0, ..., n</td>
    <td>C<sub>n</sub><sup>k</sup> p<sup>k</sup>(1 - p)<sup>n-k</sup></td>
    <td>np</td>
    <td>np(1 - p)</td>
  </tr>
  <tr>
    <td>Пуассона П > 0</td>
    <td>k = 0, 1, 2, ...</td>
    <td>\( \frac{k}{k!} e^{-\Pi} \)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Геометрическое G<sub>p</sub> p ∈ (0, 1)</td>
    <td>k = 1, 2, ...</td>
    <td>p(1 - p)<sup>k-1</sup></td>
    <td>\( \frac{1}{p} \)</td>
    <td>\( \frac{1 - p}{p^2} \)</td>
  </tr>
  <tr>
    <td>Гипергеометрическое n, K, N ∈ ℕ<br>0 ≤ n, K ≤ N</td>
    <td>целые от max(0, n+K-N) до min(n, K)</td>
    <td>\( \frac{C_K^k C_{N-K}^{n-k}}{C_N^n} \)</td>
    <td>\( n \frac{K}{N} \)</td>
    <td>\( n \frac{K}{N} \left( 1 - \frac{K}{N} \right) \frac{N-n}{N-1} \)</td>
  </tr>
</table>