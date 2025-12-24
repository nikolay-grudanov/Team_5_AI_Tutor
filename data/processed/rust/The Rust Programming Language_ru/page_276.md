---
source_image: page_276.png
page_number: 276
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 63.69
tokens: 11795
characters: 2070
timestamp: 2025-12-24T10:30:23.754484
finish_reason: stop
---

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.72s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 2 tests
test tests::another ... FAILED
test tests::exploration ... ok

failures:

---- tests::another stdout ----
thread 'main' panicked at 'Make this test fail', src/lib.rs:10:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

failures:
    tests::another

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

error: test failed, to rerun pass '--lib'

Листинг 11-4. Результаты теста, когда один тест пройден, а другой нет

Вместо ok, строка test tests::another сообщает FAILED. У нас есть два новых раздела между результатами и итогами. Первый раздел показывает детальную причину ошибки каждого теста. В данном случае тест another не сработал, потому что panicked at 'Make this test fail', произошло в строке 10 файла src/lib.rs. В следующем разделе перечисляют имена всех не пройденных тестов, что удобно, когда тестов очень много и есть много деталей про аварийное завершение. Мы можем использовать имя не пройденного теста для его дальнейшей отладки; мы больше поговорим о способах запуска тестов в разделе "Контролирование хода выполнения тестов".

Итоговая строка отображается в конце: общий результат нашего тестирования FAILED. У нас один тест пройден и один тест завершён аварийно.

Теперь, когда вы увидели, как выглядят результаты теста при разных сценариях, давайте рассмотрим другие макросы полезные в тестах, кроме panic!.

Проверка результатов с помощью макроса assert!

Макрос assert! доступен из стандартной библиотеки и является удобным, когда вы хотите проверить что некоторое условие в тесте вычисляется в значение true. Внутри макроса assert! переданный аргумент вычисляется в логическое значение. Если оно true, то assert! в тесте ничего не делает и он считается пройденным. Если же значение вычисляется в false, то макрос assert! вызывает макрос panic!, что делает тест