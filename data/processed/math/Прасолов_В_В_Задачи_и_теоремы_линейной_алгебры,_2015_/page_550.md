---
source_image: page_550.png
page_number: 550
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.66
tokens: 6819
characters: 3238
timestamp: 2025-12-24T08:22:46.584392
finish_reason: stop
---

ров и отбросим в нём все векторы, кроме первых \( k \) векторов. Совпадающие наборы \( k \) векторов получаются в том случае, когда в качестве последних \( n - k \) векторов берётся ортонормированный базис ортогонального дополнения к подпространству, натянутому на данные \( k \) векторов. Все такие ортонормированные базисы вместе образуют пространство \( \mathrm{Sp}(n - k) \).

Непосредственно из определения видно, что \( V_n(\mathbb{H}^n) = \mathrm{Sp}(n) \) и \( V_1(\mathbb{H}^n) = S^{4n-1} \) — единичная сфера в \( \mathbb{H}^n \).

**Теорема 59.9.2.** *Первая ненулевая гомотопическая группа пространства \( \mathrm{GL}(n, \mathbb{H}) \) — это группа \( \pi_3(\mathrm{GL}(n, \mathbb{H})) = \mathbb{Z} \).*

**Доказательство.** Запишем гомотопическую точную последовательность расслоения \( \mathrm{Sp}(n+1) \to V_{n+1}(\mathbb{H}^{n+1}) \) со слоем \( \mathrm{Sp}(n) \):

\[
\ldots \to \pi_{i+1}(S^{4n+3}) \to \pi_i(\mathrm{Sp}(n)) \to \pi_i(\mathrm{Sp}(n+1)) \to \pi_i(S^{4n+3}) \to \ldots
\]

Если \( i \leq 4n + 1 \), то \( \pi_{i+1}(S^{4n+3}) = \pi_i(S^{4n+3}) = 0 \), поэтому \( \pi_i(\mathrm{Sp}(n)) \cong \cong \pi_i(\mathrm{Sp}(n+1)) \). При \( i = 3 \) неравенство \( i \leq 4n + 1 \) выполняется для всех \( n \), поэтому \( \pi_3(\mathrm{Sp}(n)) \cong \pi_3(\mathrm{Sp}(1)) = \pi_3(S^3) = \mathbb{Z} \).

**Теорема 59.9.3.** *Отображение \( S^3 \to \mathrm{GL}(n, \mathbb{H}) \), при котором \( \lambda \in S^3 \subset \mathbb{H} \) отображается в матрицу \( \lambda I \), представляет элемент \( n \) гомотопической группы \( \pi_3(\mathrm{GL}(n, \mathbb{H})) = \mathbb{Z} \).*

**Доказательство.** Если проследить за отображениями в точных последовательностях из доказательства теоремы 59.9.2, то можно установить, что образующей группы \( \pi_3(\mathrm{GL}(n, \mathbb{H})) \) служит отображение \( S^3 \to \mathrm{GL}(n, \mathbb{H}) \), при котором \( \lambda \in S^3 \subset \mathbb{H} \) отображается в матрицу \( \mathrm{diag}(\lambda, 1, \ldots, 1) \). Отображение \( S^3 \to S^3 \), заданное формулой \( \lambda \mapsto \lambda^n \), имеет степень \( n \), поэтому отображение \( S^3 \to \mathrm{GL}(n, \mathbb{H}) \), при котором \( \lambda \in S^3 \subset \mathbb{H} \) отображается в матрицу \( \mathrm{diag}(\lambda^n, 1, \ldots, 1) \), представляет элемент \( n \) группы \( \pi_3(\mathrm{GL}(n, \mathbb{H})) = \mathbb{Z} \). Остаётся доказать, что отображения \( \lambda \mapsto \mathrm{diag}(\lambda^n, 1, \ldots, 1) \) и \( \lambda \mapsto \mathrm{diag}(\lambda, \ldots, \lambda) \) гомотопны. Для этого достаточно проверить, что отображения \( \lambda \mapsto \mathrm{diag}(\lambda^{k+1}, 1) \) и \( \lambda \mapsto \mathrm{diag}(\lambda^k, \lambda) \) гомотопны, а затем за несколько шагов построить гомотопию между требуемыми отображениями.

Гомотопия, связывающая отображения \( \lambda \mapsto \mathrm{diag}(\lambda^{k+1}, 1) \) и \( \lambda \mapsto \mathrm{diag}(\lambda^k, \lambda) \), задаётся формулой

\[
f_t(\lambda) = \begin{pmatrix} \lambda^k & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & \lambda \end{pmatrix} \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix},
\]

где \( 0 \leq t \leq \pi/2 \).