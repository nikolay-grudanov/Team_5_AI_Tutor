---
source_image: page_400.png
page_number: 400
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.91
tokens: 7439
characters: 1743
timestamp: 2025-12-24T10:56:08.775556
finish_reason: stop
---

struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}

Узел сможет ссылаться на родительский узел, но не будет владеть своим родителем. В листинге 15.28 мы обновляем функцию main, чтобы теперь она использовала новое определение, благодаря которому узел leaf сможет ссылаться на своего родителя branch.

Листинг 15.28. Узел leaf со слабой ссылкой на родительский узел branch
src/main.rs

fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

    println!("родительский узел leaf = {:?}", leaf.parent.borrow().upgrade());

    let branch = Rc::new(Node {
        value: 5,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

    *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

    println!("родительский узел leaf = {:?}", leaf.parent.borrow().upgrade());
}

Создание узла leaf выглядит так же, как оно выглядело в листинге 15.27, за исключением поля parent: узел leaf начинается без родителя, поэтому мы создаем новый, пустой экземпляр ссылки Weak<Node> ①.

В этом месте, когда мы пытаемся получить ссылку на родителя узла leaf с помощью метода upgrade, мы получаем значение None. Мы видим это в данных первой инструкции println! ②:

leaf parent = None

Когда мы создаем узел branch, у него также есть новая ссылка Weak<Node> в поле parent ③, потому что узел branch не имеет родительского узла. У нас еще есть узел leaf как один из дочерних узлов branch. Как только в узле branch появляется экземпляр структуры Node, мы можем модифицировать узел leaf, чтобы дать ему ссылку Weak<Node> на его родителя ④. Мы используем метод loan_mut для