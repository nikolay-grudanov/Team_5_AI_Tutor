---
source_image: page_448.png
page_number: 448
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.00
tokens: 11653
characters: 1645
timestamp: 2025-12-24T10:37:07.415993
finish_reason: stop
---

use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}

Узел сможет ссылаться на свой родительский узел, но не владеет своим родителем. В листинге 15-28 мы обновляем main на использование нового определения так, чтобы у узла leaf был бы способ ссылаться на его родительский узел branch:

Файл : src/main.rs

fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![])
    });

    println!("leaf parent = {:?}", leaf.parent.borrow().upgrade());

    let branch = Rc::new(Node {
        value: 5,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)])
    });

    *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

    println!("leaf parent = {:?}", leaf.parent.borrow().upgrade());
}

Листинг 15-28: Узел leaf со слабой ссылкой на его родительский узел branch

Создание узла leaf выглядит аналогично примеру из Листинга 15-27, за исключением поля parent: leaf изначально не имеет родителя, поэтому мы создаём новый, пустой экземпляр ссылки Weak<Node>.

На этом этапе, когда мы пытаемся получить ссылку на родительский узел у узла leaf с помощью метода upgrade, мы получаем значение None. Мы видим это в выводе первого println! выражения:

leaf parent = None

Когда мы создаём узел branch у него также будет новая ссылка типа Weak<Node> в поле parent, потому что узел branch не имеет своего родительского узла. У нас все ещё есть leaf как один из потомков узла branch. Когда мы получили экземпляр Node в