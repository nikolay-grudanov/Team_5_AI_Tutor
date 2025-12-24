---
source_image: page_359.png
page_number: 359
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.43
tokens: 7484
characters: 1716
timestamp: 2025-12-24T10:55:13.950392
finish_reason: stop
---

fn it_works() {
    assert_eq!(3, add_one(2));
}
}

Теперь выполните команду cargo test в верхнеуровневом каталоге add:

$ cargo test
    Compiling add-one v0.1.0 (file:///projects/add/add-one)
    Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.27 secs
    Running target/debug/deps/add_one-f0253159197f7841

running 1 test
test tests::it_works ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

    Running target/debug/deps/adder-f88af9d2cc175a5e

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Doc-tests add-one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Первая часть данных показывает, что тест it_works в упаковке add-one пройден. Следующая часть говорит о том, что в упаковке adder было найдено ноль тестов, и затем последняя часть показывает, что в упаковке add-one было найдено ноль документационных тестов. Команда cargo test в рабочем пространстве, структурированная подобным образом, будет выполнять тесты для всех упаковок в рабочем пространстве.

Мы также можем выполнить тесты для одной конкретной упаковки в рабочем пространстве из верхнеуровневого каталога, применив флаг -p и указав имя упаковки, которую мы хотим протестировать:

$ cargo test -p add-one
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
    Running target/debug/deps/add_one-b3235fea9a156f74

running 1 test
test tests::it_works ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Doc-tests add-one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out