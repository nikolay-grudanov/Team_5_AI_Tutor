---
source_image: page_252.png
page_number: 252
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.11
tokens: 11637
characters: 1984
timestamp: 2025-12-24T10:29:08.485474
finish_reason: stop
---

fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}

Используя impl Summary для возвращаемого типа, мы указываем, что функция returns_summarizable возвращает некоторый тип, который реализует типаж Summary без обозначения конкретного типа. В этом случае returns_summarizable возвращает Tweet, но код, вызывающий эту функцию, этого не знает.

Возможность возвращать тип, который определяется только реализуемым им признаком, особенно полезна в контексте замыканий и итераторов, которые мы рассмотрим в Главе 13. Замыкания и итераторы создают типы, которые знает только компилятор или типы, которые очень долго указывать. Синтаксис impl Trait позволяет кратко указать, что функция возвращает некоторый тип, который реализует типаж Iterator без необходимости писать очень длинный тип.

Однако, impl Trait возможно использовать, если возвращаете только один тип. Например, данный код, который возвращает значения или типа NewsArticle или типа Tweet, но в качестве возвращаемого типа объявляет impl Summary, не будет работать:

fn returns_summarizable(switch: bool) -> impl Summary {
    if switch {
        NewsArticle {
            headline: String::from(
                "Penguins win the Stanley Cup Championship!",
            ),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                 hockey team in the NHL.",
            ),
        }
    } else {
        Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        }
    }
}