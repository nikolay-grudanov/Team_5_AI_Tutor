---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.88
tokens: 5393
characters: 1720
timestamp: 2025-12-24T07:30:14.464629
finish_reason: stop
---

§ 21 УРАВНЕНИЕ ДЛЯ ВЕРОЯТНОСТЕЙ ПЕРЕХОДА

Используя (1.9) и теорему 1.2, получим
\[
P(\xi_{t_1} = l_1, \ldots, \xi_{t_s} = l_s | \xi_0 = k) =
\]
\[
= P(\xi_{t_1} = l_1 | \xi_0 = k) P(\xi_{t_2} = l_2 | \xi_0 = k, \xi_{t_1} = l_1) \times \ldots
\]
\[
\ldots \times P(\xi_{t_s} = l_s | \xi_0 = k, \xi_{t_1} = l_1, \ldots, \xi_{t_{s-1}} = l_{s-1}) =
\]
\[
= P(\xi_{t_1} = l_1 | \xi_0 = k) P(\xi_{t_2} = l_2 | \xi_{t_1} = l_1) \ldots
\]
\[
\ldots P(\xi_{t_s} = l_s | \xi_{t_{s-1}} = l_{s-1}) =
\]
\[
= P_{k l_1}(t_1) P_{l_1 l_2}(t_2 - t_1) \ldots P_{l_{s-1} l_s}(t_s - t_{s-1}).
\]
Отсюда и из (2.2) найдем
\[
P(\xi_{t_1} = l_1, \ldots, \xi_{t_s} = l_s) =
\]
\[
= \sum_{k=1}^N q_k P_{k l_1}(t_1) P_{l_1 l_2}(t_2 - t_1) \ldots P_{l_{s-1} l_s}(t_s - t_{s-1}). \tag{2.3}
\]
Для вычислений по формуле (2.3) нужно уметь находить \( P_{ij}(t) \).

Теорема 2.1. При любых \( s, t \)
\[
P_{ij}(t+s) = \sum_{k=1}^N P_{ik}(s) P_{kj}(t), \quad i, j = 1, 2, \ldots, N. \tag{2.4}
\]

Доказательство. Вычислим вероятность \( P(\xi_{t+s} = j | \xi_0 = i) \) по формуле полной вероятности (2.3.1), положив \( B_k = (\xi_s = k) \):
\[
P(\xi_{t+s} = j | \xi_0 = i) =
\]
\[
= \sum_{k=1}^N P(\xi_s = k | \xi_0 = i) P(\xi_{t+s} = j | \xi_0 = i, \xi_s = k). \tag{2.5}
\]
Из равенства (1.9) и теоремы 1.2 следует
\[
P(\xi_{t+s} = j | \xi_0 = i, \xi_s = k) =
\]
\[
= P(\xi_{t+s} = j | \xi_s = k) = P(\xi_t = j | \xi_0 = k).
\]
Отсюда и из равенств (2.5) и (1.12) получаем утверждение теоремы. Определим матрицу \( P(t) = \| P_{ij}(t) \| \). В матричной записи (2.4) имеет вид
\[
P(t+s) = P(s) P(t). \tag{2.6}
\]
Так как \( P_{ij}(1) = p_{ij} \), то \( P(1) = P \), где \( P \) — матрица (1.3). Из (2.6) следует
\[
P(t) = (P(1))^t = P^t. \tag{2.7}
\]