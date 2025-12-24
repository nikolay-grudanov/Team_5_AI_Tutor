---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 70.38
tokens: 11814
characters: 2010
timestamp: 2025-12-24T10:30:48.455564
finish_reason: stop
---

чтобы добавлять 3:

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

Попробуем выполнить данный тест ещё раз:

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.61s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test tests::it_adds_two ... FAILED

failures:

---- tests::it_adds_two stdout ----
thread 'main' panicked at 'assertion failed: `(left == right)`
  left: `4`,
  right: `5`, src/lib.rs:11:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

failures:
    tests::it_adds_two

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

error: test failed, to rerun pass '--lib'

Наш тест нашёл ошибку! Тест it_adds_two не выполнился, отображается сообщение assertion failed: (left == right)` и показывает, что left было 4, а right было 5. Это сообщение полезно и помогает начать отладку: это означает left аргумент assert_eq! имел значение 4, но right аргумент для вызова add_two(2) был со значением 5.

Обратите внимание, что в некоторых языках (таких как Java) в библиотеках кода для тестирования принято именовать входные параметры проверочных функций как "ожидаемое" (expected) и "фактическое" (actual). В Rust приняты следующие обозначения left и right соответственно, а порядок в котором определяются ожидаемое значение и производимое тестируемым кодом значение не имеют значения. Мы могли бы написать выражение в тесте как assert_eq!(add_two(2), 4), что приведёт к отображаемому сообщению об ошибке assertion failed: (left == right)``, слева left было бы 5, а справа right было бы 4.

Макрос assert_ne! сработает успешно, если входные параметры не равны друг другу и завершится с ошибкой, если значения равны. Этот макрос наиболее полезен в тех случаях, когда мы не знаем заранее, каким значение будет, но знаем точно, каким оно не может быть. К примеру, если тестируется функция, которая гарантировано изменяет