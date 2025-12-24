---
source_image: page_303.png
page_number: 303
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.17
tokens: 7258
characters: 1299
timestamp: 2025-12-24T10:53:36.740723
finish_reason: stop
---

Написание провального теста для функции search, нечувствительной к регистру

Мы хотим добавить новую функцию search_case_insensitive («нечувствительный к регистру поиск»), которую будем вызывать, когда переменная среды активирована. Мы продолжим следовать методике разработки на основе тестов, поэтому первым шагом снова будет написание провального теста. Мы добавим новый тест для новой функции search_case_insensitive и переименуем старый тест из one_result в case_sensitive, чтобы прояснить различия между этими тестами, как показано в листинге 12.20.

Листинг 12.20. Добавление нового провального теста для нечувствительной к регистру функции, которую мы намереваемся добавить

src/lib.rs

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\

Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\

Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```