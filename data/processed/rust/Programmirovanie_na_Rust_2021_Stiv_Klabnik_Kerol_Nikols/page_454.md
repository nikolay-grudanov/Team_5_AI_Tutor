---
source_image: page_454.png
page_number: 454
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.79
tokens: 7392
characters: 1672
timestamp: 2025-12-24T10:57:42.285642
finish_reason: stop
---

Листинг 17.19. Структуры Post с методом content и DraftPost без метода content

src/lib.rs

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

Структуры Post и DraftPost имеют приватное поле content, в котором хранится текст поста. Указанные структуры больше не имеют поля state, потому что мы перемещаем кодировку состояния в типы структур. Структура Post будет представлять опубликованный пост. У нее есть метод content, который возвращает в 2 содержимое поля content.

У нас по-прежнему есть функция Post::new, но вместо того, чтобы возвращать экземпляр структуры Post, она возвращает экземпляр структуры DraftPost 1. Поскольку поле content приватное и нет функций, которые возвращают Post, невозможно создать экземпляр структуры Post прямо сейчас.

Структура DraftPost имеет метод add_text, поэтому мы можем добавлять текст в поле content, как раньше 3. Но обратите внимание, что у DraftPost не определен метод content! Таким образом, теперь программа делает так, что все статьи начинаются как черновые, а черновые статьи не имеют содержимого, доступного для показа. Любая попытка обойти эти ограничения приведет к ошибке компилятора.

Реализация переходов как трансформаций в разные типы

Тогда как получить опубликованную статью? Мы хотим, чтобы соблюдалось правило, согласно которому черновая статья должна быть проверена и одобрена до