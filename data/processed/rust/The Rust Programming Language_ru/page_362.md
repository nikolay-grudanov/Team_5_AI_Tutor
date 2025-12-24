---
source_image: page_362.png
page_number: 362
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.01
tokens: 11655
characters: 1590
timestamp: 2025-12-24T10:33:44.415199
finish_reason: stop
---

только со структурами данных, которые можно индексировать, типа векторов. Давайте посмотрим как итераторы это делают.

Типаж Iterator и метод next

Все итераторы реализуют типаж Iterator, который определён в стандартной библиотеке. Его определение выглядит так:

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // methods with default implementations elided
}
```

Обратите внимание данное объявление использует новый синтаксис: type Item и Self::Item, которые определяют ассоциированный тип (associated type) с этим типажом. Мы подробнее поговорим о ассоциированных типах в главе 19. Сейчас вам нужно знать, что этот код требует от реализаций типажа Iterator определить требуемый им тип Item и данный тип Item используется в методе next. Другими словами, тип Item будет являться типом элемента, который возвращает итератор.

Типаж Iterator требует, чтобы разработчики определяли только один метод: метод next, который возвращает один элемент итератора за раз обёрнутый в вариант Some и когда итерация завершена, возвращает None.

Мы можем вызывать метод next у итераторов напрямую; в листинге 13-12 показано, какие значения возвращаются при повторных вызовах next у итератора, созданного из вектора.

Файл: src/lib.rs

```rust
#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
```

Листинг 13-12: Вызов метода next итератора