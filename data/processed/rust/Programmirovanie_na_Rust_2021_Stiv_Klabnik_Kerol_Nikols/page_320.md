---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.72
tokens: 7400
characters: 1566
timestamp: 2025-12-24T10:54:02.932107
finish_reason: stop
---

calculation: T,
    value: Option<u32>,
}

Структура Cacher имеет поле calculation обобщенного типа T. Границы типажа для T уточняют, что оно является замыканием с типажом Fn. Любое замыкание, которое мы хотим сохранить в поле calculation, должно иметь один параметр типа u32 (уточняемый внутри скобок после Fn) и возвращать тип u32 (уточняемый после ->).

ПРИМЕЧАНИЕ

Функции тоже могут реализовывать все три типажа Fn. Если то, что мы хотим сделать, не требует захватывания значения из среды, то можно использовать не замыкание, а функцию, где нам нужно что-то, что реализует типаж Fn.

Поле value имеет тип Option<u32>. Перед тем как мы исполним замыкание, value будет None. В момент, когда код, использующий структуру Cacher, запрашивает результат замыкания, Cacher исполнит замыкание и сохранит результат внутри варианта Some в поле value. Затем, если код опять запросит результат замыкания, то, не исполняя замыкание снова, Cacher вернет результат, содержащийся в варианте Some.

Алгоритм, связанный с только что описанным полем value, определен в листинге 13.10.

Листинг 13.10. Алгоритм кэширования структуры Cacher
src/main.rs

impl<T> Cacher<T>
    where T: Fn(u32) -> u32
{
    fn new(calculation: T) -> Cacher<T> {
        Cacher {
            calculation,
            value: None,
        }
    }

    fn value(&mut self, arg: u32) -> u32 {
        match self.value {
            Some(v) => v,
            None => {
                let v = (self.calculation)(arg);
                self.value = Some(v);
                v
            },
        }
    }
}