---
source_image: page_213.png
page_number: 213
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.14
tokens: 7364
characters: 1415
timestamp: 2025-12-24T10:51:18.161286
finish_reason: stop
---

if number > largest {
    largest = number;
}
}
println!("Наибольшее число равно {}", largest);
let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];
let mut largest = number_list[0];
for number in number_list {
    if number > largest {
        largest = number;
    }
}
println!("Наибольшее число равно {}", largest);
}

Этот код работает. Вместе с тем необходимость повторять код утомляет, и возможны ошибки. Если мы хотим внести изменения в код, нам также приходится обновлять его в нескольких местах.

Для того чтобы устранить этот повтор, мы можем создать абстракцию, определив функцию, которая работает с любым списком целых чисел, передаваемых ей в параметре. Это решение делает код понятнее и позволяет выразить идею поиска наибольшего числа в списке абстрактно.

В листинге 10.3 мы извлекли код, который отыскивает наибольшее число, в функцию с именем largest. В отличие от кода в листинге 10.1, который находит наибольшее число только в одном конкретном списке, эта программа отыскивает наибольшее число в двух разных списках.

Листинг 10.3. Абстрактный код для поиска наибольшего числа в двух списках

src/main.rs
fn largest(list: &[i32]) -> i32 {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);