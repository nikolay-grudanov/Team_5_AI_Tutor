---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.79
tokens: 11563
characters: 1190
timestamp: 2025-12-24T10:21:38.967956
finish_reason: stop
---

Внешний цикл имеет метку 'counting_up, и он будет считать от 0 до 2. Внутренний цикл без метки ведёт обратный отсчёт от 10 до 9. Первый break, который не содержит метку, выйдет только из внутреннего цикла. Оператор break 'counting_up; завершит внешний цикл. Этот код напечатает:

$ cargo run
Compiling loops v0.1.0 (file:///projects/loops)
Finished dev [unoptimized + debuginfo] target(s) in 0.58s
    Running `target/debug/loops`
count = 0
remaining = 10
remaining = 9
count = 1
remaining = 10
remaining = 9
count = 2
remaining = 10
End count = 2

Циклы с условием while

В программе часто требуется проверить состояние условия в цикле. Пока условие истинно, цикл выполняется. Когда условие перестаёт быть истинным, программа вызывает break, останавливая цикл. Такое поведение можно реализовать с помощью комбинации loop, if, else и break. При желании попробуйте сделать это в программе. Это настолько распространённый паттерн, что в Rust реализована встроенная языковая конструкция для него, называемая цикл while. В листинге 3-3 мы используем while, чтобы выполнить три цикла программы, производя каждый раз обратный отсчёт, а затем, после завершения цикла, печатаем сообщение и выводим.