---
source_image: page_483.png
page_number: 483
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.65
tokens: 11650
characters: 1689
timestamp: 2025-12-24T10:38:38.536343
finish_reason: stop
---

i32. Структура также может иметь поле содержащее среднее значение в векторе, так что всякий раз, когда кто-либо захочет получить среднее значение элементов вектора, нам не нужно вычислять его заново, другими словами, AveragedCollection будет кэшировать рассчитанное среднее значение для нас. В примере 17-1 приведено определение структуры AveragedCollection:

Файл: src/lib.rs

pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}

Листинг 17-1: структура AveragedCollection содержит список целых чисел и среднее значение элементов в коллекции.

Обратите внимание, что структура помечена ключевым словом pub, что позволяет другому коду её использовать, однако, поля внутри структуры остаются недоступными. Это важно, потому что мы хотим гарантировать обновление среднего значения при добавлении или удалении элемента из списка. Мы можем получить нужное поведение, определив в структуре методы add, remove и average, как показано в примере 17-2:

Файл: src/lib.rs

impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}

Листинг 17-2: Реализация публичных методов add, remove и average структуры AveragedCollection