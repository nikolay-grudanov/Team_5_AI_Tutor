---
source_image: page_277.png
page_number: 277
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.34
tokens: 7317
characters: 1515
timestamp: 2025-12-24T10:00:56.093794
finish_reason: stop
---

```
["": function (thing) {
    if (thing.wunth === undefined) {
        return array_literal(thing.zeroth);
    }
    return (
        "$NEO.get(" + expression(thing.zeroth)
        + ", " + expression(thing.wunth) + ")"
    );
},
"{": function (thing) {
    return record_literal(thing.zeroth);
},
"(": function (thing) {
    return (
        expression(thing.zeroth) + "("
        + thing.wunth.map(expression).join(", ") + ")"
    );
},
"[]": "[]",
"{}": "Object.create(null)",
"f": function (thing) {
    if (typeof thing.zeroth === "string") {
        return functino[thing.zeroth];
    }
    return "$NEO.stone(function (" + thing.zeroth.map(function (param) {
        if (param.id === "...") {
            return "..." + mangle(param.zeroth.id);
        }
        if (param.id === "|") {
            return (
                mangle(param.zeroth.id) + " = " + expression(param.wunth)
            );
        }
        return mangle(param.id);
    }).join(", ") + ") " + (
        Array.isArray(thing.wunth)
        ? block(thing.wunth)
        : "{return " + expression(thing.wunth) + ";}"
    ) + ")";
}
});
```

Здесь экспортируется функция генератора кода, которая принимает дерево и возвращает программу в исходном коде JavaScript.

export default $NEO.stone(function codegen(tree) {
    front_matter = [
        "import $NEO from \"/./neo.runtime.js\"\\n"
    ];
    indentation = 0;
    unique = Object.create(null);
    const bulk = statements(tree.zeroth);
    return front_matter.join("") + bulk;
});