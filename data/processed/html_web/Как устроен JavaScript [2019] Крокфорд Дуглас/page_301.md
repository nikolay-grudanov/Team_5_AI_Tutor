---
source_image: page_301.png
page_number: 301
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.92
tokens: 7439
characters: 1504
timestamp: 2025-12-24T10:01:16.356123
finish_reason: stop
---

к результату обработанное включение. Для защиты от бесконечных рекурсий значение max_depth уменьшается:

return include(
    junior_assistant_minion,
    inclusion,
    get_inclusion,
    max_depth - 1
);
}

Таково ближайшее окружение. Теперь вернемся к include. Если происходит выход за пределы заданной нами глубины, вызывается callback:

if (max_depth <= 0) {
    callback(string);
} else {

Функция include создает три функции ближайшего окружения и вызывает основную функцию minion:

minion();
}
});

Благодарности

Я хочу поблагодарить Эдвина Аоки (Edwin Aoki), Владимира Баквански (Vladimir Bacvanski), Леонардо Боначчи (Leonardo Bonacci), Джорджа Буля (George Boole), Денниса Клайна (Dennis Cline), Роландо Димаандала (Rolando Dimaandal), Билла Франца (Bill Franz), Луи Готтлиба (Louis Gottlieb), Боба Хаблутцеля (Bob Hablutzel), Грейс Мюррей Хоппер (Grace Murray Hopper), Мэтью Джонсона (Matthew Johnson), Алана Карпа (Alan Karp), Готтрида Лейбница (Gottried Leibniz), Хокона Виума Ли (Håkon Wium Lie), Линдзу Мерри (Linda Merry), Джеффа Мейера (Jeff Meyer), Чипа Морнингстара (Chip Morningstar), Евгения Орехова, Бена Пардо (Ben Pardo), Клода Шеннона (Claude Shannon), Стива Соудерса (Steve Souders), Техути (Tehuti) и, самое главное, профессора Лизу фон Дрейк (Lisa von Drake).

Послесловие

В своей карьере программиста я прошел следующие смены парадигм.

• Языки высокого уровня.
• Структурное программирование.
• Объектно-ориентированное программирование.
• Функциональное программирование.