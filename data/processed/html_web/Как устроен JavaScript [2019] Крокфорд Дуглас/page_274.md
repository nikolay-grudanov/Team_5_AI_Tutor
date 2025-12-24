---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.89
tokens: 7294
characters: 1463
timestamp: 2025-12-24T10:00:47.336462
finish_reason: stop
---

```javascript
return (
    "var " + expression(thing.zeroth)
    + " = " + expression(thing.wunth) + ";"
);
},
export: function (thing) {
    const exportation = expression(thing.zeroth);
    return "export default " + (
        exportation.startsWith("$NEO.stone(")
        ? exportation
        : "$NEO.stone(" + exportation + ")"
    ) + ";";
},
fail: function () {
    return "throw $NEO.fail(\"fail\");";
},
if: function if_statement(thing) {
    return (
        "if (" +
        assert_boolean(thing.zeroth) +
        ") "
        + block(thing.wunth)
        + (
            thing.twoth === undefined
            ? ""
            : " else " + (
                thing.twoth.id === "if"
                ? if_statement(thing.twoth)
                : block(thing.twoth)
            )
        )
    );
},
import: function (thing) {
    return (
        "import " + expression(thing.zeroth)
        + " from " + expression(thing.wunth) + ";"
    );
},
let: function (thing) {
    const right = (
        thing.wunth.id === "["
        ? expression(thing.wunth.zeroth) + ".pop();"
        : expression(thing.wunth)
    );
    if (thing.zeroth.id === "[") {
        return expression(thing.zeroth.zeroth) + ".push(" + right + ");";
    }
    if (thing.zeroth.id === ".") {
        return (
            "$NEO.set(" + expression(thing.zeroth.zeroth)
            + ", " + JSON.stringify(thing.zeroth.wunth.id)
            + ", " + right + ");"
        );
    }
}
```