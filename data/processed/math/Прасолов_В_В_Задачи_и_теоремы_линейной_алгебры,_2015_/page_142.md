---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.43
tokens: 6880
characters: 3162
timestamp: 2025-12-24T08:11:36.220543
finish_reason: stop
---

всеми матрицами \( C_{12} \). Тогда \( f(U) \subset M_{r, r} \oplus H \). Пространства \( M_{r, n-r} \) и \( M_{n-r, r} \) можно отождествить операцией транспонирования; для \( B_{21} \in M_{n-r, r} \) и \( X_{12} \in M_{r, n-r} \) величину \( \operatorname{tr}(B_{21}X_{12}) \) можно рассматривать как скалярное произведение в \( M_{r, n-r} \). Относительно этого скалярного произведения \( H \subset (\operatorname{Ker}\, f)^{\perp} \), поэтому \( \dim H \leqslant r(n - r) - \dim \operatorname{Ker}\, f \), а значит, \( \dim f(U) \leqslant r^2 + \dim H \leqslant nr - \dim \operatorname{Ker}\, f \). А так как \( nr = \dim \operatorname{Im}\, f + \dim \operatorname{Ker}\, f \), то \( H = (\operatorname{Ker}\, f)^{\perp} \), \( \dim H + \dim \operatorname{Ker}\, f = r(n - r) \) и \( \dim f(U) = r^2 + \dim H \), т. е. \( f(U) = M_{r, r} \oplus H \) и \( \operatorname{Ker}\, f = H^{\perp} \).

Выберем в \( M_{n-r, r} \) подпространство \( L \) так, что \( M_{n-r, r} = \operatorname{Ker}\, f \oplus L \). Существует единственное линейное отображение \( \lambda : f(U) \to L \), делающее диаграмму

\[
\begin{array}{ccc}
U & \xrightarrow{f} & M_{r, r} \oplus H = f(U) \\
| & & | \\
M_{n-r, r} & \xrightarrow{h} & M_{n-r, r} \oplus L \\
& & \downarrow \lambda \\
& & L
\end{array}
\]

коммутативной; здесь \( h \left( \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & 0 \end{pmatrix} \right) = C_{21} \), \( p \) — естественная проекция \( M_{n-r, r} = \operatorname{Ker}\, f \oplus L \) на \( L \). В самом деле, если \( (C_{11}, C_{12}) \in f(U) \), то в \( M_{n-r, r} \) найдётся такая матрица \( C_{21} \), что \( \left( \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & 0 \end{pmatrix} \right) \in U \), причём матрица \( C_{21} \) определена с точностью до слагаемого из \( \operatorname{Ker}\, f \). Таким образом, мы получаем отображение \( \lambda : f(U) \to M_{n-r, r}/\operatorname{Ker}\, f = L \). Легко проверить, что это отображение линейно. Докажем, что \( \lambda \equiv 0 \). Если \( C_{11} \in M_{r, r} \) и \( C_{12} \in H \), то существует матрица \( \left( \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & 0 \end{pmatrix} \right) \in U \). Тогда \( \lambda(C_{11}, C_{12}) = C_{21} \), поэтому согласно лемме 1 \( \lambda(C_{11}, C_{12})C_{12} = 0 \). Аналогично, \( \lambda(C_{11}, -C_{12})C_{12} = 0 \). Следовательно,

\[
\lambda(C_{11}, 0)C_{12} = \lambda(C_{11}, C_{12} - C_{12})C_{12} = 0,
\]

т. е. \( \lambda(C_{11}, 0) \in H^{\perp} = \operatorname{Ker}\, f \), а значит, \( \lambda(C_{11}, 0) \in L \cap \operatorname{Ker}\, f = 0 \). Величина \( \lambda(C_{11}, C_{12}) = \lambda(C_{11}, 0) + \lambda(0, C_{12}) = \lambda(0, C_{12}) \) зависит только от \( C_{12} \); обозначим её \( \lambda(C_{12}) \). Пусть \( C_{12} \in H \) — ненулевая матрица, \( v \) — её ненулевой столбец. Тогда если \( C_{11} \in M_{r, r} \) и \( u \) — строка \( \lambda(C_{12}) \), то

\[
0 \equiv \begin{vmatrix} C_{11} & v \\ u & 0 \end{vmatrix} = -u \cdot \operatorname{adj}\, C_{11} \cdot v.
\]

Матрицу \( C_{11} \) можно подобрать так, чтобы матрица \( \operatorname{adj}\, C_{11} \) имела ровно один ненулевой элемент, причём этот элемент может стоять в лю-