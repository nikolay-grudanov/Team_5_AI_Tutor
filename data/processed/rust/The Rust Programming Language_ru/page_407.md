---
source_image: page_407.png
page_number: 407
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 57.44
tokens: 11782
characters: 2069
timestamp: 2025-12-24T10:35:41.742351
finish_reason: stop
---

Первое значение Cons содержит 1 и другой List. Это значение List является следующим значением Cons, которое содержит 2 и другой List. Это значение List является ещё один значением Cons, которое содержит 3 и значение List, которое наконец является Nil, не рекурсивным вариантом, сигнализирующим об окончании списка.

Если мы попытаемся скомпилировать код в листинге 15-3, мы получим ошибку, показанную в листинге 15-4:

```
$ cargo run
   Compiling cons-list v0.1.0 (file:///projects/cons-list)
error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |         ---- recursive without indirection

help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List` representable
2 |     Cons(i32, Box<List>),
  |         ++++    +

error[E0391]: cycle detected when computing drop-check constraints for `List`
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^
  = note: ...which immediately requires computing drop-check constraints for `List` again
  = note: cycle used when computing dropck types for `Canonical { max_universe: U0, variables: [], value: ParamEnvAnd { param_env: ParamEnv { caller_bounds: [], reveal: UserFacing, constness: NotConst }, value: List } }`

Some errors have detailed explanations: E0072, E0391.
For more information about an error, try `rustc --explain E0072`.
error: could not compile `cons-list` due to 2 previous errors
```

Листинг 15-4: Ошибка, которую мы получаем при попытке определить рекурсивное перечисление

Ошибка говорит о том, что этот тип "имеет бесконечный размер". Причина в том, что мы определили List в форме, которая является рекурсивной: она непосредственно хранит другое значение своего собственного типа. В результате Rust не может определить, сколько места ему нужно для хранения значения List. Давайте разберёмся, почему мы получаем эту ошибку. Сначала мы рассмотрим, как Rust решает, сколько места ему нужно для хранения значения нерекурсивного типа.

Вычисление размера нерекурсивного типа