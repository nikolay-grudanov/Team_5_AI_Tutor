---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.19
tokens: 7501
characters: 2043
timestamp: 2025-12-24T09:55:49.630691
finish_reason: stop
---

7.9 Как работают массивы

// {"first": "Charcoal", "last": "Farkel"},
// {"first": "Fanny", "last": "Farkel"},
// {"first": "Frank", "last": "Farkel"},
// {"first": "Gar", "last": "Farkel"},
// {"first": "Mark", "last": "Farkel"},
// {"first": "Simon", "last": "Farkel"},
// {"first": "Sparkle", "last": "Farkel"}
// ]

Попурри

Метод concat получает два и более массива и объединяет их для создания нового массива:

let part_zero = ["unicorns", "rainbows"];
let part_wun = ["butterflies", "monsters"];
let whole = part_zero.concat(part_wun);
    // whole имеет значение ["unicorns", "rainbows", "butterflies", "monsters"]

Метод join получает массив, содержащий строковые значения и строку-разделитель. Он создает длинную строку, объединяющую все элементы. Если разделение не требуется, следует в качестве разделителя воспользоваться пустой строкой. Этот метод — антипод метода split, работающего со строками.

let string = whole.join(" & ");
    // string имеет значение "unicorns & rainbows & butterflies & monsters"

Метод reverse разворачивает элементы в массиве, чтобы они оказались в нем стоящими в обратном порядке. Этот метод разрушающий, как и функция sort.

whole.reverse();
    // whole имеет значение ["monsters", "butterflies", "rainbows", "unicorns"]

Метод slice способен создать копию массива или его части. Нулевой параметр определяет, с какого порядкового номера начинать. Первый параметр — это нулевой параметр плюс количество копируемых элементов. Если первый параметр не указан, будут скопированы все оставшиеся элементы.

let element_nr = whole.indexOf("butterflies");
let good_parts;
if (element_nr !== -1) {
    good_parts = whole.slice(element_nr);
}
    // good_parts имеет значение ["butterflies", "rainbows", "unicorns"]

Чистый и нечистый

Некоторые из методов работы с массивами относятся к чистым, не изменяющим введенные в них данные. Другие — нет. Некоторые из них должны быть чистыми, но таковыми не являются. Методы, которые не могут быть чистыми по своей природе, все же представляют определенную ценность.