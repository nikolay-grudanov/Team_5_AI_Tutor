---
source_image: page_212.png
page_number: 212
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.52
tokens: 7399
characters: 1215
timestamp: 2025-12-24T09:25:18.773988
finish_reason: stop
---

001 @function cos($angle) {
002   $COS: 0;
003   $angle: rad($angle);
004   // Повторить несколько раз
005   @for $i from 0 through 10 {
006     $pow = pow($angle, 2 * $i) ;
007     $cos: $cos + pow(-1, $i) * $pow / fact (2 * $i) ;
008   }
009   @return $cos;
010 }

Наконец, чтобы вычислить тангенс с помощью функции tan(), функции sin() и cos() обязательны.

001 @function tan($angle) {
002   @return sin($angle) / cos($angle);
003 }

Если вам неинтересно писать собственные математические и тригонометрические функции, то можете просто включить библиотеку compass (см. следующий пример) и использовать sin(), cos() и другие тригонометрические функции из списка.

25.14. Анимация генератора

Возьмем все, что мы узнали из этой главы, и создадим анимацию генератора синусоидальных колебаний:

001 @import "compass/css3";
002
003 .atom {
004   text-align: center;
005   border-radius: 20px;
006   height: 40px;
007   width: 40px;
008   margin: 1px;
009   display: inline-block;
010   border: 10px #1893E7 solid;
011   /* Применение анимации генератора (определена ниже) */
012   animation: oscillate 3s ease-in-out infinite;
013   /* Создание 15 классов для каждого из 15 блоков */
014   @for $i from 1 through 15 {