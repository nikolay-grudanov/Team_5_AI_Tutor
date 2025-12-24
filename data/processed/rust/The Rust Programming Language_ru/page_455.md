---
source_image: page_455.png
page_number: 455
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.57
tokens: 11749
characters: 1967
timestamp: 2025-12-24T10:37:38.088370
finish_reason: stop
---

use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
}

Листинг 16-1: Создание нового потока для печати определённого текста, в то время как основной поток печатает что-то другое

Обратите внимание, что когда основной поток программы на Rust завершается, все порождённые потоки закрываются, независимо от того, завершили они работу или нет. Вывод этой программы может каждый раз немного отличаться, но он будет выглядеть примерно так:

hi number 1 from the main thread!
hi number 1 from the spawned thread!
hi number 2 from the main thread!
hi number 2 from the spawned thread!
hi number 3 from the main thread!
hi number 3 from the spawned thread!
hi number 4 from the main thread!
hi number 4 from the spawned thread!
hi number 5 from the spawned thread!

Вызовы thread::sleep заставляют поток на короткое время останавливать своё выполнение, позволяя выполняться другим потокам. Очерёдность выполнения потоков вероятно будет меняться, но это не гарантировано: это зависит от того, как ваша операционная система планирует потоки. В этом цикле основной поток печатает первым, не смотря на то, что оператор печати из порождённого потока появляется раньше в коде. И даже несмотря на то, что мы проинструктировали порождённый поток печатать до тех пор, пока значение i не достигнет числа 9, оно успело дойти только до 5, когда основной поток завершился.

Если вы запустите этот код и увидите вывод только из основного потока или не увидите печати из других потоков, попробуйте увеличить числа в диапазонах, чтобы дать операционной системе больше возможностей для переключения между потоками.

Ожидание завершения работы всех потоков используя join