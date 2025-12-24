---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.31
tokens: 6645
characters: 1743
timestamp: 2025-12-24T07:47:35.322966
finish_reason: stop
---

б) Из тождества \((1 - x)^{-m-1}(1 - x)^{-q-1} = (1 - x)^{-m-q-2}\) выведите, что
\[
\sum_s C_{p-s}^m C_{q-s}^q = C_{p+q+1}^{p-m}.
\]
в) Из тождества \((1 + x)^n = (1 - x^2)^n(1 - x)^{-n}\) выведите, что
\[
\sum_s (-1)^s C_{n+k-2s}^n C_{n+1}^s = \sum_s C_{n+1}^k.
\]
г) Из тождества \((1 + x)^n(1 - x^2)^{-n} = (1 - x)^{-n}\) выведите, что
\[
\sum_s C_n^{k-2s} C_{n+s-1}^s = C_{n+k-1}^k.
\]
д) Из тождества \((1 - x^2)^{-p-1} = (1 + x)^{-p-1}(1 - x)^{-p-1}\) выведите, что
\[
\sum_s (-1)^s C_{p+2k-s}^p C_{p+s}^p = C_{p+k}^k.
\]

32. Из тождеств \((1 - x)^{2k} \left[1 - \left(\frac{x}{1-x}\right)^2\right]^k = (1 - 2x)^k\) для \(k = p\) и \(k = -p\) выведите, что \(\sum_s C_{p+s}^s C_{2p+2s+1}^{2p+2s+1} = 2^{m-1} C_{m+p-1}^p\).

33. Докажите, что \(\sum_s C_{p+s}^s C_{2p+m}^{2p+2s} = 2^{m-1} \frac{2p+m}{m} C_{m+p-1}^p\).

34. Из тождеств \((1 - x)^{2k} \left[1 + \frac{2x}{(1-x)^2}\right]^k = (1 + x^2)^k\) для \(k = p\) и \(k = -p\) выведите формулы
\[
\sum_s (-1)^s C_{p+s-1}^s C_{2m+2p+s}^{2m+1-s} 2^s = 0, \quad \sum_s (-1)^s C_{p+s-1}^s C_{2m+2p+s-1}^{2m-s} 2^s = (-1)^m C_{p+m-1}^m,
\]
\[
\sum_s (-1)^s C_p^s C_{2p-2s}^{2m+1-s} 2^s = 0, \quad \sum_s (-1)^s C_p^s C_{2p-2s}^{2m-s} 2^s = C_p^m.
\]
С их помощью докажите, что
\[
\sum_s C_{2p+2m}^{2s} C_{p+m-s}^p = 2^{2m} (p + m) \frac{(p + 2m - 1)!}{p! (2m)!},
\]
\[
\sum_s C_{2p+2m+1}^{2s+1} C_{p+m-s}^p = 2^{2m} (2p + 2m + 1) \frac{(p + 2m)!}{p! (2m + 1)!},
\]
\[
\sum_s C_{2p+2m}^{2s-1} C_{p+m-s}^p = 2^{2m-1} C_{p+2m-1}^p, \quad \sum_s C_{2p+2m+1}^{2s} C_{p+m-s}^p = 2^{2m} C_{p+2m}^p.
\]

35. Рассматривая формулы
\[
[(1 + x)^p \pm (1 - x)^p]^2 = (1 + x)^{2p} + (1 - x)^{2p} \pm 2(1 - x^2)^p,
\]
\[
[(1 + x)^p + (1 - x)^p] [(1 + x)^p - (1 - x)^p] = (1 + x)^{2p} - (1 - x)^{2p}
\]