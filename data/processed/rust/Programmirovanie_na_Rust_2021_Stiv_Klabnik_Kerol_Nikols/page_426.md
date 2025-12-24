---
source_image: page_426.png
page_number: 426
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.72
tokens: 7685
characters: 2397
timestamp: 2025-12-24T10:57:08.474678
finish_reason: stop
---

}
    for handle in handles {
        handle.join().unwrap();
    }

    println!("Результат: {}", *counter.lock().unwrap());
}

Мы еще раз компилируем и получаем... другие ошибки! Компилятор многому учит нас¹.

① error[E0277]: the trait bound `std::rc::Rc<std::sync::Mutex<i32>>: std::marker::Send` is not satisfied in `[closure@src/main.rs:11:36: 15:10 counter:std::rc::Rc<std::sync::Mutex<i32>>]`
    --> src/main.rs:11:22
    |
11 |         let handle = thread::spawn(move || {
    |                        ^^^^^^^^^^^^^^ `std::rc::Rc<std::sync::Mutex<i32>>` cannot be sent between threads safely
    |
    = help: within `[closure@src/main.rs:11:36: 15:10 counter:std::rc::Rc<std::sync::Mutex<i32>>]`, the trait `std::marker::Send` is not implemented for `std::rc::Rc<std::sync::Mutex<i32>>`
    = note: required because it appears within the type `[closure@src/main.rs:11:36: 15:10 counter:std::rc::Rc<std::sync::Mutex<i32>>]`
    = note: required by `std::thread::spawn`

Блеск! Это очень подробное сообщение об ошибке. Вот некоторые важные части, на которые следует обратить внимание: первая внутристрочная ошибка говорит о том, что не получается переслать мьютекс между потоками безопасным образом (`std::rc::Rc<std::sync::Mutex<i32>>` cannot be sent between threads safely) ②. Причина кроется в следующей важной части, требующей нашего внимания, — самом сообщении об ошибке. Там говорится о том, что граница типажа 'Send' не удовлетворена (trait bound `Send` is not satisfied) ①. Мы поговорим о Send в следующем разделе: это один из типажей, предназначенный для того, чтобы типы, используемые с потоками, применялись в конкурентных ситуациях.

К сожалению, умный указатель Rc<T> небезопасен для совместного использования между потоками. Когда Rc<T> управляет подсчетом ссылок, он прибавляет к числу при каждом вызове метода clone и вычитает из числа, когда каждый клон отбрасывается. Но он не использует никаких параллельных примитивов, чтобы изменения в подсчете не прерывались другим потоком. Это может привести к неправильным подсчетам ссылок — едва уловимым ошибкам, которые могут повлечь за собой утечку памяти или отбрасывание значения, прежде чем мы закончим работу. Нам нужен тип, подобный Rc<T>, который вносит изменения в подсчет ссылок безопасным для потоков способом.

¹ ошибка[E0277]: типажная граница `std::rc::Rc<std::sync::Mutex<i32>>: std::marker::Send` не удовлетворена