---
source_image: page_444.png
page_number: 444
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.71
tokens: 7045
characters: 3211
timestamp: 2025-12-24T08:19:52.211085
finish_reason: stop
---

Доказательство. Первый изоморфизм задаётся формулами \( f(e_i) = 1 \otimes e_i \) при \( i = 1, 2 \) и \( f(e_i) = \varepsilon_{i-2} \otimes e_1 e_2 \) при \( i \geq 3 \). Второй изоморфизм задаётся формулами \( g(\varepsilon_i) = 1 \otimes \varepsilon_i \) при \( i = 1, 2 \) и \( g(\varepsilon_i) = e_{i-2} \otimes \varepsilon_1 \varepsilon_2 \) при \( i \geq 3 \).

Лемма 3. \( C_{k+4} \cong C_k \otimes M_2(\mathbb{H}) \) и \( C'_{k+4} \cong C'_k \otimes M_2(\mathbb{H}) \).

Доказательство. Согласно лемме 2 \( C_{k+4} = C'_{k+2} \otimes C_2 = C_k \otimes C'_2 \otimes C_2 \). А так как \( C'_2 \otimes C_2 = \mathbb{H} \otimes M_2(\mathbb{R}) = M_2(\mathbb{H}) \), то \( C_{k+4} = C_k \otimes M_2(\mathbb{H}) \). Аналогично \( C'_{k+4} = C'_k \otimes M_2(\mathbb{H}) \).

Лемма 4. \( C_{k+8} \cong C_k \otimes M_{16}(\mathbb{R}) \).

Доказательство. Согласно лемме 3

\[
C_{k+8} = C_{k+4} \otimes M_2(\mathbb{H}) = C_k \otimes M_2(\mathbb{H}) \otimes M_2(\mathbb{H}).
\]

А так как \( \mathbb{H} \otimes \mathbb{H} \cong M_4(\mathbb{R}) \) (см. п. 46.5), то

\[
M_2(\mathbb{H}) \otimes M_2(\mathbb{H}) = M_2(M_4(\mathbb{R})) = M_{16}(\mathbb{R}).
\]

Леммы 1 — 3 позволяют вычислить \( C_k \) при \( 1 \leq k \leq 8 \). Например, \( C_5 = C_1 \otimes M_2(\mathbb{H}) = \mathbb{C} \otimes M_2(\mathbb{H}) = M_2(\mathbb{C} \otimes \mathbb{H}) = M_2(M_2(\mathbb{C})) = M_4(\mathbb{C}) \); \( C_6 = C_2 \otimes M_2(\mathbb{H}) = M_2(\mathbb{H} \otimes \mathbb{H}) = M_8(\mathbb{R}) \) и т. д. Результаты вычислений записаны в таблице 2.

Таблица 2

<table>
  <tr>
    <th>k</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
  </tr>
  <tr>
    <th>C<sub>k</sub></th>
    <td>\( \mathbb{C} \)</td>
    <td>\( \mathbb{H} \)</td>
    <td>\( \mathbb{H} \oplus \mathbb{H} \)</td>
    <td>\( M_2(\mathbb{H}) \)</td>
  </tr>
  <tr>
    <th>C'<sub>k</sub></th>
    <td>\( \mathbb{R} \oplus \mathbb{R} \)</td>
    <td>\( M_2(\mathbb{R}) \)</td>
    <td>\( M_2(\mathbb{C}) \)</td>
    <td>\( M_2(\mathbb{H}) \)</td>
  </tr>
  <tr>
    <th>k</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th>8</th>
  </tr>
  <tr>
    <th>C<sub>k</sub></th>
    <td>\( M_4(\mathbb{C}) \)</td>
    <td>\( M_8(\mathbb{R}) \)</td>
    <td>\( M_8(\mathbb{R}) \oplus M_8(\mathbb{R}) \)</td>
    <td>\( M_{16}(\mathbb{R}) \)</td>
  </tr>
  <tr>
    <th>C'<sub>k</sub></th>
    <td>\( M_2(\mathbb{H}) \oplus M_2(\mathbb{H}) \)</td>
    <td>\( M_4(\mathbb{H}) \)</td>
    <td>\( M_8(\mathbb{C}) \)</td>
    <td>\( M_{16}(\mathbb{R}) \)</td>
  </tr>
</table>

Лемма 4 позволяет теперь вычислить \( C_k \) для любого \( k \). Алгебры \( C_1, \ldots, C_8 \) имеют естественные представления в пространствах \( \mathbb{C}, \mathbb{H}, \mathbb{H}^2, \mathbb{C}^4, \mathbb{R}^8, \mathbb{R}^8 \) и \( \mathbb{R}^{16} \); размерности этих пространств над \( \mathbb{R} \) равны 2, 4, 4, 8, 8, 8, 8 и 16. Кроме того, при переходе от алгебры \( C_k \) к алгебре \( C_{k+8} \) размерность пространства естественного представления увеличивается в 16 раз. Простой перебор показывает, что при \( n = 2^k \) наибольшее \( m \), для которого алгебра \( C_m \) имеет естественное представление в \( \mathbb{R}^n \), равно \( \rho(n) - 1 \).