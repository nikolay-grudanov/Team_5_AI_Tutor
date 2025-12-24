---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.57
tokens: 7725
characters: 2376
timestamp: 2025-12-24T10:51:00.923909
finish_reason: stop
---

что вызвало ошибку. Обратная трассировка — это список всех функций, которые были вызваны, чтобы добраться до этой точки. Обратные трассировки в Rust работают так же, как и в других языках. Ключ к чтению обратной трассировки — начать сверху и читать до тех пор, пока вы не увидите файлы, которые вы писали. Именно в этом месте возникла проблема. Строки над строками с упоминанием ваших файлов показывают код, который вызвал ваш код; строки ниже показывают код, который был вызван вашим кодом. Эти строки могут включать основной код Rust, код стандартной библиотеки или используемые упаковки. Давайте попробуем получить обратную трассировку, установив переменную среды RUST_BACKTRACE, равной любому значению, кроме 0. Листинг 9.2 показывает результат, аналогичный тому, что вы увидите.

Листинг 9.2. Обратная трассировка, сгенерированная вызовом макрокоманды panic!, появляется при установке переменной среды RUST_BACKTRACE

$ RUST_BACKTRACE=1 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
    Running `target/debug/panic`
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 99', libcore/
slice/mod.rs:2448:10
stack backtrace:
   0: std::sys::unix::backtrace::tracing::imp::unwind_backtrace
      at libstd/sys/unix/backtrace/tracing/gcc_s.rs:49
   1: std::sys_common::backtrace::print
      at libstd/sys_common/backtrace.rs:71
      at libstd/sys_common/backtrace.rs:59
   2: std::panicking::default_hook::{closure}
      at libstd/panicking.rs:211
   3: std::panicking::default_hook
      at libstd/panicking.rs:227
   4: <std::panicking::begin_panic::PanicPayload<A> as core::panic::BoxMeUp>::get
      at libstd/panicking.rs:476
   5: std::panicking::continue_panic_fmt
      at libstd/panicking.rs:390
   6: std::panicking::try::do_call
      at libstd/panicking.rs:325
   7: core::ptr::drop_in_place
      at libcore/panicking.rs:77
   8: core::ptr::drop_in_place
      at libcore/panicking.rs:59
   9: <usize as core::slice::SliceIndex<[T]>>::index
      at libcore/slice/mod.rs:2448
  10: core::slice::<impl core::ops::index::Index<I> for [T]>::index
      at libcore/slice/mod.rs:2316
  11: <alloc::vec::Vec<T> as core::ops::index::Index<I>>::index
      at liballoc/vec.rs:1653
  12: panic::main
      at src/main.rs:4
  13: std::rt::lang_start::{closure}
      at libstd/rt.rs:74
  14: std::panicking::try::do_call