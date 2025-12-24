---
source_image: page_099.png
page_number: 99
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.39
tokens: 6128
characters: 1407
timestamp: 2025-12-24T10:04:28.157595
finish_reason: stop
---

config.on.complete(1, args.responseArg);
};
}
realIO = Y.io;
Это стандартный код YUI, загружающий внешние модули, включая наш модуль login, который мы и будем тестировать. Код также содержит фабрику для создания поддельной инстанции Y.io, которая является YUI-оболочкой вокруг XMLHttpRequest. Этот объект гарантирует, что ему будут переданы корректные значения. Наконец, мы сохраняем ссылку на реальный экземпляр Y.io так, чтобы его можно было восстановить для других тестов. Сам код теста выглядит так:

var testCase = new Y.Test.Case({
    name: "test ajax login"
    , tearDown: function() {
        Y.io = realIO;
    }
    , testLogin : function () {
        var username = 'mark'
            , password = 'rox'
        ;
        Y.io = getFakeIO({
            url: '/login'
            , data: JSON.stringify({
                username: username
                , password: password
            })
            , method: 'POST'
            , responseArg: {
                status: 200
                , responseText: JSON.stringify({ loginOk: true })
            }
        });
        userLoggedIn = function(user) {
            Y.Assert.areEqual(user, username); };
        failedLogin = function() {
            Y.Assert.fail('Вход в систему успешно!'); };
        networkError = function() {
            Y.Assert.fail('Вход в систему успешно!'); };
        Y.one('#username').set('value', username);