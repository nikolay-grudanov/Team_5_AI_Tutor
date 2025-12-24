---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.09
tokens: 6171
characters: 1728
timestamp: 2025-12-24T10:04:29.603980
finish_reason: stop
---

ботчиков писать небольшие блоки кода с минимальными зависимостями. Вся функциональность, выходящая за пределы «компетенции» какого-либо модуля, предоставляется ему в виде сервиса вместо того, чтобы использовать зависимости. Такая архитектура предполагает наличие вызовов функций только к концентратору событий или к методам, локальным для объекта или модуля.

Давайте взглянем на несколько классических вариантов реализации входа в систему. Ниже представлен стандартный вход в систему, использующий Ajax и платформу YUI:

YUI().add('login', function(Y) {
    Y.one('#submitButton').on('click', logIn);
    function logIn(e) {
        var username = Y.one('#username').get('value')
            , password = Y.one('#password').get('value')
            , cfg = {
                data: JSON.stringify(
                    {username: username, password: password}
                )
                , method: 'POST'
                , on: {
                    complete: function(tid, resp, args) {
                        if (resp.status === 200) {
                            var response = JSON.parse(resp.responseText);
                            if (response.loginOk) {
                                userLoggedIn(username);
                            } else {
                                failedLogin(username);
                            }
                        } else {
                            networkError(resp);
                        }
                    }
                }
            }
        request = Y.io('/login', cfg)
    }
}, '1.0', { requires: [ 'node', 'io-base' ] });

27 строк кода, обрабатывающего вход в систему, — не очень плохо. Но давайте рассмотрим эквивалентное решение на основе событий-