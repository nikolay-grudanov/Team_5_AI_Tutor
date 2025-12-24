---
source_image: page_067.png
page_number: 67
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.44
tokens: 5381
characters: 804
timestamp: 2025-12-24T07:39:24.427779
finish_reason: stop
---

7. Примеры

xv=sort(X); Fv=1–exp(–0.5*xv); Fe1=(1:N)/N; Fe2=(0:N–1)/N;
Dp=max(Fe1–Fv); Dn=max(Fv–Fe2); D=max([Dp,Dn])*N^0.5;
Dcr=crKolm(alp);
Str1="D+="+Dp+", D=""+Dn+", D="+D; Str2="Dcr="+Dcr;
if (D < Dcr) StrR=Str1+"< "+Str2+" => H0 принимается";
else StrR=Str1+"> "+Str2+" => H0 отвергается";
message(StrR); // результат проверки гипотезы
    // Дальше только графики:
fe = X.intfr(0:8:0.04);
fe=[fe.c(1:2),fe.c(3)/N]; // группировка плотности логдоходности
    //структура f_denSum1.txt: [x1,x2,f1; x2,x3,f2; x3,x4,f3; ...]
//savetable(fe,"fe_den.txt","eng");
//wintitle("Эмпирическая плотность X");
dhist(fe, white,0.9);   // гистограмма эмпирической плотности
xx=0:8:0.001; ff=L*exp(-L*xx);
line(xx,ff,red,2); axes(); show(); erase();

![Гистограмма эмпирической плотности X](../images/fig_7_1.png)