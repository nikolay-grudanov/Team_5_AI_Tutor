---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.73
tokens: 7288
characters: 1005
timestamp: 2025-12-24T10:00:58.715805
finish_reason: stop
---

Как работает генерация кода

    ? argument(index)
    : argument
    )
    );
    if ($NEO.eq(candidate, undefined)) {
        stop = true;
    }
    return candidate;
});
while (true) {
    var processed = $NEO.array($arguments, prepare_arguments);
    if ($NEO.assert_boolean(stop)) {
        break;
    }
    result.push($function(...processed));
    index = $NEO.add(index, $1);
}
return result;
});

А затем:

import do: "example/do.neo"

var result: do(f+, [1, 2, 3], [5, 4, 3])
# result is [6, 6, 6]

let result: do(f/, 60, [1, 2, 3, 4, 5, 6])
# result is [60, 30, 20, 15, 12, 10]

что транспилируется в:

import $NEO from "./neo.runtime.js"
const $1 = $NEO.number("1");
const $2 = $NEO.number("2");
const $3 = $NEO.number("3");
const $5 = $NEO.number("5");
const $4 = $NEO.number("4");
const $60 = $NEO.number("60");
const $6 = $NEO.number("6");

import $do from "example/do.neo";
var result = $do($NEO.add, $60, [$1, $2, $3], [$5, $4, $3]);
result = $do($NEO.div, $60, [$1, $2, $3, $4, $5, $6]);