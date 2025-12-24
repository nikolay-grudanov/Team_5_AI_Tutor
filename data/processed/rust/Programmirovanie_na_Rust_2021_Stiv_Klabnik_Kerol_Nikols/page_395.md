---
source_image: page_395.png
page_number: 395
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.86
tokens: 7482
characters: 1868
timestamp: 2025-12-24T10:56:08.375134
finish_reason: stop
---

Листинг 15.25. Определение cons-списка, содержащее умный указатель RefCell<T>, чтобы модифицировать то, на что ссылается вариант Cons

src/main.rs

use std::rc::Rc;
use std::cell::RefCell;
use crate::List::{Cons, Nil};

#[derive(Debug)]
enum List {
    Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
    fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}

Мы используем еще одну вариацию определения перечисления List из листинга 15.5. Второй элемент в варианте Cons теперь равен умному указателю RefCell<Rc<List>> ①, то есть вместо способности изменять значение типа i32, как мы делали в листинге 15.24, мы хотим модифицировать некое значение типа List, на которое указывает вариант Cons. Мы также добавляем метод tail ②, чтобы сделать удобным доступ ко второму элементу, если у нас есть вариант Cons.

В листинге 15.26 мы добавляем функцию main, которая использует определения из листинга 15.25. Этот код создает список в переменной a и список в переменной b, которая указывает на список в a. Затем он модифицирует список в a, указывая на b и создавая цикл в переходах по ссылкам. В коде есть инструкции println!, которые показывают количества ссылок в различных точках этого процесса.

Листинг 15.26. Создание цикла в переходах по ссылкам из двух значений типа List, которые указывают друг на друга

src/main.rs

fn main() {
    let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a начальное число rc = {}", Rc::strong_count(&a));
    println!("a следующий элемент = {:?}", a.tail());

    let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!("a число rc после создания b = {}", Rc::strong_count(&a));
    println!("b начальное число rc = {}", Rc::strong_count(&b));
    println!("b следующий элемент = {:?}", b.tail());
}