---
source_image: page_225.png
page_number: 225
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.30
tokens: 7118
characters: 905
timestamp: 2025-12-24T09:59:29.154216
finish_reason: stop
---

```javascript
$;
//
// Определение групп:
// [1] Разрешенный тег комментария
// [2] Остальная часть строки

const rx_tag = /
    ^[a-z A-Z 0-9 _]+$
/;

export default Object.freeze(function ecomcon(source_string, tag_array) {
    const tag = Object.create(null);
    tag_array.forEach(
        function (string) {
            if (!rx_tag.test(string)) {
                throw new Error("ecomcon: " + string);
            }
            tag[string] = true;
        }
    );
    return source_string.split(rx_crlf).map(
        function (line) {
            const array = line.match(rx_ecomcon);
            return (
                Array.isArray(array)
                    ? (
                        tag[array[1]] === true
                            ? array[2] + "\n"
                            : ""
                    )
                    : line + "\n"
            );
        }
    ).join("");
});
```