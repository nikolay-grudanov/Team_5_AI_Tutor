---
source_image: page_238.png
page_number: 238
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.59
tokens: 7446
characters: 1727
timestamp: 2025-12-24T10:52:00.259114
finish_reason: stop
---

вый срез. После того как мы реализовали функцию longest, код в листинге 10.20 должен вывести:

Самая длинная строка равна abcd.

Листинг 10.20. Функция main, вызывающая функцию longest для поиска самого длинного строкового среза из двух
src/main.rs

fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("Самая длинная строка равна {}", result);
}

Обратите внимание, что нужно, чтобы функция брала строковые срезы, то есть ссылки, а не чтобы функция longest владела своими параметрами. Мы хотим разрешить этой функции принимать срезы типа String (тип, хранящийся в переменной string1), а также строковые литералы (то, что содержит переменная string2).

Обратитесь к разделу «Строковые срезы в качестве параметров» (с. 114), где в подробностях обсуждается вопрос, почему параметры, используемые в листинге 10.20, — это как раз то, что нужно.

Если мы попытаемся реализовать функцию longest, как показано в листинге 10.21, то она компилироваться не будет.

Листинг 10.21. Реализация функции longest, которая возвращает самый длинный строковый срез из двух, но которая пока еще не компилируется
src/main.rs

fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

Вместо этого происходит следующая ошибка, которая говорит о жизненном цикле¹:

error[E0106]: missing lifetime specifier
 --> src/main.rs:1:33
  |
1 | fn longest(x: &str, y: &str) -> &str {
      ^ expected lifetime parameter
  |
= help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `x` or `y`

¹ ошибка[E0106]: отсутствующий спецификатор жизненного цикла