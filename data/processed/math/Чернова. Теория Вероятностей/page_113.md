---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.24
tokens: 11901
characters: 2759
timestamp: 2025-12-24T08:29:31.236830
finish_reason: stop
---

изменится, если заменить \( \nu_n \) и \( \mu_n \) на другие случайные величины с теми же распределениями.

Первое, что мы сделаем — докажем, что для двух случайных величин \( \xi \) и \( \eta \) (где угодно заданных) «расстояние между распределениями», то есть \( \sup_A | P(\xi \in A) - P(\eta \in A) | \), не больше, чем вероятность \( P\left( \tilde{\xi} \neq \tilde{\eta} \right) \) двум произвольным случайным величинам \( \tilde{\xi}, \tilde{\eta} \) с данными распределениями не совпадать. Понятно, что эти новые с.в. должны быть заданы на одном вероятностном пространстве, и наилучшая оценка сверху получится, если нам удастся так задать на одном вероятностном пространстве с.в. \( \tilde{\xi} \), распределенную как \( \xi \), и \( \tilde{\eta} \), распределенную как \( \eta \), чтобы вероятность \( P\left( \tilde{\xi} \neq \tilde{\eta} \right) \) была наименьшей.

Лемма 9 (Неравенство каплинга). Пусть \( \xi \) и \( \eta \) — произвольные с.в. Пусть случайная величина \( \tilde{\xi} \) одинаково распределена с \( \xi \), случайная величина \( \tilde{\eta} \) одинаково распределена с \( \eta \), и величины \( \tilde{\xi}, \tilde{\eta} \) заданы на одном вероятностном пространстве. Тогда

\[
\sup_{A \subseteq \mathbb{R}} | P(\xi \in A) - P(\eta \in A) | \leq P\left( \tilde{\xi} \neq \tilde{\eta} \right).
\]

Замечание 28. Каплингом (coupling) двух с.в. \( \xi \) и \( \eta \) называют задание на одном вероятностном пространстве случайных величин \( \tilde{\xi} \), распределенной как \( \xi \), и \( \tilde{\eta} \), распределенной как \( \eta \).

Доказательство неравенства каплинга. Воспользуемся равенством \( P(C) = P(C \cap B) + P(C \cap \overline{B}) \), а также тем, что вероятность пересечения двух событий не превосходит вероятности любого из них. Для любого множества \( A \subseteq \mathbb{R} \)

\[
P(\xi \in A) = P\left( \tilde{\xi} \in A \right) = P\left( \tilde{\xi} \in A, \tilde{\xi} = \tilde{\eta} \right) + P\left( \tilde{\xi} \in A, \tilde{\xi} \neq \tilde{\eta} \right) = P\left( \tilde{\eta} \in A, \tilde{\xi} = \tilde{\eta} \right) + P\left( \tilde{\xi} \in A, \tilde{\xi} \neq \tilde{\eta} \right) \leq P\left( \tilde{\eta} \in A \right) + P\left( \tilde{\xi} \neq \tilde{\eta} \right) = P(\eta \in A) + P\left( \tilde{\xi} \neq \tilde{\eta} \right),
\]
то есть
\[
P(\xi \in A) - P(\eta \in A) \leq P\left( \tilde{\xi} \neq \tilde{\eta} \right).
\]
Поменяем местами \( \xi \) и \( \eta \) и получим, что для любого множества \( A \subseteq \mathbb{R} \)
\[
| P(\xi \in A) - P(\eta \in A) | \leq P\left( \tilde{\xi} \neq \tilde{\eta} \right).
\]
Займемся заданием на одном вероятностном пространстве величин \( \tilde{\nu}_n \) и \( \tilde{\mu}_n \), распределенных как \( \nu_n \) и \( \mu_n \), соответственно.