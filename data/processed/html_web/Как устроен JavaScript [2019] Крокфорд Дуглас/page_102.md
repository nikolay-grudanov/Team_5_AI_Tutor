---
source_image: page_102.png
page_number: 102
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.55
tokens: 7289
characters: 1271
timestamp: 2025-12-24T09:56:09.340748
finish_reason: stop
---

9.10 Как работают строки

Функция entityify делает текст безопасным для вставки его в HTML:

function entityify(text) {
    return text.replace(
        /&/g,
        "&amp;"
    ).replace(
        /</g,
        "&lt;"
    ).replace(
        />/g,
        "&gt;"
    ).replace(
        /\//g,
        "&bsol;"
    ).replace(
        /"/g,
        "&quot;"
    );
}

Теперь заполним шаблон опасными данными:

const template = "<p>Lucky {name.first} {name.last} won ${amount}.</p>";

const person = {
    first: "Da5id",
    last: "<script src=enemy.evil/pwn.js/>"
};

// Теперь вызовем функцию fulfill.

fulfill(
    template,
    {
        name: person,
        amount: 10
    },
    entityify
)
// "<p>Lucky Da5id &lt;script src=enemy.evil/pwn.js/&gt; won $10.</p>"

Кодировщик entityify сделал потенциально вредоносный тег сценария безопасным для HTML.

А теперь посмотрим на код, который я использовал для подготовки оглавления книги, которую вы сейчас читаете!

Оглавление представлено в виде JSON-текста. В шаблонах имеются литералы скобок, но их наличие не вызывает никаких проблем. Здесь показаны вложенные вызовы функции fulfill, что позволяет избавиться от лексической сложности вложенных шаблонных строк:

const chapter_names = [
    "Сначала прочитайте меня!",