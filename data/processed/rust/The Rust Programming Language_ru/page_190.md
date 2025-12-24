---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.30
tokens: 11740
characters: 1994
timestamp: 2025-12-24T10:26:34.307369
finish_reason: stop
---

Эта строка создаёт новую пустую строковую переменную с именем s, в которую мы можем затем загрузить данные. Часто у нас есть некоторые начальные данные, которые мы хотим назначить строке. Для этого мы используем метод to_string доступный для любого типа, который реализует типаж Display, как у строковых литералов. Листинг 8-12 показывает два примера.

```rust
let data = "initial contents";

let s = data.to_string();

// the method also works on a literal directly:
let s = "initial contents".to_string();
```

Листинг 8-12: Использование метода to_string для создания экземпляра типа String из строкового литерала

Эти выражения создают строку с initial contents.

Мы также можем использовать функцию String::from для создания String из строкового литерала. Код листинга 8-13 является эквивалентным коду из листинга 8-12, который использует функцию to_string:

```rust
let s = String::from("initial contents");
```

Листинг 8-13: Использование функции String::from для создания экземпляра типа String из строкового литерала

Поскольку строки используются для очень многих вещей, можно использовать множество API для строк, предоставляющих множество возможностей. Некоторые из них могут показаться избыточными, но все они занимаются своим делом! В данном случае String::from и to_string делают одно и тоже, поэтому выбор зависит от стиля который вам больше импонирует.

Запомните, что строки хранятся в кодировке UTF-8, поэтому можно использовать любые правильно кодированные данные в них, как показано в листинге 8-14:

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שלום");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

Листинг 8-14: Хранение приветствий в строках на разных языках