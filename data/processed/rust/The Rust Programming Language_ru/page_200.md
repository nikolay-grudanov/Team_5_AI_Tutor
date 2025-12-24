---
source_image: page_200.png
page_number: 200
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.05
tokens: 11594
characters: 1430
timestamp: 2025-12-24T10:26:55.818220
finish_reason: stop
---

HashMap однородны: все ключи должны иметь одинаковый тип и все значения должны иметь тоже одинаковый тип.

Доступ к данным в HashMap

Мы можем получить значение из HashMap по ключу, с помощью метода get, как показано в листинге 8-21.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

Листинг 8-21: Доступ к очкам команды "Blue", которые хранятся в хеш-карте

Здесь score будет иметь количество очков, связанное с командой "Blue", результат будет 10. Метод get возвращает Option<&V>; если для какого-то ключа нет значения в HashMap, get вернёт None. Из-за такого подхода программе следует обрабатывать Option, вызывая copied для получения Option<i32> вместо Option<&i32>, затем unwrap_or для установки score в ноль, если scores не содержит данных по этому ключу.

Мы можем перебирать каждую пару ключ/значение в HashMap таким же образом, как мы делали с векторами, используя цикл for:

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{}: {}", key, value);
}
```

Этот код будет печатать каждую пару в произвольном порядке:

Yellow: 50
Blue: 10

Хеш-карты и владение