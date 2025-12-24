---
source_image: page_055.png
page_number: 55
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.30
tokens: 7300
characters: 1307
timestamp: 2025-12-24T09:55:09.824416
finish_reason: stop
---

лах той или иной страны вид знака не имеет значения. Оба они работают должным образом. Но такое разночтение препятствует международным связям, поскольку у числа вида 1,024 может быть различное толкование. Могу предсказать, что в итоге все остановятся на использовании точки, приняв ее за международный стандарт, поскольку в языках программирования применяется точка, а основная часть информационных потоков, проходящих через наши программы, написана на этих языках.

Функция scientific преобразует большое число с плавающей точкой в строку с e-нотацией:

function scientific(a) {
    if (is_zero(a)) {
        return "0";
    }
    a = normalize(a);
    let s = big_integer.string(big_integer.abs(a.coefficient));
    let e = a.exponent + s.length - 1;
    if (s.length > 1) {
        s = s.slice(0, 1) + "." + s.slice(1);
    }
    if (e !== 0) {
        s += "e" + e;
    }
    if (big_integer.is_negative(a.coefficient)) {
        s = "-" + s;
    }
    return s;
}

И наконец, все эти полезные объекты экспортируются в виде модуля:

export default Object.freeze({
    abs,
    add,
    div,
    eq,
    fraction,
    integer,
    is_big_float,
    is_negative,
    is_positive,
    is_zero,
    lt,
    make,
    mul,
    neg,
    normalize,
    number,
    scientific,
    string,
    sub,
    zero
});