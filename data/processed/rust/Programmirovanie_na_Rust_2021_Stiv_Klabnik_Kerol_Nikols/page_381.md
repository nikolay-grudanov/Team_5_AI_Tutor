---
source_image: page_381.png
page_number: 381
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.10
tokens: 7441
characters: 1564
timestamp: 2025-12-24T10:55:42.423384
finish_reason: stop
---

списка, которые будут совместно владеть третьим списком. Концептуально это выглядит примерно так же, как на рис. 15.3.

![Два списка — b и c — совместно владеющие третьим списком — a](../images/15_3.png)

Рис. 15.3. Два списка — b и с — совместно владеющие третьим списком — а

Мы создадим список a, который содержит 5, а затем 10. Затем мы составим еще два списка: b, который начинается с 3, и с, который начинается с 4. Затем оба списка, b и с, перейдут к первому списку, a, содержащему 5 и 10. Другими словами, оба списка будут совместно использовать первый список, содержащий 5 и 10.

Попытка реализовать этот сценарий с определением перечисления List и умным указателем Box<T> не сработает, как показано в листинге 15.17.

Листинг 15.17. Нельзя иметь два списка, использующих умный указатель Box<T>, которые пытаются совместно владеть третьим списком

src/main.rs

enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5,
        Box::new(Cons(10,
            Box::new(Nil))));

    let b = Cons(3, Box::new(a));
    let c = Cons(4, Box::new(a));
}

Когда мы компилируем этот код, то получаем ошибку¹:

error[E0382]: use of moved value: `a`
 --> src/main.rs:13:30
  |
12 |     let b = Cons(3, Box::new(a));
  |                        - value moved here
13 |     let c = Cons(4, Box::new(a));
  |                        ^ value used here after move
  |
  = note: move occurs because `a` has type `List`, which does not implement the `Copy` trait

¹ ошибка[E0382]: использование перемещенного значения `a`