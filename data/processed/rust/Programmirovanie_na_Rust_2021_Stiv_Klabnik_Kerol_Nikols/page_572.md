---
source_image: page_572.png
page_number: 572
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.82
tokens: 7190
characters: 918
timestamp: 2025-12-24T11:00:39.287035
finish_reason: stop
---

Ключевые слова, зарезервированные для использования в будущем

Следующие ключевые слова не имеют никакой функциональности, но зарезервированы в языке Rust для потенциального использования в будущем.

○ abstract
○ async
○ become
○ box
○ do
○ final
○ macro
○ override
○ priv
○ try
○ typeof
○ unsized
○ virtual
○ yield

Сырые идентификаторы

Сырые идентификаторы представляют собой синтаксис, который позволяет использовать ключевые слова там, где они обычно не разрешены. Сырой идентификатор применяется путем добавления к ключевому слову префикса r#.

Например, match — это ключевое слово. Если вы попытаетесь скомпилировать следующую функцию, которая использует match в качестве своего имени:

src/main.rs
    fn match(needle: &str, haystack: &str) -> bool {
        haystack.contains(needle)
    }

то получите такую ошибку:

    error: expected identifier, found keyword `match`
        --> src/main.rs:4:4
        |