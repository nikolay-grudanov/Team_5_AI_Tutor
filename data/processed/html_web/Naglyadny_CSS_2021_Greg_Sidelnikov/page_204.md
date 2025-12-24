---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.05
tokens: 7179
characters: 853
timestamp: 2025-12-24T09:25:01.806766
finish_reason: stop
---

Использование логических операторов SASS для создания класса цвета кнопки, который меняет цвет фона в зависимости от его ширины:

```scss
@mixin button-color($height, $width) {
    @if(($height < $width) and ($width >= 35px)) {
        background-color: blue;
    } @else {
        background-color: green;
    }
}
.button {
    @include button-color (20px, 30px)
}
```

Строки

В некоторых случаях можно добавить строки в допустимые значения CSS без кавычек.

Комбинирование обычных значений свойств CSS со строками SASS/SCSS:

```scss
p {
    font: 50px Ari + "al"; // Получается 50px Arial
}
```

Следующий пример, с другой стороны, приведет к ошибке компиляции:

```scss
p {
    font: "50px " + Arial; // Ошибка
}
```

Можно добавлять строки без двойных кавычек, если строка не содержит пробелов. Например, следующий пример не будет компилироваться.