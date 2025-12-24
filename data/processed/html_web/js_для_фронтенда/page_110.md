---
source_image: page_110.png
page_number: 110
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.14
tokens: 6143
characters: 1462
timestamp: 2025-12-24T10:04:43.955546
finish_reason: stop
---

var eventHub = Y.Mock();
    , addUserTests = new Y.Test.Case({
        name: 'add user'
        , addOne: function() {
            var user = { user_id: 'mark' }
            , dbHandle = { // заглушка БД
                addRow: function(user) {
                    return { user: user
                        , success: true
                        , message: 'ok' };
                }
            }
            ;
            DB(eventHub, dbHandle); // тестовые версии
            Y.Mock.expect(eventHub, 'fire',
                [
                    'USER_CREATED'
                    , { success: true: message: 'ok', user: user }
                ]
            );
            addUser(user);
            Y.Mock.verify(eventHub);
        });
        Y.Test.Runner.add(addUserTests);
        Y.Test.Runner.run();
    });
В этом случае для тестирования функции addUser мы используем оба приема тестирования: и использование имитаций — mock (для концентратора событий), и использование заглушек — stub (для дескриптора БД). Событие fire, как ожидается, вызовет на объекте eventHub функцию addUser с соответствующими аргументами. Функция addRow объекта-заглушки DB просто сообщает, что создание пользователя прошло успешно. Оба данных объекта (концентратор событий и дескриптор БД) вводятся в объект DB для тестирования.

В результате всего этого простого тестирования мы можем убедиться, что функция addUser генерирует надлежащее событие с надлежащими аргументами.