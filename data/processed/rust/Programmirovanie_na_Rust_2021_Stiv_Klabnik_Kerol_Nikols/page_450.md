---
source_image: page_450.png
page_number: 450
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.09
tokens: 7470
characters: 2009
timestamp: 2025-12-24T10:57:39.611217
finish_reason: stop
---

```rust
fn request_review(self: Box<Self>) -> Box<dyn State> {
    self
}

fn approve(self: Box<Self>) -> Box<dyn State> {
    self
}
```

Мы добавляем метод approve в типаж State и новую структуру, реализующую типаж State, состояние Published.

Аналогично методу request_review, если мы вызовем метод approve для структуры Draft, то он не будет иметь никакого эффекта, потому что он возвращает self ①. Когда мы вызываем метод approve для структуры PendingReview, он возвращает новый, обернутый в умный указатель Box экземпляр структуры Published ②. Структура Published реализует типаж State, и как для метода request_review, так и для метода approve она возвращает себя, поскольку в этих случаях статья должна оставаться в состоянии Published.

Теперь нам нужно обновить метод content для структуры Post: если состояние равно Published, то мы хотим вернуть значение, находящееся в поле content статьи. В противном случае мы хотим вернуть пустой строковый срез, как показано в листинге 17.17.

Листинг 17.17. Обновление метода content в структуре Post для делегирования полномочий методу content в типаже State

src/lib.rs
```rust
impl Post {
    // --пропуск--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(&self)
    }
    // --пропуск--
}
```

Поскольку цель состоит в том, чтобы держать все эти правила внутри структур, которые реализуют типаж State, мы вызываем метод content для значения в поле state и передаем экземпляр статьи (то есть self) в качестве аргумента. Затем мы возвращаем значение, получаемое в результате использования метода content, для значения поля state.

Мы вызываем метод as_ref для экземпляра типа Option, потому что нам нужна ссылка на значение внутри Option, а не владение значением. Поскольку поле state равно Option<Box<dyn State>>, когда мы вызываем as_ref, возвращается Option<&Box<dyn State>>. Если бы мы не вызывали as_ref, то возникла бы ошибка, потому что мы не можем переместить state из заимствованной ссылки &self параметра функции.