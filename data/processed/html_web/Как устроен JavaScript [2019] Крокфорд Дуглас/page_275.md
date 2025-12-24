---
source_image: page_275.png
page_number: 275
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.80
tokens: 7320
characters: 1351
timestamp: 2025-12-24T10:00:56.079363
finish_reason: stop
---

```javascript
if (thing.zeroth.id === "[") {
    return (
        "$NEO.set(" + expression(thing.zeroth.zeroth)
        + ", " + expression(thing.zeroth.wunth)
        + ", " + right + ");"
    );
}
return expression(thing.zeroth) + " = " + right + ";";
},
loop: function (thing) {
    return "while (true) " + block(thing.zeroth);
},
return: function (thing) {
    return "return " + expression(thing.zeroth) + ";";
},
var: function (thing) {
    return "var " + expression(thing.zeroth) + (
        thing.wunth === undefined
        ? ";"
        : " = " + expression(thing.wunth) + ";"
    );
});
});

Указатель на функцию — это встроенная функция, доступ к которой можно получить, поместив перед оператором префикс f.

const functino = $NEO.stone({
    "?": "$NEO.ternary",
    "|": "$NEO.default",
    "/\\": "$NEO.and",
    "\\/": "$NEO.or",
    "=": "$NEO.eq",
    "#": "$NEO.ne",
    "<": "$NEO.lt",
    ">": "$NEO.gt",
    "<=": "$NEO.le",
    "~": "$NEO.cat",
    "~": "$NEO.cats",
    "+": "$NEO.add",
    "-": "$NEO.sub",
    ">>": "$NEO.max",
    "<<": "$NEO.min",
    "*": "$NEO.mul",
    "/": "$NEO.div",
    "[": "$NEO.get",
    "(": "$NEO.resolve"
});

Объект operator_transform содержит все преобразования операторов.

operator_transform = $NEO.stone({
    "?": function (thing) {
        indent();
        let padding = begin();
```