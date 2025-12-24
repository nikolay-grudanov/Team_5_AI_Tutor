---
source_image: page_030.png
page_number: 30
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.11
tokens: 7313
characters: 1735
timestamp: 2025-12-24T09:54:26.029219
finish_reason: stop
---

3.4 Как работают большие целые числа

Функция eq определяет, содержат ли два больших целых числа одни и те же значения разрядов:

function eq(comparahend, comparator) {
    return comparahend === comparator || (
        comparahend.length === comparator.length
        && comparahend.every(function (element, element_nr) {
            return element === comparator[element_nr];
        })
    );
}

Функция abs_lt определяет, меньше ли абсолютное значение большого целого числа абсолютного значения другого большого целого числа. Функция lt определяет, меньше ли значение большого целого числа со знаком значения другого большого целого числа со знаком. Этим функциям приходится труднее, если два больших целых числа одинаковой длины. Их работа может стать легче при наличии версии функции reduce, способной работать в обратном порядке, а также завершать работу на ранней стадии.

function abs_lt(comparahend, comparator) {
    return (
        comparahend.length === comparator.length
        ? comparahend.reduce(
            function (reduction, element, element_nr) {
                if (element_nr !== sign) {
                    const other = comparator[element_nr];
                    if (element !== other) {
                        return element < other;
                    }
                }
                return reduction;
            },
            false
        )
        : comparahend.length < comparator.length
    );
}

function lt(comparahend, comparator) {
    return (
        comparahend[sign] !== comparator[sign]
        ? is_negative(comparahend)
        : (
            is_negative(comparahend)
            ? abs_lt(comparator, comparahend)
            : abs_lt(comparahend, comparator)
        )
    );
}