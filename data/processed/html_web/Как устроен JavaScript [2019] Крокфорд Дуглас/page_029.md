---
source_image: page_029.png
page_number: 29
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.71
tokens: 7179
characters: 1008
timestamp: 2025-12-24T09:54:19.597181
finish_reason: stop
---

```javascript
if (proto_big_integer[least] === 1) {
    return wun;
}
if (proto_big_integer[least] === 2) {
    return two;
}
if (proto_big_integer[least] === 10) {
    return ten;
}
} else if (proto_big_integer.length === 2) {
    if (proto_big_integer[least] === 1) {
        return negative_wun;
    }
}
return Object.freeze(proto_big_integer);
}

Наши первые практические функции — отрицание, абсолютное значение и извлечение знака:

function neg(big) {
    if (is_zero(big)) {
        return zero;
    }
    let negation = big.slice();
    negation[sign] = (
        is_negative(big)
        ? plus
        : minus
    );
    return mint(negation);
}

function abs(big) {
    return (
        is_zero(big)
        ? zero
        : (
            is_negative(big)
            ? neg(big)
            : big
        )
    );
}

function signum(big) {
    return (
        is_zero(big)
        ? zero
        : (
            is_negative(big)
            ? negative_wun
            : wun
        )
    );
}
```