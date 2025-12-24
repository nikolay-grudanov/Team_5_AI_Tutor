---
source_image: page_272.png
page_number: 272
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 67.58
tokens: 7086
characters: 3002
timestamp: 2025-12-24T10:08:48.711730
finish_reason: stop
---

1 (function(){var g=void 0,h=!0,i=null,j=!1,ba=encodeURIComponent;
2 function ya(a){var b=1,c=0,d;if(!C(a)){b=0;for(d=a[u]-1;0<=d;d-
3 var Ba=function(a,b,c,d){a.addEventListener?a.addEventListener
4 Ea[v].contains=function(a){return this.get(a)!==g};function Fa
5 function Ha(a,b){function c(b,c){a.contains(b)||a.set(b,[]);a.
6 var Pa=K(),Qa=K(),Ra=K(),Sa=K(),Ta=K(),L=K(),M=K(),Ua=K(),Va=K
7 Zb=K(h),$b=K(h),ac=K(h),bc=K(h),cc=K(h),dc=Oa("campaignParams"
8 nb,63,g,1);U("_setLocalRemoteServerMode",nb,47,g,2);U("_setSam
9 Wa,29,1);U("_setReferrerOverride",xb,49);U("_setSiteSpeedSampl
10 21);a("_addItem",S[v].O,19);a("_setTransactionDelim",S[v].la,8:
11 14);a("_clearOrganic",S[v].T,70);a("_cookiePathCopy",S[v].W,30
12 Aa,81);a("_setHrefExamineLimit",Aa,80)},R=function(a,b,c,d){a[l
13 function(c,d,e){Na[c]&&this[ia]();e?b[c]=d:a[c]=d;Na[c]&&this.
14 var Ec=function(a){var b=this;this.l=0;var c=a.get(fc);this.Da:
15 var Kc=function(a,b,c){c=c?""":a.c(L,"1");b=b[w](".");if(6!==b[
16 a.b(Rb,0))[z](".")},Nc=function(a,b,c){var c=c?""":a.c(L,"1"),d:
17 0<b[u]&&a.set(Hb,F(b[0]));if(1>=b[u])return h;b=b[1][w]{-1==b[
18 b(Xb,"utmccn");b(ac,"utmcmd");b(bc,"utmctr");b(cc,"utmccct");re
19 a.set(b,c))}-1==b[p]("=")&&(b=F(b));var e="2"==c("utmcvr");d(Wl
20 a=a+="="+b+"; path="+c+"; ";e&&(a+="expires="+new Date((new Da
21 a.language+b.platform+b.userAgent+a.javaEnabled+a.I+a.H+{H.cool
22 else{d=d+"."+d;try{c=new ActiveXObject(d+".7"),e=c.GetVariable
23 jd[ka](Jb),tc=J[sc],rc+=g!=tc?tc:sc;f+=rc;c[m](f)}b+=o+c[z](s).
24 c,d){if(!hd(d))return j;a(b,"v",c,d[t]());return h};e.getKey=f
25 Pc(a,Ic(b,W("__utmv")));nd=!c;return h},pd=function(a){nd||0<w
26 !C(a.get(Wb))||!C(a.get($b))||!C(a.get(Yb))||!C(a.get(Zb)),c={.
27 Fa(d[na]),k=0;k<e[u];++k)if(-1<f[p](e[k])){d=j;break b}zd(a,g,
28 "-",f=Da(b.get(a.get(fb))))||"-",k=Da(b.get("dclid"))||"-",o=c{
29 f,d=a.get(qb),c=F(c)[A](),k=0;k<d[u];++k)if(c==d[k]){c=h;break
30 f=a.get(f)||"-";if(c(k)!=c(f))return h}return j},Cd=RegExp(/^h
31 c=[J,N];break a}J=J[n](/\+/g,"%20");N=N[n](/\+/g,"%20");if(c==:
32 e=b[p]("#");if(c)return 0>e?b+="#"+d:b+"&"+d;c="";f=b[p]("?");0-
33 a.get(sb),d=0;d<e[u];d++)if(c[d].id_==b)return c[d];return i};

Рис. 7.27. Минифицированный код в инструментах разработчика Chrome

Как видите, с точки зрения читабельности код просто ужасен! Невозможно установить точку останова, и если код где-то остановится, невозможно сказать, где именно. Однако, как уже было ранее отмечено, у WebKit-браузеров есть кнопка «деминификации» кода. При отладке в браузере Chrome нажатие кнопки {} делает его читаемым, что и продемонстрировано на рис. 7.28.

Посмотрев на этот код, мы можем сделать вывод, что теперь он читаем и мы можем установить точки останова в любой строке.

Карты кода

Обратившись к коду, показанному на рис. 7.28, отметим, что он обрабатывался/оптимизировался (в английском языке для этого используется слово obfuscated), но означает это то, что в ходе оптимизации длинные, но понятные имена переменных, функций и проч.,