---
source_image: page_587.png
page_number: 587
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.30
tokens: 11819
characters: 2117
timestamp: 2025-12-24T02:02:05.466512
finish_reason: stop
---

От обратных вызовов к будущим объектам и сопрограммам

Пример 18.10. Ад обратных вызовов в JavaScript: вложенные анонимные функции, называемые еще «пирамидой судьбы» (http://survivejs.com/common_problems/pyramid.html)

api_call1(request1, function (response1) {
    // шаг 1
    var request2 = step1(response1);
    api_call2(request2, function (response2) {
        // шаг 2
        var request3 = step2(response2);
        api_call3(request3, function (response3) {
            // шаг 3
            step3(response3);
        });
    });
});
};

В примере 18.10 api_call1, api_call2 и api_call3 — библиотечные функции, используемые для асинхронного получения результатов. Например, api_call1 могла бы обращаться к базе данных, а api_call2 получать данные от веб-службы. Все они принимают на входе функцию обратного вызова, которая в JavaScript зачастую является анонимной (в следующем ниже примере на Python эти функции названы stage1, stage2 и stage3). Что же касается step1, step2 и step3, то это обычные функции, с помощью которых приложение обрабатывает ответы, полученные функциями обратного вызова.

В примере 18.11 показано, как ад обратных вызовов выглядит в Python.

Пример 18.11. Ад обратных вызовов в Python: сцепленные обратные вызовы

def stage1(response1):
    request2 = step1(response1)
    api_call2(request2, stage2)

def stage2(response2):
    request3 = step2(response2)
    api_call3(request3, stage3)

def stage3(response3):
    step3(response3)

api_call1(request1, stage1)

Хотя этот код организован совсем не так, как в примере 18.10, делают они одно и то же, и код на JavaScript можно было бы построить точно так же (однако код на Python невозможно написать в стиле JavaScript из-за ограничений на лямбда-выражения).

Код, устроенный так, как в примере 18.10 или 18.11, трудно читать, но еще труднее писать: каждая функция делает свою часть работы, настраивает следующий обратный вызов и возвращает управление, чтобы цикл обработки событий мог продолжить работу. В этот момент весь локальный контекст теряется. При выполнении следующего обратного вызова (например, stage2) значение request2