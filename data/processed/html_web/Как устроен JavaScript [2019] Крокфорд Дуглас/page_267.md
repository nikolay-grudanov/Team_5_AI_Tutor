---
source_image: page_267.png
page_number: 267
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.45
tokens: 7198
characters: 1369
timestamp: 2025-12-24T10:00:40.135098
finish_reason: stop
---

the_import.class = "statement";
return the_import;
}

function parse_export(the_export) {
    the_export.zeroth = expression();
    the_export.class = "statement";
    return the_export;
}

Экспортируется одна функция parse. Она принимает генератор лексем и возвращает дерево. Нам не нужно создавать конструктор, поскольку parse никакого состояния между вызовами не сохраняет.

export default function parse(token_generator) {
    try {
        indentation = 0;
        loop = [];
        the_token_generator = token_generator;
        next_token = the_end;
        const program = {
            id: "",
            scope: Object.create(null)
        };
        now_function = program;
        advance();
        advance();
        let the_statements = [];
        while (token.id.startsWith("import ")) {
            at_indentation();
            prelude();
            the_statements.push(parse_import(prev_token));
        }
        the_statements = the_statements.concat(statements());
        if (token.id.startsWith("export")) {
            at_indentation();
            prelude();
            the_statements.push(parse_export(prev_token));
        }
        if (token !== the_end) {
            return error(token, "unexpected");
        }
        program.zeroth = the_statements;
        return program;
    } catch (ignore) {
        return the_error;
    }
};