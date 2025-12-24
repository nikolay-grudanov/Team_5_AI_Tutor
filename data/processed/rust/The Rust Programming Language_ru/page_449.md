---
source_image: page_449.png
page_number: 449
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.48
tokens: 11590
characters: 1440
timestamp: 2025-12-24T10:37:17.392642
finish_reason: stop
---

переменной branch, мы можем изменить переменную leaf чтобы дать ей Weak<Node> ссылку на её родителя. Мы используем метод borrow_mut у типа RefCell<Weak<Node>> поля parent у leaf, а затем используем функцию Rc::downgrade для создания Weak<Node> ссылки на branch из Rc<Node> в branch.

Когда мы снова напечатаем родителя leaf то в этот раз мы получим вариант Some содержащий branch, теперь leaf может получить доступ к своему родителю! Когда мы печатаем leaf, мы также избегаем цикла, который в конечном итоге заканчивался переполнением стека, как в листинге 15-26; ссылки типа Weak<Node> печатаются как (Weak):

leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) }, children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) }, children: RefCell { value: [] } }] } })

Отсутствие бесконечного вывода означает, что этот код не создал ссылочной зациклённости. Мы также можем сказать это, посмотрев на значения, которые мы получаем при вызове Rc::strong_count и Rc::weak_count.

Визуализация изменений в strong_count и weak_count

Давайте посмотрим, как изменяются значения strong_count и weak_count экземпляров типа Rc<Node> с помощью создания новой внутренней области видимости и перемещая создания экземпляра branch в эту область. Таким образом можно увидеть, что происходит, когда branch создаётся и затем удаляется при выходе из области видимости. Изменения показаны в листинге 15-29:

Файл : src/main.rs