---
source_image: page_360.png
page_number: 360
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.24
tokens: 11426
characters: 803
timestamp: 2025-12-24T10:33:12.197795
finish_reason: stop
---

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

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!("{:#?}", sorted in {num_sort_operations} operations", list);
}
```

Листинг 13-9: Использование замыкания FnMut с sort_by_key разрешено

Трейты Fn важны при определении или использовании функций или типов, использующих замыкания. В следующем разделе мы обсудим итераторы. Многие методы итераторов принимают аргументы замыкания, поэтому не забывайте об этих деталях замыкания, по мере того как мы продвигаемся дальше!