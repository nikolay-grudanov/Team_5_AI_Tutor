---
source_image: page_254.png
page_number: 254
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.44
tokens: 7464
characters: 1846
timestamp: 2025-12-24T10:52:20.258811
finish_reason: stop
---

Листинг 11.3. Добавление второго теста, который провалится, потому что мы вызываем макрокоманду panic!

src/lib.rs

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }
    #[test]
    fn another() {
        panic!("Сделать этот тест неуспешным");
    }
}
```

Снова выполните тесты с помощью cargo test. Данные должны выглядеть, как в листинге 11.4, они показывают, что тест exploration оказался успешным, а тест another — нет.

Листинг 11.4. Результаты тестирования: один тест успешно, другой — нет

```
running 2 tests
test tests::exploration ... ok
1) test tests::another ... FAILED

2 failures:

---- tests::another stdout ----
    thread 'tests::another' panicked at 'Сделать этот тест неуспешным',
        src/lib.rs:10:8
note: Run with `RUST_BACKTRACE=1` for a backtrace.

3 failures:
    tests::another

4) test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out

error: test failed
```

Вместо ok строчка test tests::another показывает FAILED 1. Между отдельными результатами и сводкой появляются два новых раздела: первый раздел 2 показывает подробную причину провала каждого теста. В данном случае another не сработал, потому что он поднял панику в точке 'Сделать этот тест неуспешным', что произошло в строке 10 кода в файле src/lib.rs. В следующем разделе 3 перечислены только названия всех неуспешных тестов, что полезно, когда тестов много и много подробных данных неуспешных тестов. Мы можем использовать название неуспешного теста, чтобы выполнить только этот тест и с легкостью отладить его. Подробнее о способах выполнения тестов мы поговорим в разделе «Контроль выполнения тестов».

Итоговая строчка выводится в конце 4: в целом результат теста был неуспешным, FAILED. У нас был один тест, который завершился успешно, и один тест, который не сработал.