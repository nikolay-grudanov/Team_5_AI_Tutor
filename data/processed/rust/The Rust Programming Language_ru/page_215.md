---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.25
tokens: 11659
characters: 1755
timestamp: 2025-12-24T10:27:25.670827
finish_reason: stop
---

подобных методов могут очистить огромные вложенные выражения match, когда вы имеете дело с ошибками.

Лаконичные способы обработки ошибок - unwrap и expect

Использование match работает достаточно хорошо, но может быть довольно многословным и не всегда хорошо передаёт смысл. Тип Result<T, E> имеет множество вспомогательных методов для выполнения различных, более специфических задач. Метод unwrap - это метод быстрого доступа к значениям, реализованный так же, как и выражение match, которое мы написали в Листинге 9-4. Если значение Result является вариантом Ok, unwrap возвращает значение внутри Ok. Если Result - вариант Err, то unwrap вызовет для нас макрос panic!. Вот пример unwrap в действии:

Файл: src/main.rs

use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}

Если мы запустим этот код при отсутствии файла hello.txt, то увидим сообщение об ошибке из вызова panic! метода unwrap:

thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }', src/main.rs:4:49

Другой метод, похожий на unwrap, это expect, позволяющий указать сообщение об ошибке для макроса panic!. Использование expect вместо unwrap с предоставлением хорошего сообщения об ошибке выражает ваше намерение и делает более простым отслеживание источника паники. Синтаксис метода expect выглядит так:

Файл: src/main.rs

use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
        .expect("hello.txt should be included in this project");
}

expect используется так же как и unwrap: либо возвращается дескриптор файла либо вызывается макрос panic!.

Наше сообщение об ошибке в expect будет передано в panic! и заменит стандартное