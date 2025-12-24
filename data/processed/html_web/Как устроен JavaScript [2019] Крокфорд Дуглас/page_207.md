---
source_image: page_207.png
page_number: 207
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.75
tokens: 7406
characters: 1801
timestamp: 2025-12-24T09:59:04.305352
finish_reason: stop
---

let mask = big_integer.mask(n);
    let left = big_integer.xor(mask, big_integer.and(a, b));
    let right = big_integer.or(
        big_integer.xor(mask, a),
        big_integer.xor(mask, b)
    );
    return verdict(big_integer.eq(left, right));
},
[jsc.integer()]
);

Я создал генератор, выдающий большие целые числа для некоторых моих тестов. Спецификаторы, предоставляемые JSCheck, высокоэффективны, но им ничего не известно о больших числах, поэтому я написал собственный спецификатор.

function bigint(max_nr_bits) {
    return function () {
        let nr_bits = Math.floor(Math.random() * max_nr_bits);
        let result = big_integer.random(nr_bits);
        return (
            Math.random() < 0.5
            ? big_integer.neg(result)
            : result
        );
    }
}

Тестирование умножения и деления выполняется совместно. Я предоставляю функцию-классификатор, чтобы отбросить попытки, в которых будет деление на нуль.

jsc.claim(
    "mul & div",
    function (verdict, a, b) {
        let product = big_integer.mul(a, b);
        return verdict(big_integer.eq(a, big_integer.div(product, b)));
    },
    [bigint(99), bigint(99)],
    function classifier(a, b) {
        if (!big_integer.is_zero(b)) {
            return "";
        }
    }
);

Я опять тестирую умножение и деление вместе, но на этот раз с учетом остатков. Классификатор выделяет знаки двух значений, производя классификацию "--", "-+", "+-" и "++". Это помогло изолировать ошибки, связанные с обработкой знаков.

jsc.claim("div & mul & remainder", function (verdict, a, b) {
    let [quotient, remainder] = big_integer.divrem(a, b);
    return verdict(big_integer.eq(
        a,
        big_integer.add(big_integer.mul(quotient, b), remainder)
    ));
}, [bigint(99), bigint(99)], function classifier(a, b) {