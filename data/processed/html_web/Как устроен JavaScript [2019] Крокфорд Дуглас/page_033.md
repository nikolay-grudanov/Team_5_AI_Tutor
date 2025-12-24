---
source_image: page_033.png
page_number: 33
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.85
tokens: 7484
characters: 2048
timestamp: 2025-12-24T09:54:47.660677
finish_reason: stop
---

Функция shift_down уменьшает числа, удаляя наименее значимые разряды. С ее помощью можно уменьшить большое целое число. Это похоже на деление на степени числа 2. Данная операция обычно называется сдвигом вправо (>>>) и выглядит обманчиво, поскольку для уменьшения чисел использует знак «больше». Нумерация разрядов — вещь совершенно произвольная, поэтому представление о том, что разряды увеличиваются справа налево, сбивает с толку. Мы создаем значения из массивов, которые в обычном представлении растут слева направо, следовательно, рост происходит одновременно как справа налево, так и слева направо. В некоторых системах обычного письма строки идут слева направо, а в некоторых — справа налево, поэтому естественность прироста слева направо нельзя считать универсальной. Проблема направления роста разрядов (Endian Problem) уходит своими корнями именно в эту путаницу. Сдвиги влево и вправо дают менее точные результаты, чем уменьшение и увеличение чисел.

Если количество сдвигов кратно числу 24, сдвиг дается легко. В противном случае приходится перераспределять все разряды:

function shift_down(big, places) {
    if (is_zero(big)) {
        return zero;
    }
    places = int(places);
    if (Number.isSafeInteger(places)) {
        if (places === 0) {
            return abs(big);
        }
        if (places < 0) {
            return shift_up(big, -places);
        }
        let skip = Math.floor(places / log2_radix);
        places -= skip * log2_radix;
        if (skip + 1 >= big.length) {
            return zero;
        }
        big = (
            skip > 0
            ? mint(zero.concat(big.slice(skip + 1)))
            : big
        );
        if (places === 0) {
            return big;
        }
        return mint(big.map(function (element, element_nr) {
            if (element_nr === sign) {
                return plus;
            }
            return ((radix - 1) & (
                (element >> places)
                | ((big[element_nr + 1] || 0) << (log2_radix - places))
            ));
        }));
    }
}