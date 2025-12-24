---
source_image: page_401.png
page_number: 401
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.17
tokens: 7493
characters: 1917
timestamp: 2025-12-24T10:56:17.443180
finish_reason: stop
---

RefCell<Weak<Node>> в поле parent узла leaf, а затем функцию Rc::downgrade для создания ссылки Weak<Node> на узел branch из умного указателя Rc<Node> в узле branch.

Когда мы снова выведем родителя узла leaf ⑤, то на этот раз получим вариант Some, содержащий узел branch: теперь узел leaf может обратиться к своему родителю! Когда мы печатаем узел leaf, мы также избежаем цикла, который в конечном итоге закончился бы переполнением стека, как это было в листинге 15.26. Ссылки Weak<Node> печатаются как (Weak):

leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak)
}, children: RefCell { value: [] } } ] } })

Отсутствие бесконечного вывода данных показывает, что код не создал цикла в переходах по ссылкам. Это подтверждается и значениями, которые мы получаем из вызовов функции — Rc::strong_count и Rc::weak_count.

Визуализация изменений, вносимых в strong_count и weak_count

Давайте посмотрим, как изменяются значения strong_count и weak_count экземпляров Rc<Node>, создав новую внутреннюю область видимости и переместив узел branch в эту область. Сделав это, мы увидим, что происходит, когда узел branch создается, а затем отбрасывается, выходя из области видимости. Эти изменения показаны в листинге 15.29.

Листинг 15.29. Создание узла branch во внутренней области видимости и проверка числа сильных и слабых ссылок

src/main.rs

fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

    println!(
        "сильные ссылки leaf = {}, слабые ссылки = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

    {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });
    }
}