---
source_image: page_213.png
page_number: 213
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.69
tokens: 7496
characters: 1900
timestamp: 2025-12-24T09:59:23.165952
finish_reason: stop
---

```javascript
    jsc.string(8, jsc.character("A", "Z"))
])

my_little_array_specifier()    // [179, 21.228644298389554, "TJFJPLQA"]
my_little_array_specifier()    // [797, 57.05485427752137, "CWQDVXWY"]
my_little_array_specifier()    // [941, 91.98980208020657, "QVMGNVXK"]
my_little_array_specifier()    // [11, 87.07735128700733, "GXBSVLKJ"]

В противном случае он создает массив значений. Можно предоставить размерность массива или генератор, создающий целочисленные значения. Или предоставить значение или генератор значений. По умолчанию используются случайные простые числа.

let my_other_little_array_specifier = jsc.array(4);

my_other_little_array_specifier()    // [659, 383, 991, 821]
my_other_little_array_specifier()    // [479, 701, 47, 601]
my_other_little_array_specifier()    // [389, 271, 113, 263]
my_other_little_array_specifier()    // [251, 557, 547, 197]

Спецификатор string возвращает генератор, выдающий строки. По умолчанию строки составляются из ASCII-символов.

function string(...parameters) {
    const length = parameters.length;

    if (length === 0) {
        return string(integer(10), character());
    }
    return function () {
        let pieces = [];
        let parameter_nr = 0;
        let value;
        while (true) {
            value = resolve(parameters[parameter_nr]);
            parameter_nr += 1;
            if (value === undefined) {
                break;
            }
            if (
                Number.isSafeInteger(value)
                && value >= 0
                && parameters[parameter_nr] !== undefined
            ) {
                pieces = pieces.concat(
                    new Array(value).fill(parameters[parameter_nr]).map(resolve)
                );
                parameter_nr += 1;
            } else {
                pieces.push(String(value));
            }
        }
        return pieces.join("");
    };
}
```