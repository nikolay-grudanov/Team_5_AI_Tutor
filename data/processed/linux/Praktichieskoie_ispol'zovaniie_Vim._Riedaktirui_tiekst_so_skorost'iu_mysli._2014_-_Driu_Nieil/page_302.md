---
source_image: page_302.png
page_number: 302
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.13
tokens: 5595
characters: 1554
timestamp: 2025-12-24T04:15:55.600785
finish_reason: stop
---

Рецепт 99. Выборка комментариев TODO в регистр

function regex_for_depth(depth) { /* implementation */ }
},
"´": function inlineCode( text ) {
var m = text.match( /(`+)(([\s\S]*?)\1)/ );
if ( m && m[2] )
    return [ m[1].length + m[2].length ];
else {
    // TODO: No matching end code found - warn!
    return [ 1, "´" ];
}
}

Допустим, что нам требуется собрать все комментарии TODO в одном месте. Вывести их все можно одной командой:

⇒ :g/TODO
    // TODO: Cache this regexp for certain depths.
    // TODO: No matching end code found - warn!

Не забывайте, что команда :print используется командой :global по умолчанию, если поле [cmd] оставить пустым. Она просто выведет все строки, содержащие слово «TODO». Впрочем, это не самое удачное решение, потому что сообщения исчезнут, как только будет выполнена другая команда.

Можно поступить иначе: скопировать каждую строку со словом «TODO» в регистр, а затем вставить содержимое этого регистра в другой файл и сохранить для последующего использования.

В примере ниже мы будем использовать регистр a. Прежде всего его следует очистить командой qaq, где qa предписывает редактору Vim начать запись макроса в регистр a, а q останавливает запись. В процессе записи макроса ничего не вводилось, поэтому в результате регистр очищается. Убедиться в этом можно с помощью команды

⇒ :reg a
- - - Registers - - -
"a

Теперь можно приступать к копированию комментариев TODO в регистр:

⇒ :g/TODO/yank A
⇒ :reg a
"a // TODO: Cache this regexp for certain depths.
    // TODO: No matching end code found - warn!