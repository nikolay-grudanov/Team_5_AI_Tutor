---
source_image: page_211.png
page_number: 211
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.38
tokens: 7358
characters: 1033
timestamp: 2025-12-24T09:25:17.837144
finish_reason: stop
---

001 @function PI() { @return 3.14159265359; }

Написание функций в SASS/SCSS очень похоже на написание функций на JavaScript или аналогичных языках программирования.

001 @function pow($number, $exp) {
002   $value: 1;
003   @if $exp > 0 {
004     @for $i from 1 through $exp {
005       $value: $value * $number;
006     }
007   }
008   @else if $exp < 0 {
009     @for $i from 1 through -$exp {
010       $value: $value / $number;
011     }
012   }
013   @return $value;
014 }

001 @function rad($angle) {
002   $unit: unit($angle);
003   $unitless: Wangle / ($angle *0+1);
004   // Если угол в градусах, то необходимо перевести в радианы
005   @if $unit == deg {
006     $unitless: $unitless / 180 * PI();
007   }
008   @return $unitless;
009 }

001 @function sin($angle) {
002   $sin: 0;
003   $angle: rad($angle);
004   // Повторить 10 раз
005   @for $i from 0 through 10 {
006     $fact = fact(2 * $i + 1);
007     $pow = pow($angle, (2 * $i + 1)) / $fact;
008     $sin: $sin + pow(-1, $i) * ;
009   }
010   @return $sin;
011 }