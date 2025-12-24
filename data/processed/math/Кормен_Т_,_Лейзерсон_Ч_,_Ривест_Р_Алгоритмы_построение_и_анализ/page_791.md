---
source_image: page_791.png
page_number: 791
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.68
tokens: 11424
characters: 1689
timestamp: 2025-12-24T06:57:17.990367
finish_reason: stop
---

Compute-Good-Suffix-Function(P,m)
1 \pi \gets Compute-Prefix-Function(P,m)
2 P' \gets обращение строки P
3 \pi' \gets Compute-Prefix-Function(P',m)
4 for j \gets 0 to m
5 do \gamma[j] \gets m-\pi[m]
6 for l \gets 1 to m
7 do j \gets m - \pi'[l]
8 if \gamma[j] > l - \pi'[l]
9 then \gamma[j] \gets l - \pi'[l]
10 return \gamma

Процедура Compute-Good-Suffix-Function проводит вычисления в точности по формуле (34.9). Её время работы есть O(m).

Время работы алгоритма Бо́йера — Мура в худшем случае есть O((n - m + 1)m + |\Sigma|), поскольку на исполнение Compute-LastOccurrence-Function уходит время O(m + |\Sigma|), на Compute-Good-Suffix-Function уходит O(m), и в худшем случае алгоритм Бо́йера — Мура (как и алгоритм Рабина — Карпа) потратит время O(m) на проверку каждого априори возможного сдвига. На практике, однако, именно алгоритм Бо́йера-Мура часто оказывается наиболее эффективным.

34.5.3 Упражнения

34.5-1
Вычислите функции \( \lambda \) и \( \gamma \) для строки \( P = 0101101201 \).

34.5-2
Покажите на примерах, что эвристики стоп-символа и эвристика безопасного суффикса, действуя вместе, могут дать большой выигрыш по сравнению с использованием только эвристики безопасного суффикса.

34-5.3*
На практике вместо функции \( \gamma \) часто используют усовершенствованную функцию \( \gamma' \), определенную так:

\[
\gamma'[j] = m - \max \{ k : 0 \leq k < m, P[j+1..m] \sim P_k \\
\quad \text{и} \ (k - m + j > 0 \Rightarrow P[j] \neq P[k - m + j]) \}
\]

(иными словами, мы дополнительно требуем, чтобы при новом сдвиге напротив стоп-символа в тексте стоял не тот же заведомо негодный символ образца, что при предыдущем). Как эффективно вычислять функцию \( \gamma' \)?