---
source_image: page_214.png
page_number: 214
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.96
tokens: 7146
characters: 682
timestamp: 2025-12-24T09:25:17.460579
finish_reason: stop
---

001 <ul id = "atoms">
002   <li v-for = "atom in atoms">
003     {{ atom.message }}
004   </li>
005 </ul>

JavaScript-объект Vue, который создает объект Array и заполняет его 15 элементами, содержащими значение 0:

001 let atoms = new Vue({
002   el: "#atoms",
003   data: {
004     atoms: new Array(15).fill(0);
005   }
006 });

Я включил этот пример сюда только для того, чтобы показать: объединение нескольких фреймворков и библиотек облегчает написание кода и его поддержку в будущем.

Однако это не значит, что вы должны применять их в каждом отдельном проекте. Иногда проще написать код в обычной форме.

В ходе работы вы столкнетесь с кодом, использующим несколько библиотек.