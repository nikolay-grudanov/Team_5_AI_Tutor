---
source_image: page_199.png
page_number: 199
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.16
tokens: 7546
characters: 2154
timestamp: 2025-12-24T10:51:00.477710
finish_reason: stop
---

могательных методов для выполнения разных видов работ. Один из этих методов, именуемый unwrap, представляет собой укороченный метод, который реализован точно так же, как выражение match, описанное в листинге 9.4. Если значение Result является вариантом Ok, то метод unwrap вернет значение внутрь Ok. Если же Result равно варианту Err, то метод unwrap вызовет макрокоманду panic!. Вот пример метода unwrap в действии:

src/main.rs
    use std::fs::File;

    fn main() {
        let f = File::open("hello.txt").unwrap();
    }

Если мы выполним этот код без файла hello.txt, то увидим сообщение об ошибке из макрокоманды panic!, которую метод unwrap вызывает¹:

    thread 'main' panicked at 'called 'Result::unwrap()' on an 'Err' value: Error { repr: Os { code: 2, message: "No such file or directory" } }', /src/libcore/result.rs:906:4

Еще один метод, expect, похожий на unwrap, позволяет помимо этого выбирать сообщение об ошибке макрокоманды panic!. Использование метода expect вместо unwrap и корректные сообщения об ошибках лучше передают ваши намерения и облегчают отслеживание источника паники. Синтаксис метода expect выглядит следующим образом:

src/main.rs
    use std::fs::File;

    fn main() {
        let f = File::open("hello.txt").expect("Не получилось открыть hello.txt");
    }

Мы используем метод expect таким же образом, как и метод unwrap, — чтобы вернуть файловый дескриптор или вызвать макрокоманду panic!. Сообщение об ошибке, используемое методом expect в вызове макрокоманды panic!, будет параметром, который мы передаем методу expect, а не стандартным сообщением макрокоманды panic!, которое используется методом unwrap. Вот как оно выглядит²:

    thread 'main' panicked at 'Не получилось открыть hello.txt: Error { repr: Os { code: 2, message: "No such file or directory" } }',
    /src/libcore/result.rs:906:4

¹ поток 'main' вызвал панику в точке 'Вызвана функция 'Result::unwrap()' для значения 'Err': Error { repr: Os { code: 2, message: "Нет такого файла или каталога" } }'
² поток 'main' вызвал панику в точке 'Не получилось открыть hello.txt: Error { repr: Os { code: 2, message: "Нет такого файла или каталога" } }'