---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.37
tokens: 7362
characters: 1673
timestamp: 2025-12-24T09:59:18.213726
finish_reason: stop
---

result[text()] = gen();
    i += 1;
}
    return result;
}
    if (value === undefined) {
        if (keys && typeof keys === "object") {
            Object.keys(subject).forEach(function (key) {
                result[key] = resolve(keys[key]);
            });
            return result;
        }
    } else {
        const values = resolve(value);
        if (Array.isArray(keys)) {
            keys.forEach(function (key, key_nr) {
                result[key] = resolve(
                    Array.isArray(values)
                        ? values[key_nr % values.length]
                        : value
                ), key_nr);
            });
            return result;
        }
    }
};

Если ему передается массив имен и значение, он создает объект, используя эти имена в качестве имен свойств и задавая этим свойствам значения. Например, можно выдать массив, содержащий от трех до шести имен, где имена состоят из четырех букв в нижнем регистре, а значения являются булевыми:

let my_little_constructor = jsc.object(
    jsc.array(
        jsc.integer(3, 6),
        jsc.string(4, jsc.character("a", "z"))
    ),
    jsc.boolean()
);

my_little_constructor()
// {"hiyt": false, "rodf": true, "bxf": false, "ygat": false, "hwqe": false}
my_little_constructor()
// {"hwbh": true, "ndjt": false, "chsn": true, "fdag": true, "hvme": true}
my_little_constructor()
// {"qedx": false, "uoyp": true, "ewes": true}
my_little_constructor()
// {"igko": true, "txem": true, "yadl": false, "avwz": true}

Если передан объект, создается объект, имеющий те же имена свойств:

let my_little_other_constructor = jsc.object({
    left: jsc.integer(640),
    top: jsc.integer(480),