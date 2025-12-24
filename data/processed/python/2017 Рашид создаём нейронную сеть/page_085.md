---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.45
tokens: 6302
characters: 397
timestamp: 2025-12-24T02:11:19.346720
finish_reason: stop
---

Все, что нам остается, — это применить сигмоиду, и сделать это не составляет труда.

\[
O_{выходной} = \text{сигмоида} \left( \begin{array}{c}
0,975 \\
0,888 \\
1,254
\end{array} \right)
\]

\[
O_{выходной} = \left( \begin{array}{c}
0,726 \\
0,708 \\
0,778
\end{array} \right)
\]

Есть! Мы получили сигналы на выходе нейронной сети. Опять-таки, отобразим текущую ситуацию на обновленной диаграмме.