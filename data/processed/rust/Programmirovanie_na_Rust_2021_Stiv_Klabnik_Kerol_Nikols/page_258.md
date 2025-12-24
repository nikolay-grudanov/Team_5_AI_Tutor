---
source_image: page_258.png
page_number: 258
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.13
tokens: 7362
characters: 1418
timestamp: 2025-12-24T10:52:23.259145
finish_reason: stop
---

облегчает понимание того, почему тест завершился провалом. С другой стороны, макрокоманда assert! указывает только на то, что она получила значение false для выражения ==, а не значения, которые приводят к false.

В листинге 11.7 мы пишем функцию add_two, которая прибавляет 2 к своему параметру и возвращает результат. Затем мы тестируем эту функцию с помощью макрокоманды assert_eq!.

Листинг 11.7. Тестирование функции add_two с помощью макрокоманды assert_eq!

src/lib.rs

pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}

Давайте проверим, успешен ли он!

    running 1 test
    test tests::it_adds_two ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Первый аргумент, который мы передали макрокоманде assert_eq!, 4, равен результату вызова add_two(2). К этому тесту относится строка test tests::it_adds_two ... ok, и текст ok указывает на то, что тест успешный!

Давайте внесем в код ошибку и посмотрим, как выглядит результат, когда тест, который использует макрокоманду assert_eq!, не срабатывает. Измените реализацию функции add_two так, чтобы теперь она прибавляла 3:

pub fn add_two(a: i32) -> i32 {
    a + 3
}

Снова выполните тесты:

    running 1 test
    test tests::it_adds_two ... FAILED

    failures:

    ---- tests::it_adds_two stdout ----