---
source_image: page_313.png
page_number: 313
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.69
tokens: 7465
characters: 1967
timestamp: 2025-12-24T10:54:01.046607
finish_reason: stop
---

Обязательные входные данные:

○ Число интенсивности, заданное пользователем, конкретизируется, когда он запрашивает тренировку, и указывает, какая тренировка необходима — низкоинтенсивная или высокоинтенсивная.

○ Случайное число, которое будет генерировать разнообразие в планах тренировки.

Результатом будет рекомендованный план тренировок. В листинге 13.2 показана функция main, которую мы будем использовать.

Листинг 13.2. Функция main с жестко заданными значениями для моделирования ввода пользователем данных и генерации случайных чисел

src/main.rs

fn main() {
    let simulated_user_specified_value = 10;
    let simulated_random_number = 7;

    generate_workout(
        simulated_user_specified_value,
        simulated_random_number
    );
}

Для простоты мы жестко закодировали переменную simulated_user_specified_value как 10, а переменную simulated_random_number как 7. В реальной программе мы бы получили число интенсивности из фронтэнда приложения и использовали бы упаковку rand для генерации случайного числа, как в игре из главы 2. Функция main вызывает функцию generate_workout с условными входными значениями.

Теперь, когда у нас есть контекст, давайте перейдем к алгоритму. Функция generate_workout в листинге 13.3 содержит логику функционирования приложения, которая в этом примере интересует нас больше всего. Остальные изменения в коде этого примера будут вноситься именно в эту функцию.

Листинг 13.3. Логика функционирования, которая выводит планы тренировок на основе входных данных и вызывает функцию simulated_expensive_calculation

src/main.rs

fn generate_workout(intensity: u32, random_number: u32) {
    if intensity < 25 {
        println!(
            "Сегодня сделайте {} отжиманий!",
            simulated_expensive_calculation(intensity)
        );
        println!(
            "Далее, сделайте {} приседаний!",
            simulated_expensive_calculation(intensity)
        );
    } else {
        if random_number == 3 {