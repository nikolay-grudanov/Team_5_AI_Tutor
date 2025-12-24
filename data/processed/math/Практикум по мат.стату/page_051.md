---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.55
tokens: 5425
characters: 1018
timestamp: 2025-12-24T07:39:12.798798
finish_reason: stop
---

7. Примеры

if (T>x1 & T<x2) StrR=Str2+" in "+Str1+" => H0 принимается";
else StrR=Str2+" not in "+Str1+" => H0 отвергается";
message(StrR); // результат проверки гипотезы

// в) Построить функцию мощности критерия
// для значений lamda in [aL; bL]
// и найти мощность для случая, когда H1: lambda=L1
L1=0.15; aL=0.01; bL=0.2; // исходные величины

function power(L)=1-(x2law(2*n).pl(L*x2/L0)-x2law(2*n).pl(L*x1/L0));
w1=power(L1); message("P("+L1+")="+w1);
w0=power(L0); message("P("+L0+")="+w0+"=alp");
L=aL:bL:0.0001; w=power(L);
savetable([L,w],"Power(lambda).txt","eng"); // сохранение результатов
line(L,w,red,2); axes(); show(); erase(); // построение графика

![Графики мощности критерия](https://i.imgur.com/3Q5z5QG.png)

Первый рисунок появляется непосредственно в процессе расчёта, второй построен на основе сохранённых данных специальной программой Grapher.

Пример 2. Имеется монета с вероятностью выпадения орла p.
Проверяется гипотеза \( H_0 : p = 0.5 \), альтернативная гипотеза \( H_1 : p \neq 0.5 \).