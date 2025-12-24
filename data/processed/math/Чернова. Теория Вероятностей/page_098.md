---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 73.69
tokens: 12267
characters: 3657
timestamp: 2025-12-24T08:29:24.505027
finish_reason: stop
---

поскольку в точках \( c \pm \varepsilon \) функция \( F_c \) непрерывна, и, следовательно, имеет место сходимость последовательности \( F_{\xi_n}(c \pm \varepsilon) \) к \( F_c(c \pm \varepsilon) \).

Осталось заметить, что \( \mathbf{P}(|\xi_n - c| \leq \varepsilon) \) не бывает больше 1, так что по лемме о двух милиционерах \( \mathbf{P}(|\xi_n - c| \leq \varepsilon) \to 1 \).

Следующее свойство приводит пример операций, которые можно применять к слабо сходящимся последовательностям — скажем, домножать их на последовательности, сходящиеся по вероятности к постоянным величинам.

Желание написать «если \( \xi_n \Rightarrow \xi \) и \( \eta_n \Rightarrow \eta \), то \( \xi_n + \eta_n \Rightarrow \xi + \eta \)» сразу проходит, стоит перевести это «свойство» на язык функций распределения и задуматься — что такое «функция распределения суммы \( \xi + \eta \)», когда вместо них можно брать любые другие \( \tilde{\xi} \) и \( \tilde{\eta} \) с теми же распределениями, как угодно зависимые. Иное дело — когда одно из предельных распределений вырождено. В этом случае функция распределения суммы или произведения определена однозначно.

**Свойство 20.**
1. Если \( \xi_n \xrightarrow{p} c = const \) и \( \eta_n \Rightarrow \eta \), то \( \xi_n \cdot \eta_n \Rightarrow c \eta \).
2. Если \( \xi_n \xrightarrow{p} c = const \) и \( \eta_n \Rightarrow \eta \), то \( \xi_n + \eta_n \Rightarrow c + \eta \).

**Доказательство.** Заметим прежде всего, что если \( \eta_n \Rightarrow \eta \), то \( c \eta_n \Rightarrow c \eta, c + \eta_n \Rightarrow c + \eta \) (доказать!). Поэтому (и в силу соответствующих свойств сходимости по вероятности) достаточно доказать первое утверждение свойства **20** при \( c = 1 \), а второе утверждение — при \( c = 0 \).

Докажем второе утверждение, оставив первое читателю. Пусть \( \xi_n \xrightarrow{p} 0 \) и \( \eta_n \Rightarrow \eta \). Докажем, что \( \xi_n + \eta_n \Rightarrow \eta \). Пусть \( x_0 \) — точка непрерывности функции распределения \( F_\eta(x) \). Требуется доказать, что тогда имеет место сходимость \( F_{\xi_n + \eta_n}(x_0) \to F_\eta(x_0) \). Зафиксируем достаточно маленькое \( \varepsilon > 0 \) такое, что \( F_\eta(x) \) непрерывна в точках \( x_0 \pm \varepsilon \).

\[
F_{\xi_n + \eta_n}(x_0) = \mathbf{P}(\xi_n + \eta_n < x_0) = \mathbf{P}(\xi_n + \eta_n < x_0, |\xi_n| > \varepsilon) + \mathbf{P}(\xi_n + \eta_n < x_0, |\xi_n| \leq \varepsilon) = P_1 + P_2.
\]

Оценим \( P_1 + P_2 \) сверху и снизу. Для \( P_1 \) имеем: \( 0 \leq P_1 = \mathbf{P}(\xi_n + \eta_n < x_0, |\xi_n| > \varepsilon) \leq \mathbf{P}(|\xi_n| > \varepsilon) \), и последняя вероятность может быть выбором \( n \) сделана сколь угодно малой.

Для \( P_2 \), с одной стороны,

\[
P_2 = \mathbf{P}(\xi_n + \eta_n < x_0, -\varepsilon \leq \xi_n \leq \varepsilon) \leq \mathbf{P}(-\varepsilon + \eta_n < x_0) = \mathbf{P}(\eta_n < x_0 + \varepsilon).
\]

Здесь первое неравенство следует из очевидного соображения:

*если* \( -\varepsilon \leq \xi_n \) *и* \( \xi_n + \eta_n < x_0 \), *то, тем более*, \( -\varepsilon + \eta_n < x_0 \).

С другой стороны,

\[
P_2 = \mathbf{P}(\xi_n + \eta_n < x_0, -\varepsilon \leq \xi_n \leq \varepsilon) \geq \mathbf{P}(\varepsilon + \eta_n < x_0, -\varepsilon \leq \xi_n \leq \varepsilon) \geq \mathbf{P}(\varepsilon + \eta_n < x_0) - \mathbf{P}(|\xi_n| > \varepsilon) = \mathbf{P}(\eta_n < x_0 - \varepsilon) - \mathbf{P}(|\xi_n| > \varepsilon).
\]

Здесь первое неравенство объясняется включением \( \{\varepsilon + \eta_n < x_0\} \cap \{-\varepsilon \leq \xi_n \leq \varepsilon\} \subset \{\xi_n + \eta_n < x_0\} \cap \{-\varepsilon \leq \xi_n \leq \varepsilon\} \) —