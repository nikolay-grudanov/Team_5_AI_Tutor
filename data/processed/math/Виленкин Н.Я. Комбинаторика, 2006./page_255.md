---
source_image: page_255.png
page_number: 255
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.88
tokens: 6604
characters: 1838
timestamp: 2025-12-24T07:47:30.494674
finish_reason: stop
---

254 Глава VIII. РЯДЫ И ПРОИЗВОДЯЩИЕ ФУНКЦИИ

\[
2 \sum_s C_{p+1}^{2s} C_p^{2m-2s+1} = C_{2p+1}^{2m+1} - (-1)^m C_p^m,
\]

\[
2 \sum_s C_{p+1}^{2s+1} C_p^{2m-2s} = C_{2p+1}^{2m+1} + (-1)^m C_p^m,
\]

\[
2 \sum_s C_{p+1}^{2s+1} C_p^{2m-2s+1} = C_{2p+1}^{2m+2} + (-1)^m C_p^{m+1},
\]

\[
2 \sum_s C_{p+2s-1}^{p-1} C_{p+2m-2s}^p = C_{2p+2m}^{2p} + C_{p+m}^p,
\]

\[
2 \sum_s C_{p+2s-1}^{p-1} C_{p+2m-2s+1}^p = C_{2p+2m+1}^{2p} + C_{p+m}^p,
\]

\[
2 \sum_s C_{p+2s}^{p-1} C_{p+2m-2s}^p = C_{2p+2m+1}^{2p} - C_{p+m}^p,
\]

\[
2 \sum_s C_{p+2s}^{p-1} C_{p+2m-2s+1}^p = C_{2p+2m+2}^{2p} - C_{p+m+1}^p
\]

(каждая сумма распространена на целые неотрицательные значения s, для которых определена левая часть равенства).

29. Рассмотрев бином \(\left(-\frac{1}{2} + i \frac{\sqrt{3}}{2}\right)^n\), докажите, что:

а) \(1 - 3C_n^2 + 9C_n^4 - 27C_n^6 + ... = (-1)^n 2^n \cos \frac{2n\pi}{3}\);

б) \(C_n^1 - 3C_n^3 + 9C_n^5 - 27C_n^7 + ... = \frac{(-1)^{n+1}}{\sqrt{3}} 2^{n+1} \sin \frac{2n\pi}{3}\).

30. Пусть \(\varepsilon = \cos \frac{2\pi}{3} + i \sin \frac{2\pi}{3}\). Рассмотрев бином \((1 + x)^n\) последовательно при \(x = 1,\ x = \varepsilon,\ x = \varepsilon^2\) и \(x = i\), докажите, что:

а) \(C_n^0 + C_n^3 + C_n^6 + ... = \frac{1}{3} \left(2^n + 2 \cos \frac{n\pi}{3}\right)\);

б) \(C_n^1 + C_n^4 + C_n^7 + ... = \frac{1}{3} \left(2^n + 2 \cos \frac{(n-2)\pi}{3}\right)\);

в) \(C_n^2 + C_n^5 + C_n^8 + ... = \frac{1}{3} \left(2^n + 2 \cos \frac{(n+2)\pi}{3}\right)\);

г) \(C_n^0 + C_n^4 + C_n^8 + ... = \frac{1}{2} \left(2^{n-1} + 2^{\frac{n}{2}} \cos \frac{n\pi}{4}\right)\).

31. а) Из тождества \((1 + x)^p (1 + x)^{-k-1} = (1 + x)^{p-k-1}\) выведите, что \(\sum_s (-1)^s C_{k+s}^s C_p^{n-s} = C_{p-k-1}^n\) (здесь и далее сумма распространена на целые неотрицательные значения s, для которых определена левая часть равенства).