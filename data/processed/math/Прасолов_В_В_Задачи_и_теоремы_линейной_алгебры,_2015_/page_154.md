---
source_image: page_154.png
page_number: 154
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.21
tokens: 6428
characters: 1949
timestamp: 2025-12-24T08:11:45.392552
finish_reason: stop
---

Следствие. Для ортогональных векторов \( e_1, \ldots, e_n \) в \( \mathbb{R}^n \) \( m \)-мерное подпространство \( W \), образующее с ними данные углы \( \alpha_1, \ldots, \alpha_n \), существует тогда и только тогда, когда

\[
\frac{\cos^2 \alpha_1 + \ldots + \cos^2 \alpha_n}{\cos^2 \alpha_i} \geq m
\]

при \( i = 1, \ldots, n \).

Доказательство. Если \( \alpha_i \) — угол между вектором \( e_i \) и подпространством \( W \), то \( d_i = d / \cos \alpha \). \( \square \)

9.8. Определители, составленные из скалярных произведений

Теорема 9.8.1. Пусть \( U \) и \( W \) — \( m \)-мерные подпространства в пространстве \( V \), \( e_1, \ldots, e_m \) и \( \varepsilon_1, \ldots, \varepsilon_m \) — их ортонормированные базисы, \( x_1, \ldots, x_m \) и \( y_1, \ldots, y_m \) — системы векторов в \( U \) и \( W \). Тогда

\[
|(x_i, y_j)|_1^m = |(x_i, e_j)|_1^m |(y_i, \varepsilon_j)|_1^m |(e_i, \varepsilon_j)|_1^m.
\]

Доказательство [Ко]. Так как \( x_i = \sum_{k=1}^m (x_i, \varepsilon_k) \varepsilon_k + x'_i \), где \( x'_i \perp W \) и \( y_j = \sum_{k=1}^m (y_j, \varepsilon_k) \varepsilon_k \), то

\[
|(x_i, y_j)|_1^m = \left| \sum_{k=1}^m (x_i, \varepsilon_k)(\varepsilon_k, y_j) \right|_1^m = |(x_i, \varepsilon_k)|_1^m |(\varepsilon_k, y_j)|_1^m.
\]

А так как \( \varepsilon_k = \sum_{j=1}^m (\varepsilon_k, e_j) e_j + \varepsilon'_k \), где \( \varepsilon_k \perp U \), то

\[
|(x_i, \varepsilon_k)|_1^m = \left| \sum_{k=1}^m (\varepsilon_k, e_j)(e_j, x_i) \right|_1^m = |(x_i, \varepsilon_j)|_1^m |(e_j, \varepsilon_k)|_1^m.
\]

Следствие 1. \( (|(x_i, y_j)|_1^m)^2 = |(x_i, x_j)|_1^m |(y_i, y_j)|_1^m (|(e_i, \varepsilon_j)|_1^m)^2 \).

Доказательство. Из равенства \( x_i = \sum_{k=1}^m (x_i, e_k) e_k \) следует, что

\[
|(x_i, x_j)|_1^m = \left| \sum_{k=1}^m (x_i, e_k)(e_k, x_j) \right|_1^m = |(x_i, e_k)|_1^m |(e_k, x_j)|_1^m.
\]

Аналогично

\[
|(y_i, y_j)|_1^m = |(y_i, \varepsilon_k)|_1^m |(\varepsilon_k, y_j)|_1^m.
\]