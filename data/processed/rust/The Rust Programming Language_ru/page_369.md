---
source_image: page_369.png
page_number: 369
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.34
tokens: 11660
characters: 1634
timestamp: 2025-12-24T10:34:12.607850
finish_reason: stop
---

будем использовать функциональность итератора вместо кода, который проверяет длину среза и обращается по индексу к определённым значениям. Это позволит лучше понять, что делает функция Config::build, поскольку итератор будет обращаться к значениям.

Как только Config::build получит в своё распоряжение итератор и перестанет использовать операции индексирования с заимствованием, мы сможем переместить значения String из итератора в Config вместо того, чтобы вызывать clone и создавать новое выделение памяти.

Использование возвращённого итератора напрямую

Откройте файл src/main.rs проекта ввода-вывода, который должен выглядеть следующим образом:

Файл: src/main.rs

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });
    // --snip--
}
```

Сначала мы изменим начало функции main, которая была в листинге 12-24, на код в листинге 13-18, который теперь использует итератор. Это не будет компилироваться, пока мы не обновим Config::build.

Файл: src/main.rs

```rust
fn main() {
    let config = Config::build(env::args()).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });
    // --snip--
}
```

Листинг 13-18: Передача возвращаемого значения из env::args в Config::build

Функция env::args возвращает итератор! Вместо того чтобы собирать значения итератора в вектор и затем передавать срез в Config::build, теперь мы передаём владение итератором, возвращённым из env::args в Config::build напрямую.