---
source_image: page_243.png
page_number: 243
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.14
tokens: 7331
characters: 1684
timestamp: 2025-12-24T10:00:01.307790
finish_reason: stop
---

Фабрика разбиения на лексемы выставляется на экспорт.

export default Object.freeze(function tokenize(source, comment = false) {

tokenize принимает исходный код и создает из него массив объектов-лексем. Если исходный код source не является массивом, он разбивается на строки по признаку присутствия символов возврата каретки и перевода строки. Если comment имеет значение true, то комментарий включается в качестве объекта-лексемы. Парсеру комментариев не нужны, а вот инструментам для работы с программными средствами они могут понадобиться.

    const lines = (
        Array.isArray(source)
        ? source
        : source.split(rx_crlf)
    );
    let line_nr = 0;
    let line = lines[0];
    rx_token.lastIndex = 0;

Фабрика возвращает генератор, который разбивает строки на объекты-лексемы. Эти объекты состоят из идентификатора, координат и другой информации. Пробельные символы на лексемы не разбиваются.

При каждом вызове генератор лексем производит очередную лексему.

    return function token_generator() {
        if (line === undefined) {
            return;
        }
        let column_nr = rx_token.lastIndex;
        if (column_nr >= line.length) {
            rx_token.lastIndex = 0;
            line_nr += 1;
            line = lines[line_nr];
            return (
                line === undefined
                ? undefined
                : token_generator()
            );
        }
        let captives = rx_token.exec(line);

Соответствие не найдено.

        if (!captives) {
            return {
                id: "(error)",
                line_nr,
                column_nr,
                string: line.slice(column_nr)
            };
        }