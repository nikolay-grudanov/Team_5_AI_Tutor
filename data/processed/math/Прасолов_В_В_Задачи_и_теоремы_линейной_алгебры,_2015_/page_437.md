---
source_image: page_437.png
page_number: 437
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.40
tokens: 6735
characters: 2889
timestamp: 2025-12-24T08:19:38.022547
finish_reason: stop
---

докажем, что образ отображения w совпадает с \( M_4(\mathbb{R}) \). Матрицы

\[
e = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad \varepsilon = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad a = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad b = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
\]

образуют базис пространства матриц порядка 2. Образы элементов \( x \otimes y \), где \( x, y \in \{1, i, j, k\} \), при отображении w приведены в таблице 1. Из этой таблицы видно, что среди линейных комбинаций пар образов этих элементов встречаются все матрицы, три блока которых нулевые, а четвёртым блоком является одна из матриц \( e, \varepsilon, a \) и \( b \). Среди линейных комбинаций чётвёрок этих матриц встречаются все матрицы, содержащие ровно один ненулевой элемент, причём этот элемент равен 1. Такие матрицы образуют базис пространства \( M_4(\mathbb{R}) \).

Таблица 1

<table>
  <tr>
    <th rowspan="2">x</th>
    <th colspan="4">y</th>
  </tr>
  <tr>
    <th>1</th>
    <th>i</th>
    <th>j</th>
    <th>k</th>
  </tr>
  <tr>
    <td>1</td>
    <td>\( \begin{pmatrix} e & 0 \\ 0 & e \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} b & 0 \\ 0 & -b \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} 0 & e \\ -e & 0 \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} 0 & b \\ b & 0 \end{pmatrix} \)</td>
  </tr>
  <tr>
    <td>i</td>
    <td>\( \begin{pmatrix} -b & 0 \\ 0 & -b \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} e & 0 \\ 0 & -e \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} 0 & -b \\ b & 0 \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} 0 & e \\ e & 0 \end{pmatrix} \)</td>
  </tr>
  <tr>
    <td>j</td>
    <td>\( \begin{pmatrix} 0 & -\varepsilon \\ \varepsilon & 0 \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} 0 & a \\ a & 0 \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} \varepsilon & 0 \\ 0 & \varepsilon \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} -a & 0 \\ 0 & a \end{pmatrix} \)</td>
  </tr>
  <tr>
    <td>k</td>
    <td>\( \begin{pmatrix} 0 & -a \\ a & 0 \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} 0 & -\varepsilon \\ -\varepsilon & 0 \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} a & 0 \\ 0 & a \end{pmatrix} \)</td>
    <td>\( \begin{pmatrix} \varepsilon & 0 \\ 0 & -\varepsilon \end{pmatrix} \)</td>
  </tr>
</table>

46.6. Числа Кэли

Удвоением алгебры кватернионов с естественной операцией сопряжения является алгебра Кэли (алгебра октав). Октавы открыл Джон Грейвз в декабре 1843 г., после того как в октябре он получил письмо от Гамильтона, сообщившего о своём открытии кватернионов. Но Грейвз опубликовал свою работу лишь в 1848 г. За это время октавы переоткрыл Кэли в 1845 г.

Базисом алгебры Кэли как пространства над \( \mathbb{R} \) служат элементы 1, \( i, j, k, e, f = ie, g = je \) и \( h = ke \). Таблицу умножения базисных элементов удобно представить с помощью рис. 10. Произведением двух эле-