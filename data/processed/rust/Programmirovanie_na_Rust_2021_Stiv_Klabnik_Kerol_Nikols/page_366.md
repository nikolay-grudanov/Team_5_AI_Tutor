---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.21
tokens: 7441
characters: 1612
timestamp: 2025-12-24T10:55:18.992499
finish_reason: stop
---

Листинг 15.2. Первая попытка определить перечисление enum для представления структуры данных cons-списка значений типа i32

src/main.rs
enum List {
    Cons(i32, List),
    Nil,
}

ПРИМЕЧАНИЕ
В этом примере мы реализуем cons-список, который содержит только значения типа i32. Как в главе 10, мы могли бы реализовать его, используя обобщения, чтобы определить тип cons-списка, который мог бы хранить значения любого типа.

Использование типа List для хранения списка 1, 2, 3 будет выглядеть как код из листинга 15.3.

Листинг 15.3. Использование перечисления List для хранения списка 1, 2, 3

src/main.rs
use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}

Первое значение Cons содержит 1 и еще одно значение типа List. Данное значение типа List — это еще одно значение Cons, которое содержит 2 и еще одно значение List. Данное значение типа List — это очередное значение Cons, которое содержит 3 и значение типа List, в конечном итоге равное Nil, то есть нерекурсивному варианту, который сигнализирует о конце списка.

Если мы попытаемся скомпилировать код листинга 15.3, то получим ошибку, показанную в листинге 15.4¹.

Листинг 15.4. Ошибка при попытке определить рекурсивное перечисление

error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |     ---- recursive without indirection
  |
  = help: insert indirection (e.g., a `Box`, `Rc`, or `&`) at some point to make `List` representable

¹ ошибка[E0072]: рекурсивный тип `List` имеет бесконечный размер