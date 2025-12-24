---
source_image: page_034.png
page_number: 34
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.77
tokens: 7441
characters: 1954
timestamp: 2025-12-24T09:54:42.747632
finish_reason: stop
---

3.8 Как работают большие целые числа

Функция shift_up увеличивает числа, вставляя нули в менее значимые концевые разряды. Это похоже на умножение на степени числа 2. Тем самым можно увеличить большое целое число. В большинстве систем при сдвиге за пределы числа разряды могут быть утрачены, но в этой системе пределы не лимитированы, поэтому разряды не теряются:

function shift_up(big, places) {
    if (is_zero(big)) {
        return zero;
    }
    places = int(places);
    if (Number.isSafeInteger(places)) {
        if (places === 0) {
            return abs(big);
        }
        if (places < 0) {
            return shift_down(big, -places);
        }
        let blanks = Math.floor(places / log2_radix);
        let result = new Array(blanks + 1).fill(0);
        result[sign] = plus;
        places -= blanks * log2_radix;
        if (places === 0) {
            return mint(result.concat(big.slice(least)));
        }
        let carry = big.reduce(function (accumulator, element, element_nr) {
            if (element_nr === sign) {
                return 0;
            }
            result.push(((element << places) | accumulator) & (radix - 1));
            return element >> (log2_radix - places);
        }, 0);
        if (carry > 0) {
            result.push(carry);
        }
        return mint(result);
    }
}

Нам не помешало бы иметь функцию not, выполняющую дополнение всех разрядов, но у нас отсутствуют ограничения на количество разрядов, поэтому непонятно, сколько разрядов нужно переворачивать (flipped). Следовательно, есть функция mask, создающая большое целое число из конкретного количества единичных разрядов. Затем можно будет использовать mask и xor для создания not, но функции not нужно сообщить размер поля разрядов.

function mask(nr_bits) {

Создание строки единичных разрядов:

    nr_bits = int(nr_bits);
    if (nr_bits !== undefined && nr_bits >= 0) {
        let mega = Math.floor(nr_bits / log2_radix);