---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.67
tokens: 7392
characters: 1682
timestamp: 2025-12-24T10:47:48.337459
finish_reason: stop
---

в результате вычисления условие примет значение «ложь». Если вы не укажете выражение else и условие окажется ложным, то программа просто пропустит блок if и перейдет к следующему коду.

Попробуйте выполнить код ниже. На выходе вы увидите следующий результат:

$ cargo run
    Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
    Running `target/debug/branches`
    условие было истинным

Давайте изменим значение переменной number на значение, которое делает условие ложным, и посмотрим, что произойдет:

let number = 7;

Выполните программу еще раз и посмотрите на результат:

$ cargo run
    Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
    Running `target/debug/branches`
    условие было ложным

Также стоит отметить, что условие в этом коде должно иметь тип bool. Если условие не имеет типа bool, произойдет ошибка. Например, выполните следующий код:

src/main.rs
fn main() {
    let number = 3;

    if number {
        println!("число было равно трем");
    }
}

На этот раз условие if принимает значение 3, и Rust выдает ошибку:

error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |     ^^^^^ expected bool, found integral variable
  |
  = note: expected type `bool`
         found type `{integer}`

Ошибка указывает на то, что Rust ожидал значение типа bool, но получил значение целочисленного типа. В отличие от таких языков, как Ruby и JavaScript, язык Rust не будет автоматически пытаться конвертировать не-булевы типы в булев тип. Следует выражаться однозначно и всегда предоставлять выражению if