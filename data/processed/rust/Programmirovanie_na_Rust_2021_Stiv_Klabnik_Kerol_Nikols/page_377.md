---
source_image: page_377.png
page_number: 377
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.64
tokens: 7475
characters: 2031
timestamp: 2025-12-24T10:55:36.290313
finish_reason: stop
---

Задайте код, который будет выполняться, когда значение выходит из области видимости, путем реализации типажа Drop. Типаж Drop требует реализации одного метода с именем drop, который принимает изменяемую ссылку на self. Для того чтобы увидеть, когда Rust вызывает метод drop, давайте пока реализуем метод drop с инструкциями println!.

Листинг 15.14 показывает структуру CustomSmartPointer, единственная настраиваемая функциональность которой заключается в том, что она выведет

    Dropping CustomSmartPointer!

когда экземпляр выходит из области видимости. Этот пример показывает, когда язык Rust выполняет метод drop.

Листинг 15.14. Структура CustomSmartPointer, реализующая типаж Drop там, где мы разместим код очистки
src/main.rs
```rust
struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Отбрасывается CustomSmartPointer с данными `{}`!", self.data);
    }
}

fn main() {
    let c = CustomSmartPointer { data: String::from("мои вещи") };
    let d = CustomSmartPointer { data: String::from("чужие вещи") };
    println!("Экземпляры CustomSmartPointer созданы.");
}
```

Типаж Drop включен в прелюдию, поэтому нам не нужно вводить его в область видимости. Мы реализуем типаж Drop в типе CustomSmartPointer ① и предоставляем реализацию метода drop, который вызывает макрокоманду println! ②. В теле метода drop вы будете размещать любую логику, которую хотите выполнять, когда экземпляр вашего типа выходит из области видимости. Здесь мы печатаем текст, чтобы показать, когда Rust вызывает метод drop.

В функции main мы создаем два экземпляра типа CustomSmartPointer ③④, а затем печатаем сообщение Экземпляры CustomSmartPointer созданы. ⑤ В конце функции main ⑥ экземпляры типа CustomSmartPointer выйдут из области видимости, и Rust вызовет код, который мы поместим в метод drop②, печатающий окончательное сообщение. Обратите внимание, нам не нужно было вызывать метод drop явным образом.

Когда мы выполним эту программу, то увидим следующие данные: