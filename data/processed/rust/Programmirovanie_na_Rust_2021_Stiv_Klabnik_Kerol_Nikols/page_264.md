---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.86
tokens: 7475
characters: 1878
timestamp: 2025-12-24T10:52:43.274487
finish_reason: stop
---

}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic(expected = "Значение догадки должно быть меньше или равно 100")]
    fn greater_than_100() {
        Guess::new(200);
    }
}

Этот тест сработает, потому что значение, которое мы помещаем в параметр expected атрибута should_panic, является подстрокой сообщения, с которым паникует функция Guess::new. Мы могли бы указать все ожидаемое нами сообщение о панике целиком, которое в этом случае было бы Значение догадки должно быть меньше или равно 100, получено 200. То, что вы решите указать в параметре expected для should_panic, зависит от того, какая часть сообщения о панике является уникальной или динамической и насколько точным должен быть тест. В данном случае будет достаточно подстроки сообщения о панике, чтобы убедиться в том, что код в тестовой функции исполняет случай else if value > 100.

Для того чтобы увидеть, что происходит, когда тест should_panic с ожидаемым сообщением expected не срабатывает, давайте снова введем в код ошибку, поменяв местами тела блоков if value < 1 и else if value > 100:

if value < 1 {
    panic!("Значение догадки должно быть меньше или равно 100, получено {}.", value);
} else if value > 100 {
    panic!("Значение догадки должно быть больше или равно 1, получено {}.", value);
}

На этот раз, когда мы выполняем тест should_panic, он не сработает:

running 1 test
test tests::greater_than_100 ... FAILED

failures:
---- tests::greater_than_100 stdout ----
    thread 'tests::greater_than_100' panicked at 'Значение догадки должно быть больше или равно 1, получено 200.', src/lib.rs:11:12
note: Run with `RUST_BACKTRACE=1` for a backtrace.
note: Panic did not include expected string 'Значение догадки должно быть меньше или равно 100.'

failures:
    tests::greater_than_100

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out