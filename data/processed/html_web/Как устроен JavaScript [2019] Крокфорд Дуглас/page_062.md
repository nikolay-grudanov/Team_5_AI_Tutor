---
source_image: page_062.png
page_number: 62
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.52
tokens: 7312
characters: 1376
timestamp: 2025-12-24T09:55:20.409888
finish_reason: stop
---

5.5 Как работают большие рациональные числа

любое конечное число JavaScript и превращает его в рациональное без дополнительных потерь.

const number_pattern = /
    ^
    ( -? )
    (?:
        ( \d+ )
        (?:
            (?:
                \u0020 ( \d+ )
            )?
            \/
            ( \d+ )
        |
        (?: 
            \. ( \d* )
        )?
        (?: 
            e ( -? \d+ )
        )?
        )
    |
    \. (\d+)
    )
    $
/;

function make(numerator, denominator) {

Если получены два аргумента, то оба будут преобразованы в большие целые числа. Возвращаемым значением станет объект, содержащий числитель и знаменатель.

При вызове с одним аргументом будет сделана попытка его осмысления. Если аргумент имеет строковое значение, будет предпринята попытка его парсинга в качестве смешанной дроби или десятичного литерала. В противном случае предполагается, что недостающим аргументом была единица.

if (denominator !== undefined) {

Создание рационального числа из числителя и знаменателя — можно передать функции большие целые числа, простые целые числа или строки.

    numerator = big_integer.make(numerator);

Если числитель равен нулю, то знаменатель не нужен.

    if (big_integer.zero === numerator) {
        return zero;
    }
    denominator = big_integer.make(denominator);
    if (
        !big_integer.is_big_integer(numerator)