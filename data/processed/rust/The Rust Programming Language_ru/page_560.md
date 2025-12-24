---
source_image: page_560.png
page_number: 560
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.75
tokens: 11808
characters: 2103
timestamp: 2025-12-24T10:42:07.281523
finish_reason: stop
---

$ cargo run
Compiling traits-example v0.1.0 (file:///projects/traits-example)
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
20 | impl OutlinePrint for Point {}
   | ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
3  | trait OutlinePrint: fmt::Display {
   | ^^^^^^^^^^^^^^^ required by this bound in `OutlinePrint`

For more information about this error, try `rustc --explain E0277`.
error: could not compile `traits-example` due to previous error

Чтобы исправить, мы реализуем Display у структуры Point и выполняем требуемое ограничение OutlinePrint, вот так:

Файл: src/main.rs

use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

Тогда реализация типажа OutlinePrint для структуры Point будет скомпилирована успешно и мы можем вызвать outline_print у экземпляра Point для отображения значения обрамлённое звёздочками.

Шаблон Newtype для реализация внешних типажей у внешних типов

В разделе "Реализация типажа у типа" главы 10, мы упоминали "правило сироты" (orphan rule), которое гласит, что разрешается реализовать типаж у типа, если либо типаж, либо тип являются локальными для нашего крейта. Можно обойти это ограничение, используя шаблон нового типа (newtype pattern), который включает в себя создание нового типа в кортежной структуре. (Мы рассмотрели кортежные структуры в разделе "Использование структур кортежей без именованных полей для создания различных типов" главы 5.) Структура кортежа будет иметь одно поле и будет тонкой оболочкой для типа которому мы хотим реализовать типаж. Тогда тип оболочки является локальным для нашего крейта и мы можем реализовать типаж для локальной обёртки. Newtype это термин, который происходит от языка программирования Haskell. В нем нет ухудшения