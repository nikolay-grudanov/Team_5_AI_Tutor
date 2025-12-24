---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.77
tokens: 12221
characters: 2184
timestamp: 2025-12-24T07:37:36.051010
finish_reason: stop
---

Таблица 2. Основные абсолютно непрерывные распределения

<table>
  <tr>
    <th>Распределение, обозначение, параметры</th>
    <th>Плотность распределения</th>
    <th>E</th>
    <th>D</th>
    <th>Асимметрия</th>
    <th>Эксцесс</th>
  </tr>
  <tr>
    <td>Равномерное на отрезке [a, b], U<sub>a, b</sub>, a < b</td>
    <td>\[
      \begin{cases}
        \frac{1}{b-a}, & x \in [a, b], \\
        0, & x \notin [a, b]
      \end{cases}
    \]</td>
    <td>\(\frac{a+b}{2}\)</td>
    <td>\(\frac{(b-a)^2}{12}\)</td>
    <td>0</td>
    <td>-1,2</td>
  </tr>
  <tr>
    <td>Показательное (экспоненциальное) E = Γ ,1, > 0</td>
    <td>\[
      \begin{cases}
        e^{-x}, & x > 0, \\
        0, & x \leq 0
      \end{cases}
    \]</td>
    <td>\(\frac{1}{2}\)</td>
    <td>\(\frac{1}{2}\)</td>
    <td>2</td>
    <td>6</td>
  </tr>
  <tr>
    <td>Нормальное (гауссовское) N<sub>a, 2,</sub> \(a \in \mathbb{R},\ > 0\)</td>
    <td>\[
      \frac{1}{\sqrt{2\pi}} e^{-(x-a)^2/2},
      -\infty < x < \infty
    \]</td>
    <td>a</td>
    <td>2</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Коши C<sub>a,</sub>, \(a \in \mathbb{R},\ > 0\)</td>
    <td>\[
      \frac{1}{\pi} \frac{1}{2 + (x-a)^2},
      -\infty < x < \infty
    \]</td>
    <td>—</td>
    <td>—</td>
    <td>—</td>
    <td>—</td>
  </tr>
  <tr>
    <td>Гамма Γ , , > 0, > 0</td>
    <td>\[
      \begin{cases}
        \frac{\Gamma(\ )}{\Gamma(\ )} x^{-1} e^{-x}, & x > 0, \\
        0, & x \leq 0
      \end{cases}
    \]</td>
    <td>—</td>
    <td>\(\frac{2}{\sqrt{2}}\)</td>
    <td>\(\frac{2}{\sqrt{2}}\)</td>
    <td>6</td>
  </tr>
  <tr>
    <td>Лапласа L ,∞, > 0, \(x \in \mathbb{R}\)</td>
    <td>\[
      \frac{1}{2} e^{-|x-\infty|},
      -\infty < x < \infty
    \]</td>
    <td>\(\infty\)</td>
    <td>\(\frac{2}{2}\)</td>
    <td>0</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Парето, > 0</td>
    <td>\[
      \begin{cases}
        \frac{1}{x+1}, & x \geq 1, \\
        0, & x < 1
      \end{cases}
    \]</td>
    <td>\(\frac{-1}{( > 1)}\)</td>
    <td>\(\frac{(-1)^2(-2), \wedge 2}{-2 2(+1), -3}\)</td>
    <td>\(\wedge 3\)</td>
    <td>\(\frac{6(3+2-6-2)}{(-3)(-4)}, > 4\)</td>
  </tr>
</table>