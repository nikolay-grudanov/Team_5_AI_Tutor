---
source_image: page_105.png
page_number: 105
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.89
tokens: 7172
characters: 1126
timestamp: 2025-12-24T09:56:06.167015
finish_reason: stop
---

return refinement[element];
    },
    container
)
);
Если значением для замены является функция, ее вызывают, чтобы получить это значение.

    if (typeof replacement === "function") {
        replacement = replacement(path, encoding);
    }

Если предоставлен объект кодировщика, вызывается одна из его функций. Если кодировщик представлен функцией, то выполняется ее вызов.

    replacement = (
        typeof encoder === "object"
        ? encoder[encoding]
        : encoder
    )(replacement, path, encoding);

Если значения для замены относятся к булеву типу, они преобразуются в строку.

    if (
        typeof replacement === "number"
        || typeof replacement === "boolean"
    ) {
        replacement = String(replacement);
    }

Если значение для замены — строка, выполняется ее подстановка. В противном случае символическая переменная остается неизменной.

    return (
        typeof replacement === "string"
        ? replacement
        : original
    );

Если что-то пойдет не так, символическая переменная будет оставлена в исходном состоянии.

    } catch (ignore) {
        return original;
    }
});