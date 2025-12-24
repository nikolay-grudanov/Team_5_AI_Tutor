---
source_image: page_268.png
page_number: 268
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.88
tokens: 7454
characters: 1801
timestamp: 2025-12-24T10:52:50.705076
finish_reason: stop
---

failures:
    tests::this_test_will_fail

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out

Обратите внимание, что в этих данных мы не видим Я получил значение 4, которое выводится при успешном выполнении теста. Эти данные были перехвачены. Данные из неуспешного теста — Я получил значение 8 ① — появляются в разделе сводных данных тестирования, которые также показывают причину ошибки теста.

Если мы также в напечатанной форме хотим видеть значения, относящиеся к успешным тестам, то можно отключить поведение перехвата данных с помощью флага --nocapture:

$ cargo test -- --nocapture

Снова выполнив тесты из листинга 11.10 с флагом --nocapture, мы увидим следующие данные:

running 2 tests
I got the value 4
I got the value 8
test tests::this_test_will_pass ... ok
thread 'tests::this_test_will_fail' panicked at 'assertion failed: `(left == right)`
    left: `5`,
    right: `10`', src/lib.rs:19:8
note: Run with `RUST_BACKTRACE=1` for a backtrace.
test tests::this_test_will_fail ... FAILED

failures:

failures:
    tests::this_test_will_fail

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out

Обратите внимание, что данные тестов и результаты тестирования чередуются, — причина в том, что тесты работают параллельно, как мы уже говорили в предыдущем разделе. Попробуйте применить аргумент --test-threads=1 и флаг --nocapture и посмотрите, как будут выглядеть данные!

Выполнение подмножества тестов по имени

Иногда выполнение полного набора тестов занимает много времени. Если вы работаете с кодом в определенном участке, вам, возможно, потребуется выполнить только те тесты, которые относятся к этому коду. Вы можете выбрать подлежащие выполнению тесты, передав команде cargo test имя или имена тестов, которые вы хотите выполнить.