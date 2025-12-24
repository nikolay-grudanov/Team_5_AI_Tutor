---
source_image: page_331.png
page_number: 331
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.37
tokens: 11642
characters: 1708
timestamp: 2025-12-24T10:32:24.946199
finish_reason: stop
---

ссылаются с помощью срезов тоже должны быть действительно; если компилятор предполагает, что мы делаем строковые срезы переменной query, а не переменной contents, он неправильно выполнит проверку безопасности.

Если мы забудем аннотации времени жизни и попробуем скомпилировать эту функцию, то получим следующую ошибку:

$ cargo build
Compiling minigrep v0.1.0 (file:///projects/minigrep)
error[E0106]: missing lifetime specifier
 --> src/lib.rs:28:51
  |
28 | pub fn search(query: &str, contents: &str) -> Vec<&str> {
  |                ----                ----                ^ expected named lifetime parameter
  = help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
  |
28 | pub fn search<'a>(query: &'a str, contents: &'a str) -> Vec<&'a str> {
  |        ++++        ++        ++        ++
For more information about this error, try `rustc --explain E0106`.
error: could not compile `minigrep` due to previous error

Rust не может понять, какой из двух аргументов нам нужен, поэтому нужно сказать ему об этом. Так как contents является тем аргументом, который содержит весь наш текст, и мы хотим вернуть части этого текста, которые совпали при поиске, мы понимаем, что contents является аргументом, который должен быть связан с возвращаемым значением временем жизни.

Другие языки программирования не требуют от вас связывания в сигнатурае аргументов с возвращаемыми значениями. Хотя сейчас это может показаться странным, со временем станет понятнее. Можете сравнить этот пример с разделом «Валидация ссылок при помощи времён жизни» главы 10.

Запустим тест: