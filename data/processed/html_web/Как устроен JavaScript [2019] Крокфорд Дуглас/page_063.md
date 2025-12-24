---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.99
tokens: 7253
characters: 1562
timestamp: 2025-12-24T09:55:14.061029
finish_reason: stop
---

|| !big_integer.is_big_integer(denominator)
|| big_integer.zero === denominator
    ) {
        return undefined;
    }

Если знаменатель — отрицательное число, знак переносится в числитель.

    if (big_integer.is_negative(denominator)) {
        numerator = big_integer.neg(numerator);
        denominator = big_integer.abs(denominator);
    }
    return make_big_rational(numerator, denominator);
}

А если аргумент является строковым значением? В таком случае выполняется его парсинг.

    if (typeof numerator === "string") {
        let parts = numerator.match(number_pattern);
        if (!parts) {
            return undefined;
        }

        // Определение групп:
        // [1] sign
        // [2] integer
        // [3] top
        // [4] bottom
        // [5] frac
        // [6] exp
        // [7] naked frac

        if (parts[7]) {
            return make(
                big_integer.make(parts[1] + parts[7]),
                big_integer.power(big_integer.ten, parts[7].length)
            );
        }
        if (parts[4]) {
            let bottom = big_integer.make(parts[4]);
            if (parts[3]) {
                return make(
                    big_integer.add(
                        big_integer.mul(
                            big_integer.make(parts[1] + parts[2]),
                            bottom
                        ),
                        big_integer.make(parts[3])
                    ),
                    bottom
                );
            }
            return make(parts[1] + parts[2], bottom);
        }