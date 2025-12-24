---
source_image: page_353.png
page_number: 353
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 62.96
tokens: 11735
characters: 1760
timestamp: 2025-12-24T10:33:28.433394
finish_reason: stop
---

параметр: неизменное заимствование, мутабельное заимствование и принятие права собственности. Замыкание будет решать, какой из этих способов использовать, основываясь на том, что тело функции делает с полученными значениями.

В листинге 13-4 мы определяем замыкание, которое захватывает неизменяемую ссылку на вектор с именем list, поскольку неизменяемая ссылка нужна только для печати значения:

Файл : src/main.rs

```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
    only_borrows();
    println!("After calling closure: {:?}", list);
}
```

Листинг 13-4: Определение и вызов замыкания, которое захватывает неизменяемую ссылку

Этот пример также иллюстрирует, что переменная может связываться с определением замыкания, и мы можем позже вызвать замыкание, используя имя переменной и круглые скобки, как если бы имя переменной было именем функции.

Поскольку мы можем одновременно иметь несколько неизменяемых ссылок на list, list по-прежнему доступен из кода до определения замыкания, после определения замыкания, но до вызова замыкания, и после вызова замыкания. Этот код компилируется, выполняется и печатается:

```
$ cargo run
Compiling closure-example v0.1.0 (file:///projects/closure-example)
Finished dev [unoptimized + debuginfo] target(s) in 0.43s
    Running `target/debug/closure-example`
Before defining closure: [1, 2, 3]
Before calling closure: [1, 2, 3]
From closure: [1, 2, 3]
After calling closure: [1, 2, 3]
```

Затем в листинге 13.5 мы меняем тело замыкания, чтобы оно добавляло элемент в вектор list. Теперь замыкание фиксирует изменяемую ссылку:

Файл : src/main.rs