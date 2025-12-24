---
source_image: page_297.png
page_number: 297
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.27
tokens: 11731
characters: 1788
timestamp: 2025-12-24T10:31:07.270282
finish_reason: stop
---

$ cargo test one_hundred
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.69s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test tests::one_hundred ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2 filtered out;
finished in 0.00s

Был запущен только тест с названием one_hundred; имена остальных тестов отличались. Строка 2 filtered out в конце тестового вывода позволяет нам понять, что были ещё и другие тесты.

Таким образом мы не можем указать имена нескольких тестов; будет использоваться только первое значение, указанное для cargo test. Но есть способ запустить несколько тестов.

Использование фильтров для запуска нескольких тестов

Мы можем указать часть имени теста, и будет запущен любой тест, имя которого соответствует этому значению. Например, поскольку имена двух наших тестов содержат add, мы можем запустить эти два, запустив cargo test add:

$ cargo test add
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.61s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 2 tests
test tests::add_three_and_two ... ok
test tests::add_two_and_two ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1 filtered out;
finished in 0.00s

Эта команда запускала все тесты с add в имени и отфильтровывала тест с именем one_hundred. Также обратите внимание, что модуль, в котором появляется тест, становится частью имени теста, поэтому мы можем запускать все тесты в модуле, фильтруя имя модуля.

Игнорирование тестов

Бывает, что некоторые тесты требуют продолжительного времени для своего исполнения, и вы хотите исключить их из исполнения при запуске cargo test. Вместо