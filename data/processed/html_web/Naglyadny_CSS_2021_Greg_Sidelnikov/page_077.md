---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.06
tokens: 7368
characters: 1263
timestamp: 2025-12-24T09:22:34.073934
finish_reason: stop
---

Обратите внимание: свойство overflow: hidden здесь используется для того, чтобы отсечь все находящееся за пределами контейнера.

С помощью псевдоэлементов #nike:before и #nike:after создадим основу логотипа — длинную черную полосу. Скругленные углы используются в данном примере для создания знаменитой кривой Nike:

1 #nike:before {
2   content: " ";
3   position: absolute;
4   top: -250px;
5   left: 190px;
6   width: 150px;
7   height: 550px;
8   background: black;
9   border-top-left-radius: 60px 110px;
10  border-top-right-radius: 130px 220px;
11  transform: rotate(-113deg);
12  z-index: 1;
13 }

Точно так же мы создадим еще одну изогнутую рамку. Белый фон послужит маской для обработки остальной части логотипа. В данном примере угол поворота имеет решающее значение. Именно он формирует узнаваемую кривую логотипа. Для обеспечения правильного наложения элементов мы также использовали свойство z-index со значениями 1, 2 и 3 соответственно.

1 #nike:after {
2   content: " ";
3   position: absolute;
4   top: -235px;
5   left: 220px;
6   width: 120px;
7   height: 500px;
8   background: black;
9   border-top-left-radius: 60px 110px;
10  border-top-right-radius: 130px 220px;
11  background: white;
12  transform: rotate(-104deg);
13  z-index: 2;
14 }