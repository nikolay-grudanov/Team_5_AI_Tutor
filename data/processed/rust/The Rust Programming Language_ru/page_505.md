---
source_image: page_505.png
page_number: 505
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.56
tokens: 11657
characters: 1693
timestamp: 2025-12-24T10:39:34.610744
finish_reason: stop
---

образом, если мы попытаемся получить содержимое черновика, мы получим ошибку компилятора, сообщающую, что метод не существует. В результате мы не сможем случайно отобразить черновик содержимого записи в работающей программе, потому что этот код даже не скомпилируется. В листинге 17-19 показано определение структур Post и DraftPost, а также методов для каждой из них:

Файл: src/lib.rs

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
    pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

    pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Листинг 17-19: Структура Post с методом content и структура DraftPost без метода content

Обе структуры, Post и DraftPost, имеют приватное поле content, в котором хранится текст сообщения блога. Структуры больше не содержат поле state, потому что мы перемещаем кодирование состояния в типы структур. Структура Post будет представлять опубликованную публикацию, и у неё есть метод content, который возвращает content.

У нас все ещё есть функция Post::new, но вместо возврата экземпляра Post она возвращает экземпляр DraftPost. Поскольку поле content является приватным и нет никаких функций, которые возвращают Post, просто так создать экземпляр Post уже невозможно.

Структура DraftPost имеет метод add_text, поэтому мы можем добавлять текст к content как и раньше, но учтите, что в DraftPost не определён метод content! Так что теперь программа гарантирует, что все записи начинаются как черновики, а черновики