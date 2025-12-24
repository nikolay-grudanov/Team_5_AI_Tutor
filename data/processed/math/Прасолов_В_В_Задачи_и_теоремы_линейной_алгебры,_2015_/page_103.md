---
source_image: page_103.png
page_number: 103
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.42
tokens: 5906
characters: 871
timestamp: 2025-12-24T08:10:03.983220
finish_reason: stop
---

с элементами \(-1\) над главной диагональю. Поэтому согласно теореме 3.1.4 \(|A_n| = \varepsilon (a \det B + u(\operatorname{adj} B)v)\). Разберем отдельно случаи чётного и нечётного \(n\).

Пусть \(n = 2k\). Тогда \(\varepsilon = (-1)^k\) и \(\det B = 0\) (см. задачу 1.1). Матрица \(\operatorname{adj} B\) вычислена в задаче 2.12. Легко проверить, что \(u(\operatorname{adj} B) = k(1, -1, 1, -1, \ldots)\), поэтому \(u(\operatorname{adj} B)v = k(k + 1)\). Следовательно, \(|A_{2k}| = (-1)^k k(k + 1)\).

Пусть теперь \(n = 2k + 1\). Тогда \(\varepsilon = (-1)^k\), \(a = 2k^2 + k + 1\) и \(\det B = 1\) (см. задачу 1.3). Легко проверить, что \(u(\operatorname{adj} B) = (-k, k + 1, -k, k + 1, \ldots) = -k(1, -1, 1, -1, \ldots) + (0, 1, 0, 1, \ldots)\), поэтому \(u(\operatorname{adj} B)v = -k^2 + k(k + 1) = k\). Следовательно, \(|A_{2k+1}| = (-1)^k (2k^2 + 2k + 1)\).