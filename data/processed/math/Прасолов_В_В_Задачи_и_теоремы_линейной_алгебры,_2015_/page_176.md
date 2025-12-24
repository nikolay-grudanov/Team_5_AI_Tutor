---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.90
tokens: 6505
characters: 2196
timestamp: 2025-12-24T08:12:27.911948
finish_reason: stop
---

скалярным произведением \((\cdot, \cdot)_\mathbb{R}\) (точнее говоря, угол поворота от вектора \(x\) к вектору \(y\)). Тогда

\[
\cos \theta_K(x, y) \sin \angle(x, y) = \frac{(ix, y)_\mathbb{R}}{\|x\| \cdot \|y\|} = \cos \angle(ix, y).
\]

Прежде всего нужно проверить, что \(|\cos \theta_K(x, y)| \leq 1\), т. е.

\[
\cos^2 \angle(ix, y) \leq \sin^2 \angle(x, y).
\]

Согласно теореме 11.3.1 (в) \(\cos^2 \angle(x, y) + \cos^2 \angle(ix, y) \leq 1\). Это неравенство эквивалентно требуемому неравенству.

Ясно, что \(\cos \theta_K(x, y) = \cos \theta_K(y, x)\), поскольку \((ix, y)_\mathbb{R} = -(x, iy)_\mathbb{R}\) и \(\angle(x, y) = -\angle(y, x)\).

**Теорема 11.9.1.** а) Кэлеров угол \(\theta_K(x, y)\) зависит только от плоскости в \(V_\mathbb{R}\), натянутой на векторы \(x\) и \(y\), поэтому для любой плоскости определен кэлеров угол \(\theta_K\).

б) Плоскость голоморфная тогда и только тогда, когда кэлеров угол \(\theta_K\) равен 0 или \(\pi\).

в) Плоскость антиголоморфная тогда и только тогда, когда \(\theta_K = \pi/2\).

**Доказательство.** а) Достаточно проверить, что

\[
\cos \theta_K(x, y) = \cos \theta_K(x, y + tx)
\]

для любого \(t \in \mathbb{R}\). Ясно, что

\[
\cos^2 \theta_K(x, y) = \frac{\cos^2 \angle(ix, y)}{\sin^2 \angle(x, y)} = \frac{(ix, y)_\mathbb{R}^2}{\|x\|^2 \|y\|^2 - (x, y)_\mathbb{R}^2}.
\]

Учитывая, что \((ix, x)_\mathbb{R} = 0\), получаем

\[
(ix, y + tx)_\mathbb{R} = (ix, y)_\mathbb{R},
\]
\[
\|x\|^2 \|y + tx\|^2 - (x, y + tx)_\mathbb{R}^2 =
\]
\[
\|x\|^2 \|y\|^2 + 2t \|x\|^2 (y, x)_\mathbb{R} + t^2 \|x\|^4 - (x, y)_\mathbb{R}^2 - 2t \|x\|^2 (y, x)_\mathbb{R} - t^2 \|x\|^4 =
\]
\[
= \|x\|^2 \|y\|^2 - (x, y)_\mathbb{R}^2.
\]

Остаётся заметить, что числа \(\cos \theta_K(x, y)\) и \(\cos \theta_K(x, y + tx)\) имеют одинаковые знаки, поскольку \((ix, y + tx)_\mathbb{R} = (ix, y)_\mathbb{R}\) и направление поворота от вектора \(x\) к вектору \(y\) совпадает с направлением поворота от вектора \(x\) к вектору \(y + tx\).

б) В качестве базиса голоморфной плоскости можно выбрать векторы \(x\) и \(ix\). Ясно, что \(\sin \angle(x, ix) = 1\) и \(\frac{(ix, ix)_\mathbb{R}}{\|x\| \cdot \|ix\|} = 1\). Поэтому

\[
\cos \theta_K(x, ix) = 1.
\]