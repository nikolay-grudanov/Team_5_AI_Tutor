---
source_image: page_420.png
page_number: 420
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.95
tokens: 11607
characters: 1547
timestamp: 2025-12-24T10:35:48.124019
finish_reason: stop
---

Листинг 15-14: Структура CustomSmartPointer, реализующая типаж Drop, куда мы поместим наш код очистки

Типаж Drop включён в прелюдию, поэтому нам не нужно вводить его в область видимости. Мы реализуем типаж Drop для CustomSmartPointer и реализуем метод drop, который будет вызывать println!. Тело функции drop - это место, где должна располагаться вся логика, которую вы захотите выполнять, когда экземпляр вашего типа выйдет из области видимости. Мы печатаем здесь текст, чтобы наглядно продемонстрировать, когда Rust вызовет drop.

В main мы создаём два экземпляра CustomSmartPointer и затем печатаем CustomSmartPointers created. В конце main наши экземпляры CustomSmartPointer выйдут из области видимости и Rust вызовет код, который мы добавили в метод drop, который и напечатает наше окончательное сообщение. Обратите внимание, что нам не нужно вызывать метод drop явно.

Когда мы запустим эту программу, мы увидим следующий вывод:

$ cargo run
Compiling drop-example v0.1.0 (file:///projects/drop-example)
Finished dev [unoptimized + debuginfo] target(s) in 0.60s
    Running `target/debug/drop-example`
CustomSmartPointers created.
Dropping CustomSmartPointer with data `other stuff`!
Dropping CustomSmartPointer with data `my stuff`!

Rust автоматически вызывал drop в момент выхода наших экземпляров из области видимости, тем самым выполнив заданный нами код. Переменные ликвидируются в обратном порядке их создания, поэтому d была ликвидирована до с. Цель этого примера - дать вам наглядное представление о том, как работает метод drop; в