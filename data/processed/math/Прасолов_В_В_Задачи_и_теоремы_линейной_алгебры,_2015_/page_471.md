---
source_image: page_471.png
page_number: 471
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.05
tokens: 6913
characters: 3187
timestamp: 2025-12-24T08:20:40.160077
finish_reason: stop
---

этому \( \dim \operatorname{Ker} \varphi_0 = \dim \operatorname{Ker} \varphi_1 \). Если \( U \in \operatorname{Ker} \varphi_i \), то \( BR = RA \) и \( BS = SB \).
Поэтому можно рассмотреть пространство

\[
V = \{ (R, S) \in M_{n, m+n} \mid BR = RA,\ BS = SB \}
\]

и определить проекции \( \mu_i : \operatorname{Ker} \varphi_i \to V \), где \( \mu_i(U) = (R, S) \). Легко проверить, что

\[
\operatorname{Ker} \mu_i = \left\{ \begin{pmatrix} P & Q \\ 0 & 0 \end{pmatrix} \mid AP = PA,\ AQ = QB \right\}.
\]

Для \( \mu_0 \) это очевидно, а для \( \mu_1 \) следует из того, что \( CR = 0 \) и \( CS = 0 \), так как \( R = 0 \) и \( S = 0 \).

Докажем, что \( \operatorname{Im} \mu_0 = \operatorname{Im} \mu_1 \). Если \( (R, S) \in V \), то \( \begin{pmatrix} 0 & 0 \\ R & S \end{pmatrix} \in \operatorname{Ker} \varphi_0 \).
Поэтому \( \operatorname{Im} \mu_0 = V \), а значит, \( \operatorname{Im} \mu_1 \subset \operatorname{Im} \mu_0 \). С другой стороны,

\[
\dim \operatorname{Im} \mu_0 + \dim \operatorname{Ker} \mu_0 = \dim \operatorname{Ker} \varphi_0 = \dim \operatorname{Ker} \varphi_1 =
= \dim \operatorname{Im} \mu_1 + \dim \operatorname{Ker} \mu_1.
\]

Матрица \( \begin{pmatrix} I & 0 \\ 0 & -I \end{pmatrix} \) лежит в \( \operatorname{Ker} \varphi_0 \), поэтому \( (0, -I) \in \operatorname{Im} \mu_0 = \operatorname{Im} \mu_1 \).
Следовательно, в \( \operatorname{Ker} \varphi_1 \) есть матрица вида \( \begin{pmatrix} P & Q \\ 0 & -I \end{pmatrix} \). Значит, \( AQ + + CS - QB = 0 \), где \( S = -I \). Поэтому \( X = Q \) — решение уравнения \( AX - XB = C \).

Обратно, если \( X \) — решение данного уравнения, то

\[
\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \begin{pmatrix} I & X \\ 0 & I \end{pmatrix} = \begin{pmatrix} A & AX \\ 0 & B \end{pmatrix} = \begin{pmatrix} A & C + XB \\ 0 & B \end{pmatrix} = \begin{pmatrix} I & X \\ 0 & I \end{pmatrix} \begin{pmatrix} A & C \\ 0 & B \end{pmatrix},
\]

а значит, \( \begin{pmatrix} I & X \\ 0 & I \end{pmatrix}^{-1} \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \begin{pmatrix} I & X \\ 0 & I \end{pmatrix} = \begin{pmatrix} A & C \\ 0 & B \end{pmatrix} \).

б) Предположим сначала, что указанные матрицы одного ранга. Пусть \( U = \begin{pmatrix} U_{11} & U_{12} \\ U_{21} & U_{22} \end{pmatrix} \) и \( W = \begin{pmatrix} W_{11} & W_{12} \\ W_{21} & W_{22} \end{pmatrix} \). Рассмотрим для \( i = 0, 1 \) отображения \( \psi_i : M_{m+n, 2(m+n)} \to M_{m+n, m+n} \), заданные формулами

\[
\psi_0(U, W) = \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} U - W \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} = \begin{pmatrix} AU_{11} - W_{11}A & AU_{12} - W_{12}B \\ BU_{21} - W_{21}A & BU_{22} - W_{22}B \end{pmatrix},
\]
\[
\psi_1(U, W) = \begin{pmatrix} A & C \\ 0 & B \end{pmatrix} U - W \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} =
= \begin{pmatrix} AU_{11} + CU_{21} - W_{11}A & AU_{12} + CU_{22} - W_{12}B \\ BU_{21} - W_{21}A & BU_{22} - W_{22}B \end{pmatrix}.
\]

Пространства решений уравнений \( FU = WF \) и \( GFG^{-1}U' = W'F \) изоморфны; этот изоморфизм задаётся формулами \( U = G^{-1}U' \) и \( W = = G^{-1}W' \). Поэтому \( \dim \operatorname{Ker} \varphi_0 = \dim \operatorname{Ker} \varphi_1 \).