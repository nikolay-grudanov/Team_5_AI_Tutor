---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.71
tokens: 7525
characters: 2131
timestamp: 2025-12-24T10:51:04.861570
finish_reason: stop
---

которая требует возвращаемый тип Result, представлена фрагментом return Err(e), поэтому тип, возвращаемый из функции, должен иметь тип Result в целях совместимости с этим return.

Давайте посмотрим, что произойдет, если мы применим оператор ? в функции main, которая, как вы помните, возвращает тип ():

    use std::fs::File;

    fn main() {
        let f = File::open("hello.txt")?;
    }

При компиляции этого кода мы получаем следующее сообщение об ошибке¹:

    error[E0277]: the `?` operator can only be used in a function that returns `Result` or `Option` (or another type that implements `std::ops::Try`)
      --> src/main.rs:4:13
      |
    4 |     let f = File::open("hello.txt")?;
      |     ^^^^^^^^^^^^^^^^^^^^^^^^ cannot use the `?` operator in a function that returns `()`
      |
      = help: the trait `std::ops::Try` is not implemented for `()`
      = note: required by `std::ops::Try::from_error`

Эта ошибка указывает на то, что использовать оператор ? разрешено только в той функции, которая возвращает Result<T, E>. Когда вы пишете код в функции, которая не возвращает Result<T, E>, и хотите использовать оператор ? при вызове других функций, возвращающих Result<T, E>, то у вас есть два варианта решения этой проблемы. Одним из них является изменение типа значения, возвращаемого из функции, на Result<T, E>, если у вас нет никаких ограничений, этому препятствующих. Другой заключается в использовании выражения match либо одного из методов Result<T, E> для обработки Result<T, E> любым подходящим способом.

Функция main является особой, и существуют ограничения на то, каким должен быть возвращаемый из нее тип. Для функции main одним из допустимых типов возврата является (), и, что удобно, еще одним допустимым типом возврата является Result<T, E>, как показано ниже:

    use std::error::Error;
    use std::fs::File;

    fn main() -> Result<(), Box<dyn Error>> {
        let f = File::open("hello.txt")?;
        Ok(())
    }

¹ ошибка[E0277]: оператор `?` используется только в той функции, которая возвращает `Result` либо `Option` (либо какой-то другой тип, который реализует `std::ops::Try`)