---
source_image: page_208.png
page_number: 208
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.88
tokens: 7357
characters: 1718
timestamp: 2025-12-24T09:59:04.207483
finish_reason: stop
---

23.7 Как работает тестирование

    if (!big_integer.is_zero(b)) {
        return a[0] + b[0];
    }
});

Я выстроил тесты вокруг тождественностей. Например, прибавление 1 к строке из n единичных битов будет иметь такой же результат, что и 2 ** n:

    jsc.claim("exp & mask", function (verdict, n) {
        return verdict(
            big_integer.eq(
                big_integer.add(big_integer.mask(n), big_integer.wun),
                big_integer.power(big_integer.two, n)
            )
        );
    }, [jsc.integer(100)]);

Здесь еще одно тождество, (1 << n) - 1, должно быть тождественно n единичным битам:

    jsc.claim("mask & shift_up", function (verdict, n) {
        return verdict(big_integer.eq(
            big_integer.sub(
                big_integer.shift_up(big_integer.wun, n),
                big_integer.wun
            ),
            big_integer.mask(n)
        ));
    }, [jsc.integer(0, 96)]);

Я сконструировал большой набор подобных тестов. Этот стиль тестирования дает мне гораздо больше уверенности, чем можно было бы получить от 3 + 4.

JSCheck

Далее показана реализация JSCheck. Наиболее интересные его составляющие — это спецификаторы, которые могут создавать тестовые данные. Большинство из них пригодны для компоновки интересными способами, поскольку спецификаторы передают значения через функцию resolve. Функция resolve возвращает свой аргумент, если он не является функцией:

    function resolve(value, ...rest) {

Функция resolve принимает значение. Если это значение — функция, она вызывается для создания возвращаемого значения. В противном случае функция возвращает значение:

    return (
        typeof value === "function"
        ? value(...rest)
        : value
    );