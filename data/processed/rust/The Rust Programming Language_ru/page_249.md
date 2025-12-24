---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.77
tokens: 11612
characters: 1701
timestamp: 2025-12-24T10:29:04.866315
finish_reason: stop
---

pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}

Чтобы использовать такую версию типажа Summary, нужно только определить метод summarize_author, при реализации типажа для типа:

impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}

После того, как мы определим summarize_author, можно вызвать summarize для экземпляров структуры Tweet и реализация по умолчанию метода summarize будет вызывать определение summarize_author которое мы уже предоставили. Так как мы реализовали метод summarize_author типажа Summary, то типаж даёт нам поведение метода summarize без необходимости писать код.

let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};

println!("1 new tweet: {}", tweet.summarize());

Этот код печатает 1 new tweet: (Read more from @horse_ebooks...).

Обратите внимание, что невозможно вызвать реализацию по умолчанию из переопределённой реализации того же метода.

Типажи как параметры

Теперь, когда вы знаете, как определять и реализовывать типажи, можно изучить, как использовать типажи, чтобы определить функции, которые принимают много различных типов. Мы будем использовать типаж Summary, реализованный для типов NewsArticle и Tweet в листинге 10-13, чтобы определить функцию notify, которая вызывает метод summarize для его параметра item, который имеет некоторый тип, реализующий типаж Summary. Для этого мы используем синтаксис impl Trait примерно так: