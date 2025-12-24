---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.96
tokens: 7405
characters: 1604
timestamp: 2025-12-24T10:51:22.953603
finish_reason: stop
---

циональностью тех, кто вызывает нашу функцию, при этом предотвращая повторы кода.

Продолжая пример функции largest, листинг 10.4 показывает две функции — обе отыскивают наибольшее значение в срезе.

Листинг 10.4. Две функции, отличающиеся только именами и типами в сигналах src/main.rs

```rust
fn largest_i32(list: &[i32]) -> i32 {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn largest_char(list: &[char]) -> char {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("Наибольшее число равно {}", result);

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("Наибольший символ равен {}", result);
}
```

Функция largest_i32 — это именно та функция, которую мы извлекли в листинге 10.3, она отыскивает в срезе наибольшее значение типа i32. Функция largest_char ищет в срезе наибольшее значение типа char. Тела функций имеют одинаковый код, поэтому давайте исключим повторы, введя параметр обобщенного типа в единственную функцию.

В целях параметризации типов в новой определяемой нами функции нужно назвать типовой параметр, так же как мы делаем это для входных параметров, принимаемых функцией. В качестве имени типового параметра можно использовать любой идентификатор. Но мы будем использовать T, потому что, по соглашению,