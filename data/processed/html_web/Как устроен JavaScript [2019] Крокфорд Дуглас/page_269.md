---
source_image: page_269.png
page_number: 269
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.76
tokens: 7510
characters: 1941
timestamp: 2025-12-24T10:01:01.617632
finish_reason: stop
---

"arguments", "await", "break", "case", "catch", "class", "const",
"continue", "debugger", "default", "delete", "do", "else", "enum", "eval",
"export", "extends", "false", "finally", "for", "function", "if",
"implements", "import", "in", "Infinity", "instanceof", "interface", "let",
"NaN", "new", "null", "package", "private", "protected", "public", "return",
"static", "super", "switch", "this", "throw", "true", "try", "typeof",
"undefined", "var", "void", "while", "with", "yield"
]);

Объект primordial содержит всевозможные отображения из фундаментального пространства Neo в пространство JavaScript. Некоторые отображения направляются к среде выполнения Neo, а некоторые — к JavaScript.

const primordial = $NEO.stone({
    "abs": "$NEO.abs",
    "array": "$NEO.array",
    "array?": "Array.isArray",
    "bit and": "$NEO.bitand",
    "bit mask": "$NEO.bitmask",
    "bit or": "$NEO.bitor",
    "bit shift down": "$NEO.bitdown",
    "bit shift up": "$NEO.bitup",
    "bit xor": "$NEO.bitxor",
    "boolean?": "$NEO.boolean_",
    "char": "$NEO.char",
    "code": "$NEO.code",
    "false": "false",
    "fraction": "$NEO.fraction",
    "function?": "$NEO.function_",
    "integer": "$NEO.integer",
    "integer?": "$NEO.integer_",
    "length": "$NEO.length",
    "neg": "$NEO.neg",
    "not": "$NEO.not",
    "null": "undefined",
    "number": "$NEO.make",
    "number?": "$NEO.is_big_float",
    "record": "$NEO.record",
    "record?": "$NEO.record_",
    "stone": "$NEO.stone",
    "stone?": "Object.isFrozen",
    "text": "$NEO.text",
    "text?": "$NEO.text_",
    "true": "true"
});

В JavaScript пробельные символы играют куда более скромную роль, чем в Neo, поэтому можно создавать действительно уродливый код и JavaScript возражать не станет. Я думаю, что в мире слишком много безобразного. Когда есть возможность сделать что-то лучше, нужно так и делать, даже если никто этого не заметит.

let indentation;

function indent() {