---
source_image: page_433.png
page_number: 433
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.09
tokens: 7373
characters: 1702
timestamp: 2025-12-24T10:57:04.360027
finish_reason: stop
---

Листинг 17.1. Структура AveragedCollection, которая поддерживает список целых чисел и среднее арифметическое значение элементов в коллекции

src/lib.rs

pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}

Указанная структура помечена как pub, благодаря чему ее может использовать другой код, но поля внутри структуры остаются приватными. Это важно в данном случае потому, что нужно, чтобы всякий раз, когда значение добавляется в список или удаляется из него, среднее значение также обновлялось. Мы делаем это, реализуя методы add, remove и average в структуре, как показано в листинге 17.2.

Листинг 17.2. Реализации публичных методов add, remove и average в структуре AveragedCollection

src/lib.rs

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
            },
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

Публичные методы add, remove и average — это единственные способы доступа к данным, а также для их изменения в экземпляре структуры AveragedCollection. Когда элемент добавляется в список с помощью метода add или удаляется с помощью метода remove, реализации каждого из них вызывают приватный метод update_average, который также обрабатывает обновление поля average.