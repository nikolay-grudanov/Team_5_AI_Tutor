---
source_image: page_301.png
page_number: 301
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.08
tokens: 7411
characters: 1732
timestamp: 2025-12-24T10:53:40.743724
finish_reason: stop
---

чтобы хранить строки текста в этом векторе. После цикла for мы возвращаем вектор, как показано в листинге 12.19.

Листинг 12.19. Хранение совпадающих строк с целью их последующего возвращения

src/lib.rs
```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results = Vec::new();
    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }
    results
}
```

Теперь функция search должна возвращать только те строки текста, которые содержат query, и тест должен завершиться успешно. Давайте выполним тест:

```bash
$ cargo test
--пропуск--
running 1 test
test tests::one_result ... ok
test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

На данном этапе мы могли бы рассмотреть возможности, чтобы рефакторить реализацию функции search, сохраняя при этом успешное прохождение тестов с целью поддержания той же функциональности. Код в функции search не так уж и плох, но в нем не использованы некоторые полезные свойства итераторов. Мы вернемся к этому примеру в главе 13, где подробно изучим итераторы и рассмотрим, как улучшить данный пример.

Использование функции search в функции run

Теперь, когда проверенная функция search работает, нужно вызвать search из функции run. Требуется передать значение config.query и содержимое contents, которое функция run читает из файла, в функцию search. Затем функция run выводит каждую строку текста, возвращаемую из функции search:

src/lib.rs
```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;
    for line in search(&config.query, &contents) {
        println!("{}", line);
    }
    Ok(())
}
```