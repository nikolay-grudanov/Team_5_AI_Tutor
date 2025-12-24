---
source_image: page_555.png
page_number: 555
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.36
tokens: 11712
characters: 1673
timestamp: 2025-12-24T10:41:47.555096
finish_reason: stop
---

Листинг 19-16: Два типажа определены с методом fly и реализованы у типа Human, а также метод fly реализован непосредственно у Human

Когда мы вызываем fly у экземпляра Human, то компилятор по умолчанию вызывает метод, который непосредственно реализован для типа, как показано в листинге 19-17.

Файл: src/main.rs

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Листинг 19-17: Вызов fly у экземпляра Human

Запуск этого кода напечатает *waving arms furiously*, показывая, что Rust называется метод fly реализованный непосредственно у Human.

Чтобы вызвать методы fly у типажа Pilot или типажа Wizard нужно использовать более явный синтаксис, указывая какой метод fly мы имеем в виду. Листинг 19-18 демонстрирует такой синтаксис.

Файл: src/main.rs

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

Листинг 19-18: Указание какой метода fly мы хотим вызвать

Указание имени типажа перед именем метода проясняет компилятору Rust, какую именно реализацию fly мы хотим вызвать. Мы могли бы также написать Human::fly(&person), что эквивалентно используемому нами person.fly() в листинге 19-18, но это писание немного длиннее, когда нужна неоднозначность.

Выполнение этого кода выводит следующее:

```
$ cargo run
Compiling traits-example v0.1.0 (file:///projects/traits-example)
Finished dev [unoptimized + debuginfo] target(s) in 0.46s
    Running `target/debug/traits-example`
This is your captain speaking.
Up!
*waving arms furiously*
```

Поскольку метод fly принимает параметр self, если у нас было два типа оба реализующих один типаж, то Rust может понять, какую реализацию типажа