---
source_image: page_711.png
page_number: 711
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.00
tokens: 11714
characters: 2275
timestamp: 2025-12-24T06:53:53.644204
finish_reason: stop
---

готавливается преобразование Фурье всего вектора \(a\).

Соответствующая программа использует вектор \(A[0..n-1]\) в котором в начале работы мы помещаем элементы вектора \(a\) в том порядке, в котором идут листья дерева рис. 32.4. (Что это за порядок, мы обсудим дальше.) Введём также переменную \(s\), в которой будет содержаться текущий номер уровня в дереве рекурсии (растущий от \(s=1\) для листьев до \(\lg n\) для корня, когда мы получаем \(n\)-элементный результат). Вот схема программы:

1 for $s \leftarrow 1$ to $\lg n$
2 \quad do for $k \leftarrow 0$ to $n-1$ by $2^s$
3 \qquad do преобразовать два $2^{s-1}$-элементных куска
\quad\qquad $A[k..k+2^{s-1}-1]$ и $A[k+2^{s-1}..k+2^s-1]$
\quad\qquad в $2^s$-элементный кусок $A[k..k+2^s-1]$

Опишем тело цикла (строка 3) более подробно. Мы воспроизведим цикл for из процедуры Recursive-FFT, используя вместо \(y^{[0]}\) кусок \(A[k..k+2^{s-1}-1]\), а вместо \(y^{[1]}\) — кусок \(A[k+2^{s-1}..k+2^s-1]\). Значение \(\omega\) (используемое в преобразовании бабочки) зависит от \(s\): оно есть \(\omega_m\), где \(m = 2^s\). Временная переменная и используется в преобразовании бабочки. Таким образом, развёртывая строку 3 в предыдущей процедуре, получаем такую программу:

\textsc{FFT-Base}
1 $n \leftarrow \text{length}[a]$ \qquad $n$ есть степень 2
2 for $s \leftarrow 1$ to $\lg n$
3 \quad do $m \leftarrow 2^s$
4 \qquad $\omega_m \leftarrow e^{2\pi i/m}$
5 \qquad for $k \leftarrow 0$ to $n-1$ by m
6 \qquad\qquad do $\omega \leftarrow 1$
7 \qquad\qquad for $j \leftarrow 0$ to $m/2-1$
8 \qquad\qquad\qquad do $t \leftarrow \omega A[k+j+m/2]$
9 \qquad\qquad\qquad $u \leftarrow A[k+j]$
10 \qquad\qquad\qquad $A[k+j] \leftarrow u + t$
11 \qquad\qquad\qquad $A[k+j+m/2] \leftarrow u - t$
12 \qquad\qquad\qquad $\omega \leftarrow \omega \omega_m$

Наконец, представим окончательную версию итеративной процедуры быстрого преобразования Фурье, в которой два внутренних цикла переставлены (экономия при вычислении \(\omega\)) и использована дополнительная процедура Bit-Reverse-Copy$(a, A)$, копирующая элементы вектора \(a\) в массив \(A\) в нужном нам порядке.

\textsc{Iterative-FFT}$(a)$
1 \textsc{Bit-Reverse-Copy}$(a, A)$
2 $n \leftarrow \text{length}[a]$ \quad $n$ --- степень $2$
3 for $s \leftarrow 1$ to $\lg n$