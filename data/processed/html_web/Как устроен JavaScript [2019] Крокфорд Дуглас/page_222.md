---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.23
tokens: 7367
characters: 1672
timestamp: 2025-12-24T09:59:38.122618
finish_reason: stop
---

23.21    Как работает тестирование

Проход по генерации и тестированию примеров:

    while (case_nr < nr_trials && attempt_nr < at_most) {
        if (a_claim(register, unique) !== reject) {
            case_nr += 1;
            unique += 1;
        }
        attempt_nr += 1;
    });
};

Были вызваны все предикаты примера:

    all_started = true;

Если все примеры возвратили вердикты, создание отчета:

    if (nr_pending <= 0) {
        finish();
    }

В противном случае запуск таймера:

    } else if (configuration.time_limit !== undefined) {
        timeout_id = setTimeout(finish, configuration.time_limit);
    }
}

Функция claim используется для подачи каждого утверждения. Все утверждения проверяются сразу при вызове функции check. Утверждение состоит:

• из описательного имени, отображаемого в отчете;
• функции-предиката, применяющей утверждение и возвращающей true, если оно соблюдается;
• функции с массивом сигнатур, определяющей типы и значения для функции-предиката;
• необязательной функции-классификатора, принимающей значения, создаваемые сигнатурой, и возвращающей строку для классификации попыток, или undefined, если предикату не нужно давать данный набор сгенерированных аргументов:

function claim(name, predicate, signature, classifier) {

Функция размещается в наборе всех утверждений:

    if (!Array.isArray(signature)) {
        signature = [signature];
    }

    function the_claim(register, serial) {
        let args = signature.map(resolve);
        let classification = "";

Если была предоставлена функция-классификатор, она используется для получения классификации. Если классификация не является строкой, пример отбрасывается: