---
source_image: page_321.png
page_number: 321
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.89
tokens: 7464
characters: 1970
timestamp: 2025-12-24T10:54:08.683204
finish_reason: stop
---

Мы хотим, чтобы структура Cacher управляла значениями своих полей, не давая вызывающему коду потенциально изменять значения в этих полях напрямую, поэтому поля являются приватными.

Функция Cacher::new берет обобщенный параметр T ②, который мы определили как имеющий тот же типаж, что и структура Cacher ①. Затем Cacher::new возвращает экземпляр структуры Cacher ③, содержащий замыкание, указанное в поле calculation, и значение None в поле value, потому что замыкание еще не было исполнено.

Когда вызывающему коду требуется результат оценки замыкания, вместо прямого вызова замыкания он вызовет метод value ④. Этот метод проверяет, есть ли у нас результирующее значение в self.value внутри Some. Если оно там есть, то он возвращает значение внутри Some, не исполняя замыкание снова ⑤.

Если self.value равно None, то код вызывает замыкание, хранящееся в self.calculation, сохраняет результат self.value для будущего использования, а также возвращает значение ⑥.

Листинг 13.11 показывает, как использовать структуру Cacher в функции generate_workout из листинга 13.6.

Листинг 13.11. Использование структуры Cacher в функции generate_workout, чтобы абстрагировать алгоритм кэширования

src/main.rs

fn generate_workout(intensity: u32, random_number: u32) {
    let mut expensive_result = Cacher::new(|num| {
        println!("вычисляется медленно...");
        thread::sleep(Duration::from_secs(2));
        num
    });
    if intensity < 25 {
        println!(
            "Сегодня сделайте {} отжиманий!",
            expensive_result.value(intensity)
        );
        println!(
            "Далее, сделайте {} приседаний!",
            expensive_result.value(intensity)
        );
    } else {
        if random_number == 3 {
            println!("Сделайте сегодня перерыв! Пейте больше воды!");
        } else {
            println!(
                "Сегодня пробежка {} минут!",
                expensive_result.value(intensity)
            );
        }
    }
}