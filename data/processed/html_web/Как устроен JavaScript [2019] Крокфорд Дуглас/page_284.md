---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.29
tokens: 7231
characters: 1417
timestamp: 2025-12-24T10:01:05.499899
finish_reason: stop
---

29.4 Как работает среда выполнения

    ? a
    : undefined
    )
    );
}
}

function record(zeroth, wunth) {
    const newness = Object.create(null);
    if (zeroth === undefined) {
        return newness;
    }
    if (Array.isArray(zeroth)) {
        if (wunth === undefined) {
            wunth = true;
        }
        zeroth.forEach(function (element, element_nr) {
            set(
                newness,
                element,
                (
                    Array.isArray(wunth)
                    ? wunth[element_nr]
                    : (
                        typeof wunth === "function"
                        ? wunth(element)
                        : wunth
                    )
                )
            );
        });
        return newness;
    }
    if (typeof zeroth === "object") {
        if (wunth === undefined) {
            return Object.assign(newness, zeroth);
        }
        if (typeof wunth === "object") {
            return Object.assign(newness, zeroth, wunth);
        }
        if (Array.isArray(wunth)) {
            wunth.forEach(function (key) {
                let value = zeroth[key];
                if (value !== undefined) {
                    newness[key] = value;
                }
            });
            return newness;
        }
    }
    return fail("record");
}

function text(zeroth, wunth, twoth) {
    if (typeof zeroth === "string") {