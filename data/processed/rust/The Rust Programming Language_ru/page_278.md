---
source_image: page_278.png
page_number: 278
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.64
tokens: 11613
characters: 1444
timestamp: 2025-12-24T10:30:07.734527
finish_reason: stop
---

Также, в модуле tests обратите внимание на новую добавленную строку use super::*; . Модуль tests является обычным и подчиняется тем же правилам видимости, которые мы обсуждали в главе 7 "Пути для ссылки на элементы внутри дерева модуля". Так как этот модуль tests является внутренним, нужно подключить тестируемый код из внешнего модуля в область видимости внутреннего модуля с тестами. Для этого используется глобальное подключение, так что все что определено во внешнем модуле становится доступным внутри tests модуля.

Мы назвали наш тест larger_can_hold_smaller и создали два нужных экземпляра Rectangle. Затем вызвали макрос assert! и передали результат вызова larger.can_hold(&smaller) в него. Это выражение должно возвращать true, поэтому наш тест должен пройти. Давайте выясним!

$ cargo test
Compiling rectangle v0.1.0 (file:///projects/rectangle)
Finished test [unoptimized + debuginfo] target(s) in 0.66s
Running unittests src/lib.rs (target/debug/deps/rectangle-6584c4561e48942e)

running 1 test
test tests::larger_can_hold_smaller ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests rectangle

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Тест проходит. Теперь добавим другой тест, в этот раз мы попытаемся убедиться, что меньший прямоугольник не может содержать больший прямоугольник:

Файл: src/lib.rs