---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.27
tokens: 7409
characters: 1732
timestamp: 2025-12-24T10:52:19.948944
finish_reason: stop
---

Обратите внимание, что мы добавили новую строку кода внутрь модуля tests:
use super::*; ①. Модуль tests — это обычный модуль, который подчиняется обычным правилам видимости, описанным в разделе «Пути для ссылки на элемент в дереве модулей» (с. 151). Поскольку модуль tests внутренний, необходимо ввести тестируемый код во внешнем модуле в область видимости внутреннего модуля. Здесь мы используем оператор glob *, поэтому все, что мы определяем во внешнем модуле, доступно этому модулю tests.

Мы назвали тест larger_can_hold_smaller ② и создали два экземпляра структуры Rectangle, которые нам нужны ③. Затем мы вызвали макрокоманду assert! и передали ей результат larger_can_hold_smaller(&smaller) ④. Предполагается, что это выражение вернет true, поэтому тест должен быть успешным. Давайте выясним это!

    running 1 test
    test tests::larger_can_hold_smaller ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Он действительно успешно! Давайте добавим еще один тест, на этот раз подтверждающий, что меньший прямоугольник не вместит больший прямоугольник:

src/lib.rs
    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn larger_can_hold_smaller() {
            // --пропуск--
        }

        #[test]
        fn smaller_cannot_hold_larger() {
            let larger = Rectangle { length: 8, width: 7 };
            let smaller = Rectangle { length: 5, width: 1 };

            assert!(!smaller.can_hold(&larger));
        }
    }

Поскольку правильный результат функции can_hold в этом случае является ложным, мы должны инвертировать этот результат перед его передачей в макрокоманду assert!. В результате тест будет успешным, если can_hold возвращает false: