---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.18
tokens: 7264
characters: 1331
timestamp: 2025-12-24T09:54:42.369347
finish_reason: stop
---

3.16 Как работают большие целые числа

let radish;
if (radix_2_37 === undefined) {
    radix_2_37 = 10;
    radish = ten;
} else {
    if (
        !Number.isInteger(radix_2_37)
        || radix_2_37 < 2
        || radix_2_37 > 37
    ) {
        return undefined;
    }
    radish = make(radix_2_37);
}
result = zero;
let good = false;
let negative = false;
if (value.toUpperCase().split("").every(
    function (element, element_nr) {
        let digit = charset[element];
        if (digit !== undefined && digit < radix_2_37) {
            result = add(mul(result, radish), [plus, digit]);
            good = true;
            return true;
        }
        if (element_nr === sign) {
            if (element === plus) {
                return true;
            }
            if (element === minus) {
                negative = true;
                return true;
            }
        }
        return digit === "_";
    }
) && good) {
    if (negative) {
        result = neg(result);
    }
    return mint(result);
}
return undefined;
}
if (Number.isInteger(value)) {
    let whole = Math.abs(value);
    result = [
        value < 0
        ? minus
        : plus
    ];
    while (whole >= radix) {
        let quotient = Math.floor(whole / radix);
        result.push(whole - (quotient * radix));
        whole = quotient;