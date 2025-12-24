---
source_image: page_288.png
page_number: 288
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.01
tokens: 7164
characters: 914
timestamp: 2025-12-24T10:01:11.176544
finish_reason: stop
---

```javascript
(big_float.is_big_float(a) && big_float.is_big_float(b))
    ? big_float.add(a, b)
    : undefined
);
}

function sub(a, b) {
    return (
        (big_float.is_big_float(a) && big_float.is_big_float(b))
        ? big_float.sub(a, b)
        : undefined
    );
}

function mul(a, b) {
    return (
        (big_float.is_big_float(a) && big_float.is_big_float(b))
        ? big_float.mul(a, b)
        : undefined
    );
}

function div(a, b) {
    return (
        (big_float.is_big_float(a) && big_float.is_big_float(b))
        ? big_float.div(a, b)
        : undefined
    );
}

function max(a, b) {
    return (
        lt(b, a)
        ? a
        : b
    );
}

function min(a, b) {
    return (
        lt(a, b)
        ? a
        : b
    );
}

function abs(a) {
    return (
        big_float.is_big_float(a)
        ? big_float.abs(a)
        : undefined
    );
}

function fraction(a) {
```