---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.79
tokens: 11725
characters: 2431
timestamp: 2025-12-24T08:28:35.431683
finish_reason: stop
---

Сходимость по вероятности обладает обычными для сходимостей свойствами. Например, такими.

**Свойство 16.** Если \( \xi_n \xrightarrow{\mathrm{p}} \xi \) и \( \eta_n \xrightarrow{\mathrm{p}} \eta \), то

1. \( \xi_n + \eta_n \xrightarrow{\mathrm{p}} \xi + \eta; \)
2. \( \xi_n \cdot \eta_n \xrightarrow{\mathrm{p}} \xi \cdot \eta. \)

Доказательство при первом прочтении можно пропустить.

1. В доказательстве мы будем пользоваться естественным свойством вероятности: если из события \( A \) следует событие \( B \) (всегда, когда выполнено \( A \), выполнено и \( B \)), то вероятность \( A \) не превосходит вероятности \( B \):

если \( A \subseteq B \), то \( \mathbf{P}(A) \leqslant \mathbf{P}(B). \)

Здесь я категорически требую остановиться и ответить на следующие «глупые вопросы»:

— Верно ли, что модуль суммы не превосходит суммы модулей?
— Верно ли, что если \( a > b \), и \( c > a \), то \( c > b \)?
— Верно ли, что если \( a + b > 2 \), то хоть одно из чисел \( a, b \) больше единицы?
— Верно ли, что вероятность объединения двух событий не превосходит суммы их вероятностей?
— Верно ли, что вероятность пересечения двух событий не превосходит вероятности любого из них?

Если на все вопросы вы ответили «да», можно двигаться дальше. Если не на все — ваш контрпример ошибочен. Если вы вообще не поняли, о чем это, лучше вернуться сюда ...

Пусть \( \varepsilon > 0 \). Требуется доказать, что \( \mathbf{P}(|\xi_n + \eta_n - \xi - \eta| > \varepsilon) \to 0 \) при \( n \to \infty \). Но

а) \( |\xi_n + \eta_n - \xi - \eta| \leqslant |\xi_n - \xi| + |\eta_n - \eta| \), поэтому

б) если \( |\xi_n + \eta_n - \xi - \eta| > \varepsilon \), то и \( |\xi_n - \xi| + |\eta_n - \eta| > \varepsilon \), и вероятность первого события не больше вероятности второго. Далее,

в) если \( |\xi_n - \xi| + |\eta_n - \eta| > \varepsilon \), то хотя бы одно из слагаемых больше, чем \( \varepsilon/2 \).

Получаем следующую цепочку неравенств:

\[
\begin{align*}
\mathbf{P}(|\xi_n + \eta_n - \xi - \eta| > \varepsilon) &\leqslant \mathbf{P}(|\xi_n - \xi| + |\eta_n - \eta| > \varepsilon) \leqslant \mathbf{P}(|\xi_n - \xi| > \varepsilon/2 \text{ или } |\eta_n - \eta| > \varepsilon/2) \\
&\leqslant \mathbf{P}(|\xi_n - \xi| > \varepsilon/2) + \mathbf{P}(|\eta_n - \eta| > \varepsilon/2) \to 0
\end{align*}
\]

при \( n \to \infty \), так как \( \xi_n \xrightarrow{\mathrm{p}} \xi \) и \( \eta_n \xrightarrow{\mathrm{p}} \eta \).