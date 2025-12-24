---
source_image: page_101.png
page_number: 101
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.41
tokens: 6187
characters: 1666
timestamp: 2025-12-24T10:04:34.031068
finish_reason: stop
---

Здесь мы видим тот же шаблон и подобную фабрику для имитации обработчика событий. Несмотря на это, данный код более чист и прост, небольшая сложность возникает при сравнении двух объектов на равенство, поскольку YUI не предоставляет стандартного метода сравнения объектов.

Теперь рассмотрим фактический код теста:

    var testCase = new Y.Test.Case({
        name: "test eh login"
        , testLogin : function () {
            var username = 'mark'
            , password = 'rox'
            ;
            eventHub = getFakeEH({
                event: 'logIn'
                , data: {
                    username: username
                    , password: password
                }
                , responseArg: { loginOk: true }
            });
            userLoggedIn = function(user) {
                Y.Assert.areEqual(user, username); };
            failedLogin = function() {
                Y.Assert.fail('login should have succeeded!'); };
            networkError = function() {
                Y.Assert.fail('login should have succeeded!'); };
                Y.one('#username').set('value', username);
                Y.one('#password').set('value', password);
                Y.one('#submitButton').simulate('click');
            }
        });
    });

Данный код по своей сути очень похож на рассмотренный нами ранее для Ajax-версии. Мы получаем сымитированную версию концентратора событий, заполняем HTML-элементы и нажимаем кнопку Submit для имитации входа в систему.

Однако этот пример иллюстрирует, что в случае с событийно-ориентированным программированием размер кода (как основного, так и кода тестирования) существенно меньше. Например,