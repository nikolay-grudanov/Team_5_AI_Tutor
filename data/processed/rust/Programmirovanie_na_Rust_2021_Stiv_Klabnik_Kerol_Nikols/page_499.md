---
source_image: page_499.png
page_number: 499
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.23
tokens: 7276
characters: 1163
timestamp: 2025-12-24T10:58:44.329245
finish_reason: stop
---

Листинг 19.16. Два типажа определяются как имеющие метод fly и реализуются в типе Human, а метод fly реализуется непосредственно в Human

src/main.rs
```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("Говорит ваш капитан.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Подъем!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*яростно размахивает руками*");
    }
}
```

Когда мы вызываем fly для экземпляра типа Human, компилятор по умолчанию вызывает метод, который реализован непосредственно в типе, как показано в листинге 19.17.

Листинг 19.17. Вызов метод fly для экземпляра типа Human

src/main.rs
```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Выполнение этого кода выведет *яростно размахивает руками*, показывая, что компилятор вызвал метод fly, реализованный непосредственно в Human.

Для того чтобы вызвать метод fly либо из Pilot, либо из Wizard, нужно использовать более явный синтаксис, который указывает, какой метод fly мы имеем в виду. Этот синтаксис показан в листинге 19.18.