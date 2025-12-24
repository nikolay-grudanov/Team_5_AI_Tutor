---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.81
tokens: 7471
characters: 1850
timestamp: 2025-12-24T10:50:31.361605
finish_reason: stop
---

let field_value = String::from("Синий");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name и field_value в этом месте недопустимы, попробуйте
// их использовать и увидите, какая ошибка компилятора произойдет!

Мы не можем использовать переменные field_name и field_value после того, как они были перемещены в хеш-отображение вызовом метода insert.

Если мы вставим ссылки на значения в хеш-отображение, то значения не будут перемещены в хеш-отображение. Значения, на которые указывают ссылки, должны быть действительными по крайней мере до тех пор, пока действует хеш-отображение. Более подробно об этих трудностях мы поговорим в разделе «Проверка ссылок с помощью жизненных циклов».

Доступ к значениям в хеш-отображении

Мы можем получить значение из хеш-отображения, предоставив его ключ методу get, как показано в листинге 8.23.

Листинг 8.23. Доступ к баллу Синей команды, хранящемуся в хеш-отображении
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Синяя"), 10);
scores.insert(String::from("Желтая"), 50);

let team_name = String::from("Синяя");
let score = scores.get(&team_name);

Здесь у score будет значение, связанное с Синей командой, и результат будет Some(&10). Результат обернут в Some, потому что метод get возвращает Option<&V>. Если для этого ключа значения в хеш-отображении нет, то метод get вернет None. Программа должна будет обрабатывать тип Option одним из способов, которые мы рассмотрели в главе 6.

Мы можем перебрать каждую пару ключ/значение хеш-отображения аналогично тому, как мы делаем с векторами, используя цикл for:

use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Синяя"), 10);
scores.insert(String::from("Желтая"), 50);

for (key, value) in &scores {
    println!("{}: {}", key, value);
}