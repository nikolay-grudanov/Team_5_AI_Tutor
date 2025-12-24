---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.57
tokens: 11602
characters: 1470
timestamp: 2025-12-24T10:25:41.032785
finish_reason: stop
---

Листинг 7-12. Объявление use действительно только для той области, в которой оно находится.

Ошибка компилятора показывает, что данный псевдоним не может использоваться в модуле customer:

$ cargo build
Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
 --> src/lib.rs:11:9
  |
11 |     hosting::add_to_waitlist();
  |     ^^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

= note: #[warn(unused_imports)] on by default

For more information about this error, try `rustc --explain E0433`.
warning: `restaurant` (lib) generated 1 warning
error: could not compile `restaurant` due to previous error; 1 warning emitted

Обратите внимание, что есть также предупреждение о том, что use не используется в своей области! Чтобы решить эту проблему, можно переместить use в модуль customer, или же можно сослаться на псевдоним в родительском модуле с помощью super::hosting в дочернем модуле customer.

Создание идиоматических путей с use

В листинге 7-11 вы могли бы задаться вопросом, почему мы указали use crate::front_of_house::hosting, а затем вызвали hosting::add_to_waitlist внутри eat_at_restaurant вместо указания в use полного пути прямо до функции add_to_waitlist для получения того же результата, что в листинге 7-13.