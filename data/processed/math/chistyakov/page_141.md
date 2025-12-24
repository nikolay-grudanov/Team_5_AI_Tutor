---
source_image: page_141.png
page_number: 141
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.55
tokens: 5261
characters: 1486
timestamp: 2025-12-24T07:29:25.388043
finish_reason: stop
---

§ 1] ПРОИЗВОДЯЩИЕ ФУНКЦИИ

где \( P(\xi_k = 1) = 1 - P(\xi_k = 0) = p, \ k = 1, 2, \ldots, n \). По теореме 1.3

\[
\varphi_{\mu_n}(x) = \varphi_{\xi_1}(x) \varphi_{\xi_2}(x) \ldots \varphi_{\xi_n}(x).
\]

Производящие функции слагаемых получим по формуле (1.4):

\[
\varphi_{\xi_k}(x) = x p + x^0 q = p x + q, \quad k = 1, \ldots, n.
\]

Таким образом,

\[
\varphi_{\mu_n}(x) = (p x + q)^n.
\]

Найдем производящую функцию случайного числа случайных слагаемых.

Теорема 1.4. Пусть целочисленные величины \( v, \xi_1, \xi_2, \ldots, \xi_n \) независимы при любом \( n = 1, 2, 3, \ldots; \xi_k, \ k = 1, 2, \ldots, \) одинаково распределены. Положим

\[
\xi_v = \xi_1 + \xi_2 + \ldots + \xi_v, \quad \xi_0 = 0.
\]

Тогда

\[
\varphi_{\xi_v}(x) = \varphi_v[\varphi_{\xi_1}(x)].
\] (1.13)

Доказательство. Вероятность события \( (\xi_v = m) \) представим в виде

\[
P(\xi_v = m) = \sum_{k=0}^{\infty} P(v = k, \xi_v = m).
\]

Так как \( (v = k, \xi_v = m) = (v = k, \xi_k = m) \) и события \( (v = k), (\xi_k = m) \) независимы, то

\[
P(v = k, \xi_v = m) = P(v = k, \xi_k = m) =
= P(v = k, \xi_1 + \ldots + \xi_k = m) = P(v = k) P(\xi_1 + \ldots + \xi_k = m).
\]

Тогда

\[
P(\xi_v = m) = \sum_{k=0}^{\infty} P(v = k) P(\xi_1 + \xi_2 + \ldots + \xi_k = m).
\]

Умножив обе части этого равенства на \( x^m \) и просуммировав по \( m = 0, 1, 2, \ldots \), получим

\[
\varphi_{\xi_v}(x) = \sum_{k=0}^{\infty} P(v = k) \left( \sum_{m=0}^{\infty} x^m P(\xi_1 + \ldots + \xi_k = m) \right).
\]