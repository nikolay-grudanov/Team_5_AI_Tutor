---
source_image: page_272.png
page_number: 272
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.86
tokens: 7285
characters: 1485
timestamp: 2025-12-24T10:00:47.009496
finish_reason: stop
---

28.4 Как работает генерация кода

    : mangle(thing.id)
    );
}
return op(thing);
}

Эта функция создает массив литералов.

function array_literal(array) {
    return "[" + array.map(function (element) {
        return (
            Array.isArray(element)
            ? array_literal(element)
            : expression(element)
        );
    }).join(", ") + "]";
}

Из литералов записей Neo получаются объекты без прототипов. Пустые записи создаются с помощью Object.create(null). Поля создаются путем присваивания. Присваивания заключаются в тут же вызываемое функциональное выражение. Из {[foo bear]: 12.3, two part} получается:

(function (o) {
    $NEO.set(o, foo_bear, $12_3);
    o["two part"] = two_part;
})(Object.create(null)))

Имена переменных в литералах записей коверкаются, а имена полей — нет.

function record_literal(array) {
    indent();
    const padding = begin();
    const string = "(function (o) {" + array.map(function (element) {
        return padding + (
            typeof element.zeroth === "string"
            ?
            "o["
            + JSON.stringify(element.zeroth)
            + "] = "
            + expression(element.wunth)
            + ";"
            )
            :
            "$NEO.set(o, "
            + expression(element.zeroth)
            + ", "
            + expression(element.wunth)
            + ");"
        )
    }).join("") + padding + "return o;";
    outdent();
    return string + begin() + "}(Object.create(null)))";
}