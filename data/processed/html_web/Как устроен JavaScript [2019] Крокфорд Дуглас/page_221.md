---
source_image: page_221.png
page_number: 221
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.10
tokens: 7285
characters: 1405
timestamp: 2025-12-24T09:59:35.453115
finish_reason: stop
---

if (cases) {
    let the_case = cases[serial];
}

Если порядковый номер не наблюдался, регистрируется новый пример и добавляется к коллекции примеров. Порядковый номер добавляется к коллекции порядковых номеров. Количество отложенных примеров увеличивается.

    if (the_case === undefined) {
        value.serial = serial;
        cases[serial] = value;
        serials.push(serial);
        nr_pending += 1;
    } else {

Теперь существующий пример получает свой вердикт. Если у него совершенно неожиданно уже имеется результат, выдается исключение. У каждого примера должен быть только один результат.

    if (
        the_case.pass !== undefined
        || typeof value !== "boolean"
    ) {
        throw the_case;
    }

Если результат является булевым значением, пример обновляется и отправляется on_pass или on_fail:

    if (value === true) {
        the_case.pass = true;
        go("on_pass", the_case);
    } else {
        the_case.pass = false;
        go("on_fail", the_case);
    }

Этот пример больше не откладывается. Если все примеры были сгенерированы и дали результаты, нужно завершить работу.

    nr_pending -= 1;
    if (nr_pending <= 0 && all_started) {
        finish();
    }
}
return value;
}
let unique = 0;

Обработка каждого утверждения:

    the_claims.forEach(function (a_claim) {
        let at_most = nr_trials * 10;
        let case_nr = 0;
        let attempt_nr = 0;