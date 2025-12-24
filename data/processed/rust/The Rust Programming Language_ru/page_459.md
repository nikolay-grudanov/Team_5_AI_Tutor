---
source_image: page_459.png
page_number: 459
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.74
tokens: 11651
characters: 1675
timestamp: 2025-12-24T10:37:38.250050
finish_reason: stop
---

Замыкание использует переменную v, поэтому оно захватит v и сделает его частью окружения замыкания. Поскольку thread::spawn запускает это замыкание в новом потоке, мы должны иметь доступ к v внутри этого нового потока. Но при компиляции этого примера, мы получаем следующую ошибку:

```
$ cargo run
Compiling threads v0.1.0 (file:///projects/threads)
error[E0373]: closure may outlive the current function, but it borrows `v`, which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                           ^^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?})", v);
  |                        - `v` is borrowed here

note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |     let handle = thread::spawn(|| {
  |                       _____________^
7 |         println!("Here's a vector: {:?})", v);
8 |     });
  |     ^_____^
help: to force the closure to take ownership of `v` (and any other referenced variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                           ++++
For more information about this error, try `rustc --explain E0373`.
error: could not compile `threads` due to previous error
```

Rust выводит как захватить v и так как в println! нужна только ссылка на v, то замыкание пытается заимствовать v. Однако есть проблема: Rust не может определить, как долго будет работать порождённый поток, поэтому он не знает, будет ли всегда действительной ссылка на v.

В листинге 16-4 приведён сценарий, который с большей вероятностью будет иметь ссылку на v, что будет недопустимо:

Файл: src/main.rs