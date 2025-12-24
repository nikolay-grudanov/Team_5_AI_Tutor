---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.89
tokens: 7240
characters: 1060
timestamp: 2025-12-24T09:59:16.485960
finish_reason: stop
---

23.17 Как работает тестирование

lost: (
    nr_lost
    ? ", " + nr_lost + " lost"
    : ""
)
}
if (detail >= 2) {
    Object.keys(
        class_pass
    ).sort().forEach(
        generate_class
    );
    report += lines;
}
total_fail += nr_fail;
total_lost += nr_lost;
total_pass += nr_pass;
}
if (!next_case) {
    break;
}
nr_class = 0;
nr_fail = 0;
nr_lost = 0;
nr_pass = 0;
class_pass = {};
class_fail = {};
class_lost = {};
lines = "";
the_case = next_case;
now_claim = the_case.claim;
the_class = the_case.classification;
if (the_class && typeof class_pass[the_class] !== "number") {
    class_pass[the_class] = 0;
    class_fail[the_class] = 0;
    class_lost[the_class] = 0;
    nr_class += 1;
}
if (the_case.pass === true) {
    if (the_class) {
        class_pass[the_class] += 1;
    }
    if (detail >= 4) {
        generate_line("Pass", 4);
    }
    nr_pass += 1;
} else if (the_case.pass === false) {
    if (the_class) {
        class_fail[the_class] += 1;
    }
    generate_line("FAIL", 2);
    nr_fail += 1;
} else {
    if (the_class) {