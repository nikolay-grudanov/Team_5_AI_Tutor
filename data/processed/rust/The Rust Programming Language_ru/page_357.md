---
source_image: page_357.png
page_number: 357
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.64
tokens: 11531
characters: 1146
timestamp: 2025-12-24T10:33:16.263403
finish_reason: stop
---

unwrap_or_else(Vec::new), чтобы получить новый пустой вектор, если значение равно None.

Теперь рассмотрим метод стандартной библиотеки sort_by_key, определённый для срезов, чтобы увидеть, чем он отличается от unwrap_or_else и почему sort_by_key использует FnMut вместо FnOnce для ограничения трейта. Замыкание получает один аргумент в виде ссылки на текущий элемент в рассматриваемом срезе и возвращает значение типа K, которое может быть упорядочено. Эта функция полезна, когда вы хотите отсортировать срез по определённому атрибуту каждого элемента. В листинге 13-7 у нас есть список экземпляров Rectangle, и мы используем sort_by_key, чтобы упорядочить их по атрибуту width от меньшего к большему:

Файл : src/main.rs

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

Листинг 13-7: Использование sort_by_key для сортировки прямоугольников по ширине

Этот код печатает: