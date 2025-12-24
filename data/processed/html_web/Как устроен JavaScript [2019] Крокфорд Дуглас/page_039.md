---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.59
tokens: 7415
characters: 1816
timestamp: 2025-12-24T09:54:52.846982
finish_reason: stop
---

Чтобы улучшить прогнозы, сначала обрабатаем делитель функцией mint. Сдвиг влево выполняется до тех пор, пока его самый старший разряд не станет 1. На ту же величину выполняется сдвиг влево делимого. Описание алгоритма Algorithm 4.3.1D можно найти в книге The Art of Computer Programming.

Для определения количества сдвигов находим количество лидирующих 0. Функция clz32 выполняет вычисление в поле из 32 разрядов. Нас также интересует поле из 24 разрядов, поэтому вычитаем 8:

    let shift = Math.clz32(last(divisor)) - 8;

    dividend = shift_up(dividend, shift);
    divisor = shift_up(divisor, shift);
    let place = dividend.length - divisor.length;
    let dividend_prefix = last(dividend);
    let divisor_prefix = last(divisor);
    if (dividend_prefix < divisor_prefix) {
        dividend_prefix = (dividend_prefix * radix) + next_to_last(dividend);
    } else {
        place += 1;
    }
    divisor = shift_up(divisor, (place - 1) * 24);
    let quotient = new Array(place + 1).fill(0);
    quotient[sign] = plus;
    while (true) {

Оценка не будет слишком маленькой, но может оказаться слишком большой. Если она слишком высока, вычитание из делимого произведения оценки и делителя дает отрицательный результат. Когда это происходит, нужно уменьшить оценку и попробовать еще раз:

    let estimated = Math.floor(dividend_prefix / divisor_prefix);
    if (estimated > 0) {
        while (true) {
            let trial = sub(dividend, mul(divisor, [plus, estimated]));
            if (!is_negative(trial)) {
                dividend = trial;
                break;
            }
            estimated -= 1;
        }
    }

Правильная оценка сохраняется в quotient. Если это был последний разряд, идем дальше:

    quotient[place] = estimated;
    place -= 1;
    if (place === 0) {
        break;
    }