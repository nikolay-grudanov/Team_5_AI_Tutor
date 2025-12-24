---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.39
tokens: 11570
characters: 1822
timestamp: 2025-12-24T08:26:44.843175
finish_reason: stop
---

(f5) Если случайная величина \( \xi \) имеет абсолютно непрерывное распределение, то

\[
\mathbf{P}(a < \xi < b) = \mathbf{P}(a \leq \xi < b) = \mathbf{P}(a < \xi \leq b) = \mathbf{P}(a \leq \xi \leq b) = \int_a^b f_\xi(t) \, dt.
\]

Доказательство. Действительно, \( \mathbf{P}(a \leq \xi < b) = F_\xi(b) - F_\xi(a) = \int_{-\infty}^b f_\xi(t) \, dt - \int_{-\infty}^a f_\xi(t) \, dt \). Остальные равенства вытекают из следствия 5.

8.1 Примеры абсолютно непрерывных распределений

Равномерное. Это распределение нам уже знакомо. Говорят, что \( \xi \) имеет равномерное распределение на отрезке \([a, b]\), и пишут \( \xi \in \mathbf{U}_{a,b} \), если

\[
F_\xi(x) = \mathbf{P}(\xi < x) = \begin{cases}
0, & x < a; \\
\frac{x-a}{b-a}, & a \leq x \leq b \\
1, & x > b,
\end{cases}
\]
\[
f_\xi(x) = \begin{cases}
0, & x < a; \\
\frac{1}{b-a}, & a \leq x \leq b \\
0, & x > b.
\end{cases}
\]

Заметьте, что в точках \( a \) и \( b \) функция распределения недифференцируема, и плотность можно задать как угодно.

Показательное. Говорят, что \( \xi \) имеет показательное распределение с параметром \( \alpha, \alpha > 0 \) и пишут \( \xi \in \mathbf{E}_\alpha \), если

\[
F_\xi(x) = \mathbf{P}(\xi < x) = \begin{cases}
0, & x < 0; \\
1 - e^{-\alpha x}, & x \geq 0,
\end{cases}
\]
\[
f_\xi(x) = \begin{cases}
0, & x < 0; \\
\alpha e^{-\alpha x}, & x \geq 0.
\end{cases}
\]

Показательное распределение является единственным абсолютно непрерывным распределением, для которого выполнено свойство «нестарения» (и в этом смысле оно является непрерывным аналогом дискретного геометрического распределения).

Теорема 21. Свойство «нестарения». Пусть \( \xi \in \mathbf{E}_\alpha \). Тогда для любых \( x, y > 0 \)

\[
\mathbf{P}(\xi > x + y \mid \xi > x) = \mathbf{P}(\xi > y).
\]

Упражнение 10. Доказать «свойство нестарения».