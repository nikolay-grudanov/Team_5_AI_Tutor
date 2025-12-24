---
source_image: page_443.png
page_number: 443
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.68
tokens: 11767
characters: 2063
timestamp: 2025-12-24T10:37:16.774580
finish_reason: stop
---

В листинге 15-26 мы добавляем main функцию, которая использует определения листинга 15-25. Этот код создаёт список в переменной a и список b, который указывает на список a. Затем он изменяет список внутри a так, чтобы он указывал на b, создавая ссылочное зацикливание. В коде есть инструкции println!, чтобы показать значения счётчиков ссылок в различных точках этого процесса.

Файл : src/main.rs

```rust
fn main() {
    let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

    let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!("a rc count after b creation = {}", Rc::strong_count(&a));
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

    if let Some(link) = a.tail() {
        *link.borrow_mut() = Rc::clone(&b);
    }

    println!("b rc count after changing a = {}", Rc::strong_count(&b));
    println!("a rc count after changing a = {}", Rc::strong_count(&a));

    // Uncomment the next line to see that we have a cycle;
    // it will overflow the stack
    // println!("a next item = {:?}", a.tail());
}
```

Листинг 15-26: Создание ссылочного цикла из двух значений List, указывающих друг на друга

Мы создаём экземпляр Rc<List> содержащий значение List в переменной a с начальным списком 5, Nil. Затем мы создаём экземпляр Rc<List> содержащий другое значение List в переменной b, которое содержит значение 10 и указывает на список в a.

Мы меняем a так, чтобы он указывал на b вместо Nil, создавая зациклённость. Мы делаем это с помощью метода tail, чтобы получить ссылку на RefCell<Rc<List>> из переменной a, которую мы помещаем в переменную link. Затем мы используем метод borrow_mut из типа RefCell<Rc<List>>, чтобы изменить внутреннее значение типа Rc<List>, содержащего начальное значение Nil на значение типа Rc<List> взятое из переменной b.

Когда мы запускаем этот код, оставив последний println! закомментированным в данный момент, мы получим вывод: