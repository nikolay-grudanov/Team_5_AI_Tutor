---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.17
tokens: 6182
characters: 1573
timestamp: 2025-12-24T10:04:47.377417
finish_reason: stop
---

Сравните данное тестирование со стандартным подходом, когда используется инстанцированный объект DB с его прототипом функции addUser:

var DB = function(dbHandle) {
    this.handle = dbHandle;
};
DB.prototype.addUser = function(user) {
    var result = dbHandle.addRow('user', user);
    return {
        success: result.success
        , message: result.message
        , user: user
    };
};

Как ко всему этому получить доступ со стороны клиента? А вот:

transporter.sendMessage('addUser', user);

Глобальный или централизованный механизм передачи сообщений (в данном случае мы получаем к нему доступ посредством объекта transporter) отправит сообщение обратно серверу, используя Ajax или что-то подобное (способ передачи сообщения нас сейчас мало волнует, но на практике обычно используется технология Ajax, позволяющая сценариям JS отправлять информацию на сервер без перезагрузки страницы). Отправка сообщения о создании пользователя происходит, как правило, после создания или обновления объекта модели user на стороне клиента. Части, которые должны отслеживать запросы и ответы, а также код стороны сервера нуждаются в маршруте, по которому можно отправить сообщение глобальному объекту DB, обработать ответ и отправить ответ обратно клиенту.

Далее приведен тест для этого кода:

YUI().use('test', function(Y) {
    var addUserTests = new Y.Test.Case({
        name: 'add user'
        , addOne: function() {
            var user = { user_id: 'mark' }
            , dbHandle = { // заглушка БД
                addRow: function(user) {
                    return {
