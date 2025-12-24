---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.41
tokens: 12498
characters: 2878
timestamp: 2025-12-24T07:05:10.533135
finish_reason: stop
---

или, в матричной форме, \( \vec{X} = Z^T \vec{\beta} + \vec{\varepsilon} \), где матрица \( Z(k \times n) \) называется «матрицей плана»:

\[
Z = \begin{pmatrix}
Z_1^{(1)} & \ldots & Z_1^{(n)} \\
\vdots & \ldots & \vdots \\
Z_k^{(1)} & \ldots & Z_k^{(n)}
\end{pmatrix} = (\overrightarrow{Z^{(1)}} \ldots \overrightarrow{Z^{(n)}}).
\]

Требуется по данным матрице плана \( Z \) и вектору результатов \( \vec{X} \) найти оценки для параметров регрессии \( \vec{\beta} \) и вектора ошибок \( \vec{\varepsilon} \) (например, для его числовых характеристик \( E\varepsilon, D\varepsilon, \) матрицы ковариаций и т.д.). Мы рассмотрим только проблему оценивания \( \vec{\beta} \).

**Предположение 1.** *Матрица \( Z \) имеет ранг \( k \), т.е. все \( k \) ее строк линейно независимы.*

**Лемма 12.** *Предположение 1 \( \iff \) матрица \( A = Z \cdot Z^T \) положительно определена.*

**Напоминание 1.** *Матрица \( A(k \times k) \) положительно определена, если \( \vec{t}^T A \vec{t} \geq 0 \) для любого \( \vec{t} = (t_1, \ldots, t_k), \) и \( \vec{t}^T A \vec{t} = 0 \iff \vec{t} \equiv 0. \)*

**Напоминание 2.** *Норма вектора (столбца) \( \vec{u} = (u_1, \ldots, u_k) \) есть \( \vec{u}^T \vec{u} = \sum_{i=1}^k u_i^2 \geq 0, \) и равна нулю \( \iff \vec{u} \equiv 0. \)*

**Доказательство леммы 12.** Благодаря напоминанию 2, \( \vec{t}^T A \vec{t} = \vec{t}^T Z \cdot Z^T \vec{t} = (Z^T \vec{t})^T \cdot (Z^T \vec{t}) \geq 0, \)
причем \( (Z^T \vec{t})^T \cdot (Z^T \vec{t}) = 0 \iff Z^T \vec{t} = 0. \)
Но «ранг \( Z \) равен \( k \)» как раз и означает, по определению, что \( Z^T \vec{t} = 0 \iff \vec{t} = 0. \)

\(\square\)

9.4 **Метод наименьших квадратов. Нормальное уравнение**

Обозначим

\[
S(\vec{\beta}) = \sum_{i=1}^n \varepsilon_i^2 = \sum_{i=1}^n \left( X_i - \sum_{j=1}^k \beta_j Z_j^{(i)} \right)^2 = (\vec{X} - Z^T \vec{\beta})^T \cdot (\vec{X} - Z^T \vec{\beta}).
\]

**Определение 33.** Если \( S(\widehat{\vec{\beta}}) = \min_{\vec{\beta}} S(\vec{\beta}) \), то \( \widehat{\vec{\beta}} \) называется оценкой метода наименьших квадратов (ОМНК) вектора \( \vec{\beta} \). Здесь \( \widehat{\vec{\beta}} = (\widehat{\beta}_1, \ldots, \widehat{\beta}_k) \).

Найдем систему уравнений, определяющих точку экстремума функции \( S(\vec{\beta}) \) (пока только точку экстремума!).

\[
\frac{\partial S}{\partial \beta_m} = -2 \sum_{i=1}^n Z_m^{(i)} \left( X_i - \sum_{j=1}^k \beta_j Z_j^{(i)} \right) \Bigg|_{\vec{\beta} = \widehat{\vec{\beta}}} = 0, \ m = 1, \ldots, k.
\]

Раскрыв скобки, получим систему

\[
\sum_{i=1}^n Z_m^{(i)} X_i = \sum_{i=1}^n Z_m^{(i)} \sum_{j=1}^k \beta_j Z_j^{(i)}, \ m = 1, \ldots, k. \tag{18}
\]

Слева стоит \( m \)-я координата вектора \( Z \vec{X} \), справа — \( m \)-я координата вектора \( ZZ^T \vec{\beta} \), так что систему уравнений 18 можно записать в виде

\[
Z \vec{X} = Z \cdot Z^T \vec{\beta} = A \vec{\beta}.
\]