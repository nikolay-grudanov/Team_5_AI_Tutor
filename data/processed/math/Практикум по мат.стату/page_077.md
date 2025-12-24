---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.54
tokens: 5696
characters: 1596
timestamp: 2025-12-24T07:39:42.869845
finish_reason: stop
---

7. Примеры

Q4=sum(cols(Q3)); message("Q4=",Q4);
Q=[Q4;Q2]; message("Q=",Q);
n2Q=Q.c(6)^2/Q.c(5);
Q=[Q,n2Q];
Xi2=sum(n2); message("Xi2=sum((n–Np)^2/(Np))="+Xi2);
SumQ=sum(cols(Q)); message("SumQ=",SumQ);
Xi2Q=SumQ(#SumQ); message("Xi2Q="+Xi2Q+"; Xi2="+Xi2);
Xcr=x2law(n-2).q(1-alp);
message("Xi_cr= x2law("+n–2+").q("+1-alp+")="+Xcr);
Pv=x2law(n-2).pg(Xi2Q); message("Pv="+Pv);
if(Xi2Q<Xcr) message("H0 принимается на уровне значимости"+alp);
else message("H0 отклоняется на уровне значимости"+alp);

H=["j","xi","ni","pi","N*pi","ni-Npi","(ni-Npi)^2/Npi"];
message([H;Q;SumQ]);
savetable([H;round([Q;SumQ],4)],"Пример_7.txt","eng");
line(k,nj,red); line(k,Npj,navy); //полигон частот
axes(); show(); erase();
line(k,sums(nj),red); line(k,sums(Npj),navy); //Функции распределения
axes(); show(); erase();
savetable([k,nj,Npj],"Пример7(k,nj,Npj).txt","eng");

Пример 8. В автобусном парке ежедневно регистрировалось число автобусов, сошедших с линии в течение рабочего дня. Результаты наблюдений над 200 автобусами представлены в таблице.

<table>
  <tr>
    <th>x<sub>i</sub></th>
    <th>0</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>≥ 6</th>
  </tr>
  <tr>
    <th>n<sub>i</sub></th>
    <td>70</td>
    <td>78</td>
    <td>34</td>
    <td>13</td>
    <td>4</td>
    <td>1</td>
    <td>0</td>
  </tr>
</table>

С помощью критерия \( \chi^2 \) проверьте на уровне значимости \( \alpha = 0,05 \) гипотезу \( H_0 \) о том, что случайная величина \( X \), равная числу автобусов, вышедших из строя в течение рабочего дня, распределена по закону Пуассона.