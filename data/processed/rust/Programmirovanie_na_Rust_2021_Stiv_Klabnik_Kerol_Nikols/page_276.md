---
source_image: page_276.png
page_number: 276
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.73
tokens: 7487
characters: 1986
timestamp: 2025-12-24T10:52:55.994767
finish_reason: stop
---

setup, то сможем добавить в setup код, который хотим вызывать из нескольких тестовых функций в нескольких тестовых файлах:

tests/common.rs
    pub fn setup() {
        // код функции setup, характерный для тестов вашей библиотеки,
        // будет находиться здесь
    }

Снова выполнив тесты, мы увидим новый раздел в данных теста для файла common.rs, хотя этот файл не содержит никаких тестовых функций и мы не вызывали функцию setup:

    running 1 test
    test tests::internal ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
        Running target/debug/deps/common-b8b07b6f1be2db70

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
        Running target/debug/deps/integration_test-d993c68b431d39df

    running 1 test
    test it_adds_two ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
        Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Появление common в результатах тестирования с сообщением running 0 tests — это не совсем то, чего мы хотели. Мы просто хотели поделиться кодом с другими файлами интеграционных тестов.

Чтобы избежать common в данных теста, вместо tests/common.rs мы создадим tests/common/mod.rs. Это альтернативное соглашение об именовании, которое язык Rust также понимает. Такое имя файла говорит компилятору не рассматривать модуль common как файл интеграционного теста. Когда мы переместим код функции setup в файл tests/common/mod.rs и удалим файл tests/common.rs, раздел в данных теста больше не будет появляться. Файлы в подкаталогах каталога tests не компилируются как отдельные упаковки и не имеют разделов в данных теста.

После того как мы создали файл tests/common/mod.rs, можно использовать его из любого файла интеграционного теста в качестве модуля. Вот пример вызова функции setup из теста it_adds_two в файле tests/integration_test.rs: