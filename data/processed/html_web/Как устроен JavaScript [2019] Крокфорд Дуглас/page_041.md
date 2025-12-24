---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.61
tokens: 7412
characters: 1675
timestamp: 2025-12-24T09:54:55.621564
finish_reason: stop
---

exp = Math.floor(exp / 2);
    if (exp < 1) {
        break;
    }
    big = mul(big, big);
}
    return mint(result);
}

Для сокращения дробей применим функцию gcd:

function gcd(a, b) {
    a = abs(a);
    b = abs(b);
    while (!is_zero(b)) {
        let [ignore, remainder] = divrem(a, b);
        a = b;
        b = remainder;
    }
    return a;
}

Нам нужны функции для преобразования чисел и строк в большие целые числа и обратно. При преобразовании в строки и из строк нужна явная поддержка десятичной системы записи, а также следующих сигнатур: двоичной, восьмеричной, шестнадцатеричной и Base32. Дополнительные сведения о Base32 можно получить по адресу crockford.com/wrmg/base32.html.

Строка digitset позволяет отображать числа на символы. Объект charset отображает символы не числа. Для шестнадцатеричных, десятичных, восьмеричных и двоичных чисел может использоваться поднабор с аналогичным символьным отображением:

const digitset = "0123456789ABCDEFHJKMNPQRSTVWXYZ*~$=U";
const charset = (function (object) {
    digitset.split("").forEach(function (element, element_nr) {
        object[element] = element_nr;
    });
    return Object.freeze(object);
})(Object.create(null)));

Функция make получает число или строку и необязательное основание системы счисления, а возвращает большое целое число. Преобразование выполняется с абсолютной точностью для всех целочисленных значений:

function make(value, radix_2_37) {

Функция make возвращает большое целое число. Параметр value является строкой, а необязательный параметр radix — либо целочисленным значением, либо значением большого целого числа (big_integer):

let result;
if (typeof value === "string") {