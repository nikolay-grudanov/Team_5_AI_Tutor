---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.72
tokens: 7364
characters: 1774
timestamp: 2025-12-24T09:55:20.395890
finish_reason: stop
---

Сложение и вычитание реализуются весьма просто. Если знаменатели равны, можно складывать или вычитать числители. В противном случае дополнительно выполняются два умножения, сложение и еще одно умножение, поскольку:

\[
(a / b) + (c / d) = ((a * d) + (b * c)) / (b * d)
\]

Схожесть сложения и вычитания позволила мне создать функцию, выполняющую функции add и sub:

```javascript
function conform_op(op) {
    return function (a, b) {
        try {
            if (big_integer.eq(a.denominator, b.denominator)) {
                return make(
                    op(a.numerator, b.numerator),
                    a.denominator
                );
            }
            return normalize(make(
                op(
                    big_integer.mul(a.numerator, b.denominator),
                    big_integer.mul(b.numerator, a.denominator)
                ),
                big_integer.mul(a.denominator, b.denominator)
            ));
        } catch (ignore) {
        }
    };
}
const add = conform_op(big_integer.add);
const sub = conform_op(big_integer.sub);
```

Рациональное число можно увеличить на единицу, добавив знаменатель к числителю.

```javascript
function inc(a) {
    return make(
        big_integer.add(a.numerator, a.denominator),
        a.denominator
    );
}

function dec(a) {
    return make(
        big_integer.sub(a.numerator, a.denominator),
        a.denominator
    );
}
```

Умножение также не вызывает затруднений. Мы просто перемножаем числители и знаменатели. Деление представляется тем же умножением, но с инвертированным вторым аргументом. В системе рациональных чисел выполнять деление в столбик практически не приходится. Мы просто увеличиваем делитель:

```javascript
function mul(multiplicand, multiplier) {
    return make(
```