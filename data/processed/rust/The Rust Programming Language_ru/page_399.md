---
source_image: page_399.png
page_number: 399
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.11
tokens: 11590
characters: 1261
timestamp: 2025-12-24T10:35:14.098667
finish_reason: stop
---

$ cargo test -p add_one
    Finished test [unoptimized + debuginfo] target(s) in 0.00s
    Running target/debug/deps/add_one-b3235fea9a156f74

running 1 test
test tests::it_works ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Эти выходные данные показывают, что выполнение cargo test запускает только тесты для крейта add-one и не запускает тесты крейта adder.

Если вы соберётесь опубликовать крейты из рабочего пространства на crates.io, каждый крейт будет необходимо будет опубликовать отдельно. Подобно cargo test, мы можем опубликовать конкретный крейт из нашей рабочей области, используя флаг -p и указав имя крейта, который мы хотим опубликовать.

Для дополнительной практики добавьте крейт add_two в данное рабочее пространство аналогичным способом, как делали с крейт add_one!

По мере роста проекта рассмотрите возможность использования рабочих областей: легче понять небольшие, отдельные компоненты, чем один большой кусок кода. Кроме того, хранение крейтов в рабочем пространстве может облегчить координацию между крейтами, если они часто изменяются параллельно.