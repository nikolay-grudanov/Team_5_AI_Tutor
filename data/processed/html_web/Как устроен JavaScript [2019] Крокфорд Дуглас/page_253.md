---
source_image: page_253.png
page_number: 253
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.63
tokens: 7268
characters: 1445
timestamp: 2025-12-24T10:00:17.748111
finish_reason: stop
---

same_line();
}
advance("]\"");
return the_bracket;
}

Парсер многоточия ellipsis укомплектован не так, как другие парсеры суффиксных операторов, поскольку присутствие данного суффикса разрешено только в трех местах: в списках параметров, списках аргументов и литералах массивов. В других местах он запрещен, поэтому рассматривается как особый случай.

function ellipsis(left) {
    if (token.id === "...") {
        const the_ellipsis = token;
        same_line();
        advance("...");
        the_ellipsis.zeroth = left;
        return the_ellipsis;
    }
    return left;
}

Парсер вызова () проводит синтаксический разбор вызовов функций. Он вызывает для каждого аргумента argument_expression. В вызове в открытой форме аргументы перечисляются вертикально, без применения запятых.

function parse_invocation(left, the_paren) {

// вызов функции:
//   выражение
//   выражение...

    const args = [];
    if (token.id === ")\"") {
        same_line();
    } else {
        const open = is_line_break();
        if (open) {
            indent();
        }
        while (true) {
            line_check(open);
            args.push(ellipsis(argument_expression()));
            if (token.id === ")\" || token === the_end) {
                break;
            }
            if (!open) {
                same_line();
                advance(",");
            }
        }
        if (open) {
            outdent();
            at_indentation();