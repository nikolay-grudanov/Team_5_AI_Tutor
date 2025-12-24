---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.70
tokens: 7213
characters: 1335
timestamp: 2025-12-24T09:59:31.985578
finish_reason: stop
---

23.19 Как работает тестирование

    : configuration.nr_trials
    );
    function go(on, report) {
Вызов функции обратного вызова:

        try {
            return configuration[on](report);
        } catch (ignore) {}
    }

Функция check проверяет все попытки. Результаты предоставляются функциям обратного вызова:

    let cases = {};
    let all_started = false;
    let nr_pending = 0;
    let serials = [];
    let timeout_id;

    function finish() {
        if (timeout_id) {
            clearTimeout(timeout_id);
        }
        const {
            losses,
            summary,
            report
        } = crunch(
            (
                configuration.detail === undefined
                ? 3
                : configuration.detail
            ),
            cases,
            serials
        );
        losses.forEach(function (the_case) {
            go("on_lost", the_case);
        });
        go("on_result", summary);
        go("on_report", report);
        cases = undefined;
    }

    function register(serial, value) {

Эта функция используется функцией claim для регистрации нового примера, а также самим примером для вынесения вердикта. Эти два применения сопоставляются с помощью порядкового номера.

Если объект cases утрачен, все прибывшие позже потерянные результаты должны быть проигнорированы: