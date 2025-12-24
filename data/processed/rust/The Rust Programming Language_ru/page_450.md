---
source_image: page_450.png
page_number: 450
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.01
tokens: 11357
characters: 637
timestamp: 2025-12-24T10:36:51.131003
finish_reason: stop
---

Листинг 15-29: Создание branch во внутренней области видимости и подсчёт сильных и слабых ссылок

После того, как leaf создан его Rc<Node> имеет значения strong count равное 1 и weak count равное 0. Во внутренней области мы создаём branch и связываем её с leaf, после чего при печати значений счётчиков Rc<Node> в branch они будет иметь strong count 1 и weak count 1 (для leaf.parent указывающего на branch с Weak<Node>). Когда мы распечатаем счётчики из leaf, мы увидим, что они будут иметь strong count 2, потому что branch теперь имеет клон Rc<Node> переменной leaf хранящийся в branch.children, но все равно будет иметь weak count 0.