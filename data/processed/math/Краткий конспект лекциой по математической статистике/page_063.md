---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.50
tokens: 12455
characters: 3065
timestamp: 2025-12-24T07:05:10.086933
finish_reason: stop
---

Упражнение. Убедиться, что решением системы уравнений

\[
\frac{\partial}{\partial \theta_1} \left|_{\theta = \hat{\theta}} \sum_{i=1}^n \varepsilon_i^2 \right. = 0; \quad \frac{\partial}{\partial \theta_2} \left|_{\theta = \hat{\theta}} \sum_{i=1}^n \varepsilon_i^2 \right. = 0
\]

является пара

\[
\hat{\theta}_2 = \frac{\frac{1}{n} \sum t_i X_i - \overline{X} \cdot \overline{t}}{\frac{1}{n} \sum (t_i - \overline{t})^2}; \qquad \hat{\theta}_1 = \overline{X} - \overline{t} \hat{\theta}_2.
\]

Линия \( \mathbf{E}X = \hat{\theta}_1 + t \hat{\theta}_2 \) называется линией регрессии \( X \) на \( t \).

Определение 32. Величина

\[
\rho^* = \frac{\frac{1}{n} \sum t_i X_i - \overline{X} \cdot \overline{t}}{\sqrt{\frac{1}{n} \sum (t_i - \overline{t})^2 \frac{1}{n} \sum (X_i - \overline{X})^2}}
\]

называется «выборочным коэффициентом корреляции» и характеризует степень линейной зависимости между \( X \) и \( t \).

Пример 33. Полиномиальная регрессия Модель регрессии имеет вид \( \mathbf{E}X = \theta_0 + \theta_1 t + \theta_2 t^2 + \ldots + \theta_{k-1} t^{k-1} \). В следующем параграфе будет показано, как эта модель сводится к общей модели линейной регрессии.

Пример 34. Термин «регрессия» появился впервые в работе Francis Galton, “Regression towards mediocrity in hereditary stature" (Journal of the Anthropological Institute V. 15, p. 246–265, 1886).
Гальтон (в частности) исследовал рост детей высоких родителей, и установил, что он «регрессирует» в среднем, то есть в среднем дети высоких родителей не так высоки, как их родители. Для линейной модели регрессии \( X = \theta_1 t + \theta_2 u + c \) Гальтон нашел оценки параметров:

Рост сына = 0,27 Роста отца + 0,2 Роста матери + const,

а рост дочери еще в 1,08 раз меньше.

9.3 Общая модель линейной регрессии

Замечание 30. В отличие от обозначений Лекции 6, отныне и навеки все вектора есть вектора-столбцы. Благодарю А. Иванова за соответствующее замечание и надеюсь, что не только он заметил несоответствие обозначений в лемме Фишера курсу алгебры.

Введем два вектора: \( \vec{Z} = (Z_1, \ldots, Z_k) \) — вектор факторов регрессии и \( \vec{\beta} = (\beta_1, \ldots, \beta_k) \) — вектор неизвестных параметров регрессии. Рассматривается модель регрессии, которая в курсе «Эконометрия» называется «простой (линейной) регрессией»:

\[
\mathbf{E}X = \beta_1 Z_1 + \ldots + \beta_k Z_k.
\]

Пусть в \( i \)-м эксперименте факторы регрессии принимают (известные) значения \( \overrightarrow{Z^{(i)}} = (Z_1^{(i)}, \ldots, Z_k^{(i)}) \), \( i = 1, \ldots, n \).
Пусть \( \vec{\varepsilon} = (\varepsilon_1, \ldots, \varepsilon_n) \), где \( \varepsilon_i \) — случайная ошибка в \( i \)-м эксперименте (неизвестна).
После \( n \) экспериментов (\( n \geq k \)) в данной модели получена выборка \( \vec{X} = (X_1, \ldots, X_n) \), где

\[
\begin{cases}
X_1 = \beta_1 Z_1^{(1)} + \ldots + \beta_k Z_k^{(1)} + \varepsilon_1 \\
X_2 = \beta_1 Z_1^{(2)} + \ldots + \beta_k Z_k^{(2)} + \varepsilon_2 \\
\ldots \\
X_n = \beta_1 Z_1^{(n)} + \ldots + \beta_k Z_k^{(n)} + \varepsilon_n,
\end{cases}
\]