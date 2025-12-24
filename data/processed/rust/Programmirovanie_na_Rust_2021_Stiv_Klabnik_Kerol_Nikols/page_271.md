---
source_image: page_271.png
page_number: 271
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.96
tokens: 7562
characters: 2143
timestamp: 2025-12-24T10:52:57.982648
finish_reason: stop
---

После #[test] мы добавляем строку #[ignore] в тест, который хотим исключить. Теперь, когда мы запускаем тесты, it_works выполняется, а expensive_test — нет:

$ cargo test
    Compiling adder v0.1.0 (file:///projects/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24 secs
    Running target/debug/deps/adder-ce99bcc2479f4607

running 2 tests
test expensive_test ... ignored
test it_works ... ok

test result: ok. 1 passed; 0 failed; 1 ignored; 0 measured; 0 filtered out

Функция expensive_test указана как игнорируемая. Если мы хотим выполнять только игнорируемые тесты, можно применить команду cargo test -- --ignored:

$ cargo test -- --ignored
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
    Running target/debug/deps/adder-ce99bcc2479f4607

running 1 test
test expensive_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 1 filtered out

Контролируя то, какие тесты выполняются, вы можете сделать так, чтобы результаты команды cargo test были быстрыми. Когда вы находитесь в точке, где имеет смысл проверить результаты проигнорированных тестов и у вас есть время на то, чтобы дождаться результатов, то вместо этого вы можете выполнить команду cargo test -- --ignored.

Организация тестов

Как уже упоминалось в начале главы, тестирование представляет собой сложную дисциплину и разные люди используют разную терминологию и организацию. Сообщество Rust рассматривает тесты с точки зрения двух главных категорий: модульных тестов и интеграционных тестов. Модульные тесты малы и более сфокусированы на проверке одного модуля в отдельности, они могут тестировать приватные интерфейсы. Интеграционные тесты полностью внешние по отношению к библиотеке и используют ваш код так же, как и любой другой внешний код, применяя только публичный интерфейс и потенциально проверяя несколько модулей в одном тесте.

Важно писать оба вида теста, чтобы разделы библиотеки делали то, что вы хотите, вместе и по отдельности.

Модульные тесты

Назначение модульных тестов (юнит-тестов) — проверять каждую единицу кода отдельно от остальной части кода, чтобы оперативно находить места, где код рабо-