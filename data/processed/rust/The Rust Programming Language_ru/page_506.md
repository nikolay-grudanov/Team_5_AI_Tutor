---
source_image: page_506.png
page_number: 506
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.18
tokens: 11743
characters: 2059
timestamp: 2025-12-24T10:39:52.090898
finish_reason: stop
---

публикаций не имеют своего контента для отображения. Любая попытка обойти эти ограничения приведёт к ошибке компилятора.

Реализация переходов в виде преобразований в другие типы

Так как же получить опубликованный пост? Мы хотим обеспечить соблюдение правила, согласно которому черновик записи должен быть рассмотрен и утверждён до того, как он будет опубликован. Запись, находящаяся в состоянии проверки, по-прежнему не должна отображать содержимое. Давайте реализуем эти ограничения, добавив ещё одну структуру, PendingReviewPost, определив метод request_review у DraftPost, возвращающий PendingReviewPost, и определив метод approve у PendingReviewPost, возвращающий Post, как показано в листинге 17-20:

Файл: src/lib.rs

```rust
impl DraftPost {
    // --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

Листинг 17-20: Тип PendingReviewPost, который создаётся путём вызова request_review экземпляра DraftPost и метод approve, который превращает PendingReviewPost в опубликованный Post.

Методы request_review и approve забирают во владение self, таким образом поглощая экземпляры DraftPost и PendingReviewPost, которые потом преобразуются в PendingReviewPost и опубликованную Post, соответственно. Таким образом, у нас не будет никаких долгоживущих экземпляров DraftPost, после того, как мы вызвали у них request_review и так далее. В структуре PendingReviewPost не определён метод content, поэтому попытка прочитать его содержимое приводит к ошибке компилятора, также как и в случае с DraftPost. Так как единственным способом получить опубликованный экземпляр Post, у которого действительно есть объявленный метод content, является вызов метода approve у экземпляра PendingReviewPost, а единственный способ получить PendingReviewPost - это вызвать метод request_review у