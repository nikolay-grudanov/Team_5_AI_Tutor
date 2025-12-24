---
source_image: page_455.png
page_number: 455
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.38
tokens: 7482
characters: 2091
timestamp: 2025-12-24T10:57:47.624182
finish_reason: stop
---

публикации. Пост в состоянии ожидания проверки по-прежнему не должен иметь никакого содержимого. Давайте выполним эти ограничения, добавив еще одну структуру PendingReviewPost, определив метод request_review для DraftPost, который возвращает PendingReviewPost, и метод approve для PendingReviewPost, возвращающий Post, как показано в листинге 17.20.

Листинг 17.20. Структура PendingReviewPost, созданная вызовом request_review для DraftPost, и метод approve, который превращает PendingReviewPost в опубликованную статью Post

src/lib.rs

```rust
impl DraftPost {
    // --пропуск--
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

Методы request_review и approve берут self во владение, тем самым поглощая экземпляры DraftPost и PendingReviewPost и трансформируя их соответственно в PendingReviewPost и опубликованный пост Post. Благодаря этому у нас не будет затянувшихся экземпляров DraftPost после вызова для них request_review и так далее. Для структуры PendingReviewPost не определен метод content, поэтому попытка прочитать содержимое этой структуры приводит к ошибке компилятора, как и в случае с DraftPost. Поскольку единственный способ получить экземпляр опубликованной статьи Post, у которой все-таки определен метод content, состоит в вызове метода approve для PendingReviewPost, а единственный способ получить PendingReviewPost — вызвать метод request_review для DraftPost, теперь мы закодировали процесс создания поста в систему типов.

Но мы также должны внести небольшие изменения в функцию main. Методы request_review и approve возвращают новые экземпляры вместо того, чтобы модифицировать структуру, для которой они вызываются, поэтому нужно добавить больше затеняющих присваиваний let post =, чтобы сохранять возвращаемые экземпляры. Мы также не можем иметь проверочные утверждения, в которых со-