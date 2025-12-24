---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.09
tokens: 7345
characters: 1804
timestamp: 2025-12-24T10:00:52.404428
finish_reason: stop
---

В языке Neo нет ничего булевоподобного. Есть места, где язык ожидает предоставления булевых значений, например условная часть инструкции if. Если Neo передается значение, не являющееся булевым, он должен дать сбой. Чтобы получить такое же поведение в JavaScript, может потребоваться заключить такие значения в функцию assert_boolean.

function assert_boolean(thing) {
    const string = expression(thing);
    return (
        (
            boolean_operator[thing.id] === true
            ||
            (
                thing.zeroth !== undefined
                && thing.zeroth.origin === undefined
                && boolean_operator[thing.zeroth.id]
            )
        )
        ? string
        : "$NEO.assert_boolean(" + string + ")"
    );
}

Массивы лексем-инструкций можно преобразовать в строку и заключить в блоки.

function statements(array) {
    const padding = begin();
    return array.map(function (statement) {
        return padding + statement_transform[statement.id](statement);
    }).join("");
}

function block(array) {
    indent();
    const string = statements(array);
    outdent();
    return "{" + string + begin() + "}";
}

Объект statement_transform содержит функции преобразований для всех инструкций. В большинстве инструкций нет ничего сложного. Сложность инструкции if заключается в существовании трех форм: без else, с else и с else if. Инструкция let — единственное место, где происходят изменения. Она должна работать с оператором [], который в левой части выполняет добавление, а в правой — извлечение и работает с левосторонними значениями (lvalue).

statement_transform = $NEO.stone({
    break: function (ignore) {
        return "break;";
    },
    call: function (thing) {
        return expression(thing.zeroth) + ";";
    },
    def: function (thing) {