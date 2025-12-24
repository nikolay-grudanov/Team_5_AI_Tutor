---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.26
tokens: 6183
characters: 1638
timestamp: 2025-12-24T10:04:29.813954
finish_reason: stop
---

ногого программирования (мы будем использовать модуль YUI Event Hub):

YUI().add('login', function(Y) {
    Y.one('#submitButton').on('click', logIn);
    function logIn(e) {
        var username = Y.one('#username').get('value')
            , password = Y.one('#password').get('value')
        ;
        eventHub.fire('logIn'
            , { username: username, password: password }
            , function(err, resp) {
                if (!err) {
                    if (resp.loginOk) {
                        userLoggedIn(username);
                    } else {
                        failedLogin(username);
                    }
                } else {
                    networkError(err);
                }
            });
    }
}, '1.0', { requires: [ 'node', 'EventHub' ] });

На этот раз код занял всего 18 строк, экономия кода составила 33%, что уже очень и очень неплохо. Но в дополнение к меньшему числу строк кода существенно упрощено его тестирование. Чтобы проиллюстрировать это, давайте проведем модульное тестирование. Детально модульное тестирование будет рассмотрено нами в главе 4, поэтому особо не обращайте внимание на синтаксис, если не знакомы с YUI Test. Начнем с Ajax-версии:

YUI().use('test', 'console', 'node-event-simulate'
    , 'login', function(Y) {
        // Фабрика для «подделки» Y.io
        var getFakeIO = function(args) {
            return function(url, config) {
                Y.Assert.areEqual(url, args.url);
                Y.Assert.areEqual(config.data, args.data);
                Y.Assert.areEqual(config.method, args.method);
                Y.Assert.isFunction(config.on.complete);
