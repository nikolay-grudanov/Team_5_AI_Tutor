---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 65.06
tokens: 11788
characters: 1903
timestamp: 2025-12-24T10:30:13.930034
finish_reason: stop
---

# [cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}

Листинг 11-1: Тестовый модуль и функция, сгенерированные автоматически с помощью cargo new

Сейчас проигнорируем первые две строчки кода и сосредоточимся на функции, чтобы увидеть как она работает. Обратите внимание на синтаксис аннотации #[test] перед ключевым словом fn. Этот атрибут сообщает компилятору, что это является заголовком тестирующей функции, так что функционал запускающий тесты на выполнение теперь знает, что это тестирующая функция. Также в составе модуля тестов tests могут быть вспомогательные функции, помогающие настроить и выполнить общие подготовительные операции, поэтому специальная аннотация важна для указания объявления функций тестами с использованием атрибута #[test].

Тело функции использует макрос assert_eq!, чтобы утверждать, что 2 + 2 равно 4. Это утверждение служит примером формата для типичного теста. Давайте запустим, чтобы увидеть, что этот тест проходит.

Команда cargo test выполнит все тесты в выбранном проекте и сообщит о результатах как в листинге 11-2:

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.57s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test tests::it_works ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Листинг 11-2: Вывод информации о работе автоматически сгенерированных тестов

Cargo скомпилировал и выполнил тест. После строк Compiling, Finished и Running мы видим строку running 1 test. Следующая строка показывает имя созданной тест функции с названием it_works и результат её выполнения - ok. Далее вы видите