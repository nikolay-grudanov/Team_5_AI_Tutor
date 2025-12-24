---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.75
tokens: 7402
characters: 1778
timestamp: 2025-12-24T10:53:48.370482
finish_reason: stop
---

let results = if config.case_sensitive {
    search(&config.query, &contents)
} else {
    search_case_insensitive(&config.query, &contents)
};

for line in results {
    println!("{}", line);
}

Ok(())
}

Наконец, нужно проверить переменную среды. Функции для работы с переменными среды находятся в модуле env стандартной библиотеки, поэтому мы хотим ввести этот модуль в область видимости с помощью строки use std::env; в верхней части src/lib.rs. Затем мы воспользуемся функцией var из модуля env для проверки переменной среды с именем CASE_INSENSITIVE, как показано в листинге 12.23.

Листинг 12.23. Проверка переменной среды с именем CASE_INSENSITIVE
src/lib.rs

use std::env;
// --пропуск--

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("недостаточно аргументов");
        }

        let query = args[1].clone();
        let filename = args[2].clone();

        let case_sensitive = env::var("CASE_INSENSITIVE").is_err();

        Ok(Config { query, filename, case_sensitive })
    }
}

Здесь мы создаем новую переменную case_sensitive. Для того чтобы задать ее значение, мы вызываем функцию env::var и передаем ей имя переменной среды CASE_INSENSITIVE. Функция env::var возвращает экземпляр типа Result, который будет равен успешному варианту Ok и будет содержать значение переменной среды, если переменная среды задана. Она вернет вариант Err, если переменная среды не задана.

Мы используем метод is_err для экземпляра типа Result, чтобы проверить, имеется ли ошибка и задан ли он. Это значит, что программа должна выполнить поиск, чувствительный к регистру. Если переменная среды CASE_INSENSITIVE задана и имеет любое значение, то is_err вернет false и программа выполнит поиск, не-