---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.18
tokens: 7267
characters: 1491
timestamp: 2025-12-24T09:55:30.624822
finish_reason: stop
---

return "0";
}
let {numerator, denominator} = normalize(a);

Числитель делится на знаменатель. Если действие выполнено без остатка, значит, получен нужный результат.

    let [quotient, remains] = big_integer.divrem(numerator, denominator);
    let result = big_integer.string(quotient);
    if (remains !== big_integer.zero) {

Если предоставлен аргумент nr_places, результат имеет десятичный формат. Остатки сводятся к масштабу степени 10, и выполняется целочисленное деление. Если остаток составляет не менее половины знаменателя, производится округление в большую сторону.

    remains = big_integer.abs(remains);
    if (nr_places === undefined) {
        let [fractus, residue] = big_integer.divrem(
            big_integer.mul(
                remains,
                big_integer.power(big_integer.ten, nr_places)
            ),
            denominator
        );
        if (!big_integer.abs_lt(
            big_integer.mul(residue, big_integer.two),
            denominator
        )) {
            fractus = big_integer.add(fractus, big_integer.wun);
        }
        result += "." + big_integer.string(fractus).padStart(
            big_integer.number(nr_places),
            "0"
        );
    } else {

Результат будет в виде смешанной дроби.

    result = (
        (
            result === "0"
            ? ""
            : result + " "
        )
        + big_integer.string(remains)
        + "/"
        + big_integer.string(denominator)
    );
    }
    return result;
}