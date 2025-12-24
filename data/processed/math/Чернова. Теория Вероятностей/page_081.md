---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 62.24
tokens: 11828
characters: 2305
timestamp: 2025-12-24T08:28:28.740517
finish_reason: stop
---

Упражнение 23. Обяснить, будет ли распределение \( \tilde{\xi} \)
а) нормальным, если \( \xi \) распределена по нормальному закону; б) равномерным, если \( \xi \) имеет равномерное распределение;
в) биномиальным, если \( \xi \) имеет биномиальное распределение; г) показательным, если \( \xi \) имеет показательное распределение;
(и т.д.)

Свойство 15. Стандартизованная с. в. \( \tilde{\xi} \) имеет нулевое математическое ожидание и единичную дисперсию.

Доказательство. Воспользуемся свойствами математического ожидания и дисперсии:

\[
E \tilde{\xi} = E \left( \frac{\xi - E \xi}{\sqrt{D \xi}} \right) = \frac{1}{\sqrt{D \xi}} E (\xi - E \xi) = \frac{1}{\sqrt{D \xi}} (E \xi - E \xi) = 0;
\]

\[
D \tilde{\xi} = D \left( \frac{\xi - E \xi}{\sqrt{D \xi}} \right) = \frac{1}{D \xi} D (\xi - E \xi) = \frac{1}{D \xi} D \xi = 1.
\]

Не забудьте у каждого знака равенства написать, в силу какого свойства, утверждения или определения это равенство верно!

Возвращаясь к доказательству 2, заметим, что

\[
\rho(\xi, \eta) = \frac{E \left( (\xi - E \xi)(\eta - E \eta) \right)}{\sqrt{D \xi} \sqrt{D \eta}} = E \left( \frac{(\xi - E \xi)(\eta - E \eta)}{\sqrt{D \xi} \sqrt{D \eta}} \right) = E \left( \tilde{\xi} \tilde{\eta} \right),
\]

где \( \tilde{\xi} = \frac{\xi - E \xi}{\sqrt{D \xi}} \) и \( \tilde{\eta} = \frac{\eta - E \eta}{\sqrt{D \eta}} \) — стандартизованные версии с. в. \( \xi \) и \( \eta \).

Теперь воспользуемся неравенством \( 0 \leq (a - b)^2 = a^2 - 2ab + b^2 \), или \( ab \leq \frac{1}{2}(a^2 + b^2) \). Подставим \( \tilde{\xi} \) вместо \( a \), \( \tilde{\eta} \) вместо \( b \) и возьмем математические ожидания от обеих частей неравенства:

\[
\rho(\xi, \eta) = E \left( \tilde{\xi} \tilde{\eta} \right) \leq \frac{1}{2} E \left( \tilde{\xi}^2 + \tilde{\eta}^2 \right) = \frac{1}{2} \left( D \tilde{\xi} + (E \tilde{\xi})^2 + D \tilde{\eta} + (E \tilde{\eta})^2 \right) = \frac{1}{2} \cdot 2 = 1.
\] (19)

Пользуясь точно так же неравенством \( 0 \leq (a + b)^2 = a^2 + 2ab + b^2 \), или \( ab \geq -\frac{1}{2}(a^2 + b^2) \), получим

\[
\rho(\xi, \eta) = E \left( \tilde{\xi} \tilde{\eta} \right) \geq -\frac{1}{2} E \left( \tilde{\xi}^2 + \tilde{\eta}^2 \right) = -\frac{1}{2} \cdot 2 = -1.
\] (20)

Таким образом, \( |\rho(\xi, \eta)| \leq 1 \), что и требовалось доказать.