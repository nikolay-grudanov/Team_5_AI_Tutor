---
source_image: page_043.png
page_number: 43
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.95
tokens: 7271
characters: 1256
timestamp: 2025-12-24T09:54:53.024504
finish_reason: stop
---

```javascript
}
if (whole > 0) {
    result.push(whole);
}
return mint(result);
}
if (Array.isArray(value)) {
    return mint(value);
}
}

Функция number преобразует большое целое число в число JavaScript. Это делается с абсолютной точностью, если значение находится в безопасном целочисленном диапазоне:

function number(big) {
    let value = 0;
    let the_sign = 1;
    let factor = 1;
    big.forEach(function (element, element_nr) {
        if (element_nr === 0) {
            if (element === minus) {
                the_sign = -1;
            }
        } else {
            value += element * factor;
            factor *= radix;
        }
    });
    return the_sign * value;
}

Функция string преобразует большое целое число в строку. Преобразование выполняется с абсолютной точностью:

function string(a, radix_2_thru_37 = 10) {
    if (is_zero(a)) {
        return "0";
    }
    radix_2_thru_37 = int(radix_2_thru_37);
    if (
        !Number.isSafeInteger(radix_2_thru_37)
        || radix_2_thru_37 < 2
        || radix_2_thru_37 > 37
    ) {
        return undefined;
    }
    const radish = make(radix_2_thru_37);
    const the_sign = (
        a[sign] === minus
        ? "-"
        : ""
    );
    a = abs(a);
    let digits = [];
```