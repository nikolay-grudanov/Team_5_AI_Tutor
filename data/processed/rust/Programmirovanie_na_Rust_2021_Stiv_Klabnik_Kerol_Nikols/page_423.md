---
source_image: page_423.png
page_number: 423
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.44
tokens: 7497
characters: 1881
timestamp: 2025-12-24T10:56:56.889609
finish_reason: stop
---

2 for _ in 0..10 {
    3 let handle = thread::spawn(move || {
        4 let mut num = counter.lock().unwrap();
        5 *num += 1;
    });
    6 handles.push(handle);
}
for handle in handles {
    7 handle.join().unwrap();
}
8 println!("Результат: {}", *counter.lock().unwrap());
}

Мы создаем переменную counter для хранения типа i32 внутри Mutex<T> ①, как это было сделано в листинге 16.12. Далее мы создаем 10 потоков исполнения, перебирая диапазон чисел ②. Мы используем функцию thread::spawn и даем всем потокам одинаковое замыкание, которое перемещает переменную counter в поток ③, получает замок для умного указателя Mutex<T>, вызывая метод lock ④, а затем прибавляет 1 к значению в мьютексе ⑤. Когда поток завершит выполнение своего замыкания, переменная num выйдет из области видимости и освободит замок, в результате чего его сможет получить еще один поток.

В главном потоке исполнения мы собираем все дескрипторы ⑥, а затем, как и в листинге 16.2, для каждого из них вызываем join, тем самым обеспечивая завершение работы всех потоков ⑦. В этот момент главный поток получит замок и выведет результат этой программы ⑧.

Мы предупредили, что этот пример не будет компилироваться. А теперь давайте выясним почему!¹

error[E0382]: capture of moved value: `counter`
 --> src/main.rs:10:27
  |
9 |     let handle = thread::spawn(move || {
  |                        ------ value moved (into closure) here
10 |         let mut num = counter.lock().unwrap();
  |         ^^^^^^^ value captured here after move
= note: move occurs because `counter` has type `std::sync::Mutex<i32>`,
which does not implement the `Copy` trait

error[E0382]: capture of moved value: `counter`
 --> src/main.rs:21:29
  |

¹ ошибка[E0382]: захват перемещенного значения: `counter`
ошибка[E0382]: использование перемещенного значения: `counter`
ошибка: прерывание работы из-за двух предыдущих ошибок