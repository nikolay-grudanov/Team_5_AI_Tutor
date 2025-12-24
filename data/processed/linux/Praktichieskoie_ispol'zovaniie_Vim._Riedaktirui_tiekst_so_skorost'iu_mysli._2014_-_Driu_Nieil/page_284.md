---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.31
tokens: 5551
characters: 1434
timestamp: 2025-12-24T04:15:29.367179
finish_reason: stop
---

Рецепт 92. Повторение предыдущей команды подстановки

Повторение команды подстановки в строке ко всему файлу

Допустим, что мы только что выполнили следующую команду, воздействующую на текущую строку:

⇒ :s/target/replacement/g

А после этого заметили ошибку: мы забыли добавить префикс %. Но нет причин для расстройства. Мы можем повторить команду и применить ее ко всему файлу, просто нажав g& (см.: h g& i http://vimdoc.sourceforge.net/htmldoc/change.html#g&), что эквивалентно следующей команде:

⇒ :%s//~/&

Она расшифровывается как «повторить последнюю команду подстановки с теми же флагами, с той же строкой замены и с текущим шаблоном поиска, но использовать диапазон %. Другими словами: применить последнюю команду подстановки ко всему файлу.

В следующий раз, когда вы поймете себя на желании добавить префикс % к команде подстановки из истории команд, попробуйте просто нажать клавиши g&.

Изменение диапазона в команде подстановки

В качестве примера возьмем следующий код:

substitution/mixin.js
http://media.pragprog.com/titles/dnvim/code/substitution/mixin.js

mixin = {
    applyName: function(config) {
        return Factory(config, this.getName());
    },
}

Допустим, что его потребовалось дополнить, как показано ниже:

mixin = {
    applyName: function(config) {
        return Factory(config, this.getName());
    },
    applyNumber: function(config) {
        return Factory(config, this.getNumber());
    },
}