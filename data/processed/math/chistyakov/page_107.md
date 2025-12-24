---
source_image: page_107.png
page_number: 107
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.36
tokens: 5223
characters: 1486
timestamp: 2025-12-24T07:28:33.187210
finish_reason: stop
---

§ 1] МАТЕМАТИЧЕСКОЕ ОЖИДАНИЕ

Если интеграл (1.5) не сходится абсолютно, то говорят, что математическое ожидание \( M \xi \) не существует.

Пример 1. Найдем математическое ожидание выигрыша \( \xi \) первого игрока в примере 1 § 1 гл. 4. В этом примере

\[
\Omega = \{ \Gamma, P \}, \quad P(\{ \Gamma \}) = P(\{ P \}) = \frac{1}{2},
\]
\[
\xi(\Gamma) = 1, \quad \xi(P) = -1.
\]

По формуле (1.4)
\[
M \xi = \xi(\Gamma) P(\{ \Gamma \}) + \xi(P) P(\{ P \}) = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot (-1) = 0.
\]

Пример 2. Пусть в дискретном вероятностном пространстве (\$ 6 гл. 1) \( \Omega = \{ 1, 2, \ldots, k, \ldots \} \), \( p_k = \frac{1}{k(k+1)} \). Величины \( p_k \) удовлетворяют (1.6.4):

\[
\sum_{k=1}^{\infty} p_k = \sum_{k=1}^{\infty} \left( \frac{1}{k} - \frac{1}{k+1} \right) = 1.
\]

Положим \( \xi_1 = \xi_1(k) = (-1)^k \), \( \xi_2 = \xi_2(k) = (-1)^k k \). Так как ряд \( \sum_{k=1}^{\infty} \frac{(-1)^k}{k(k+1)} \) сходится абсолютно, то \( M \xi_1 \) существует. По формуле (1.4)

\[
M \xi_1 = \sum_{k=1}^{\infty} \xi_1(k) p_k =
\]
\[
= \sum_{k=1}^{\infty} \frac{(-1)^k}{k(k+1)} = \sum_{k=1}^{\infty} (-1)^k \left[ \frac{1}{k} - \frac{1}{k+1} \right] =
\]
\[
= \sum_{k=1}^{\infty} \frac{(-1)^k}{k} + \sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k+1} = 1 + 2 \sum_{k=1}^{\infty} \frac{(-1)^k}{k}.
\]

Полагая в разложении
\[
- \ln(1+x) = \sum_{k=1}^{\infty} (-1)^k \frac{x^k}{k}
\]
\( x = 1 \), получим \( \sum_{k=1}^{\infty} \frac{(-1)^k}{k} = - \ln 2 \). Таким образом,