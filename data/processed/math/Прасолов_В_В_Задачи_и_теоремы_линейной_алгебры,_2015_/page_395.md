---
source_image: page_395.png
page_number: 395
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.76
tokens: 6441
characters: 2068
timestamp: 2025-12-24T08:18:18.052944
finish_reason: stop
---

Достаточно проверить, что \( \sum_{r \leq i} \sum_{s \leq j} (\delta_{rs} - a_{rs}) \geq 0 \). Если \( i \leq j \), то \( \sum_{r \leq i} \sum_{s \leq j} \delta_{rs} = \sum_{r \leq i} \sum_{s=1}^n \delta_{rs} \), поэтому \( \sum_{r \leq i} \sum_{s \leq j} (\delta_{rs} - a_{rs}) \geq \sum_{r \leq i} \sum_{s=1}^n (\delta_{rs} - a_{rs}) = 0 \). Случай \( i \geq j \) разбирается аналогично.

41.2. Существует такая унитарная матрица \( U \), что \( H = U \Lambda U^* \), где
\[
\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n).
\]
Так как \( h_{ij} = \sum_k u_{ik} \overline{u}_{jk} \lambda_k \), то \( h_{ii} = \sum_k x_{ik} \lambda_k \), где \( x_{ik} = |u_{ik}|^2 \). Поэтому \( h = X \lambda \), где \( \lambda \) — столбец \( (\lambda_1, \ldots, \lambda_n) \) и \( X \) — дважды стохастическая матрица. Согласно теореме 41.2.1 \( X = \sum_{\sigma} t_{\sigma} P_{\sigma} \), где \( P_{\sigma} \) — матрица перестановки \( \sigma \), \( t_{\sigma} \geq 0 \) и \( \sum_{\sigma} t_{\sigma} = 1 \). Следовательно, \( h = \sum_{\sigma} t_{\sigma} (P_{\sigma} \lambda) \).

41.3. Пусть \( I + S + S^2 + \ldots + S^n = A(n) = \|a_{ij}(n)\|_1^n \). Матрица \( S^n \) неотрицательная, поэтому из равенства \( A(n) = A(n-1) + S^n \) следует, что \( a_{ij}(n-1) \leq a_{ij}(n) \).

Докажем по индукции, что \( a_{ij}(n) \leq a_{jj}(n-1) \) при \( i \neq j \). При \( n = 0 \) требуемое неравенство легко доказывается: \( a_{ij}(1) = s_{ij} \leq 1 = a_{jj}(0) \). Чтобы сделать шаг индукции, воспользуемся равенством \( A(n+1) = I + SA(n) \). Если \( i \neq j \), то из этого равенства следует, что \( a_{ij}(n+1) = \sum_{k=1}^n s_{ik} a_{kj}(n) \). Мы уже доказали неравенство \( a_{ij}(n-1) \leq a_{ij}(n) \). Кроме того, по предположению индукции \( a_{ij}(n) \leq a_{jj}(n-1) \) при \( i \neq j \). Значит, \( a_{ij}(n) \leq a_{jj}(n) \) (при \( i = j \) это неравенство очевидно). Поэтому \( a_{ij}(n+1) \leq \sum_{k=1}^n s_{ik} a_{jj}(n) = a_{jj}(n) \) при \( i \neq j \). Таким образом, если \( i \neq j \), то \( a_{ij}(n) \leq a_{jj}(n-1) \leq a_{jj}(n) \).