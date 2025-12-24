---
source_image: page_276.png
page_number: 276
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.74
tokens: 7265
characters: 1163
timestamp: 2025-12-24T10:00:49.097694
finish_reason: stop
---

```javascript
let string = (
    "(" + padding + assert_boolean(thing.zeroth)
    + padding + "? " + expression(thing.wunth)
    + padding + ": " + expression(thing.twoth)
);
outdent();
return string + begin() + ")";
},
"/\"": function (thing) {
    return (
        "(" + assert_boolean(thing.zeroth)
        + " && " + assert_boolean(thing.wunth)
        + ")"
    );
},
"\\/": function (thing) {
    return (
        "(" + assert_boolean(thing.zeroth)
        + " || " + assert_boolean(thing.wunth)
        + ")"
    );
},
"=": "$NEO.eq",
"#": "$NEO.ne",
"<": "$NEO.lt",
">": "$NEO.gt",
"<=": "$NEO.le",
"~": "$NEO.cat",
"≈": "$NEO.cats",
"+": "$NEO.add",
"-": "$NEO.sub",
">>": "$NEO.max",
"<<": "$NEO.min",
"*": "$NEO.mul",
"/": "$NEO.div",
"|": function (thing) {
    return (
        "(function (_0) {"
        + "return (_0 === undefined) ? "
        + expression(thing.wunth) + " : _0);}("
        + expression(thing.zeroth) + ")"
    );
},
"...": function (thing) {
    return "..." + expression(thing.zeroth);
},
".": function (thing) {
    return (
        "$NEO.get(" + expression(thing.zeroth)
        + ", \\" + thing.wunth.id + "\")"
    );
},
```