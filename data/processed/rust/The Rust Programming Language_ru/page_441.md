---
source_image: page_441.png
page_number: 441
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.20
tokens: 11542
characters: 1147
timestamp: 2025-12-24T10:36:41.120699
finish_reason: stop
---

указатель `RefMut<T>`, и мы используя оператор разыменования, изменяем внутреннее значение.

Когда мы печатаем `a`, `b` и `c` то видим, что все они имеют изменённое значение равное 15, а не 5:

```sh
$ cargo run
Compiling cons-list v0.1.0 (file:///projects/cons-list)
Finished dev [unoptimized + debuginfo] target(s) in 0.63s
    Running `target/debug/cons-list`
a after = Cons(RefCell { value: 15 }, Nil)
b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))
```

Эта техника довольно изящна! Используя `RefCell<T>`, мы получаем внешне неизменяемое значение `List`. Но мы можем использовать методы `RefCell<T>`, которые предоставляют доступ к его внутренностям, чтобы мы могли изменять наши данные, когда это необходимо. Проверка правил заимствования во время выполнения защищает нас от гонок данных, и иногда стоит немного пожертвовать производительностью ради такой гибкости наших структур данных. Обратите внимание, что `RefCell<T>` не работает для многопоточного кода! `Mutex<T>` - это thread-safe версия `RefCell<T>`, а `Mutex<T>` мы обсудим в главе 16.