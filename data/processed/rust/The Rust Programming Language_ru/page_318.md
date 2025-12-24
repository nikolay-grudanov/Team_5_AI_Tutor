---
source_image: page_318.png
page_number: 318
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.60
tokens: 11665
characters: 1819
timestamp: 2025-12-24T10:31:58.467069
finish_reason: stop
---

Файл: src/main.rs

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = parse_config(&args);

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    let contents = fs::read_to_string(config.file_path)
        .expect("Should have been able to read the file");

    // --snip--
}

struct Config {
    query: String,
    file_path: String,
}

fn parse_config(args: &[String]) -> Config {
    let query = args[1].clone();
    let file_path = args[2].clone();

    Config { query, file_path }
}
```

Листинг 12-6: Рефакторинг функции parse_config, чтобы возвращать экземпляр структуры Config

Мы добавили структуру с именем Config объявленную с полями названными как query и filename. Сигнатура parse_config теперь указывает, что она возвращает значение Config. В теле parse_config, где мы возвращали срезы строк, которые ссылаются на значения String в args, теперь мы определяем Config как содержащие собственные String значения. Переменная args в main является владельцем значений аргумента и позволяют функции parse_config только одолживать их, что означает, что мы бы нарушили правила заимствования Rust, если бы Config попытался бы взять во владение значения в args.

Мы можем управлять данными String разным количеством способов, но самый простой, хотя и отчасти неэффективный это вызвать метод clone у значений. Он делает полную копию данных для экземпляра Config для владения, что занимает больше времени и памяти, чем сохранение ссылки на строку данных. Однако клонирование данных также делает наш код очень простым, потому что нам не нужно управлять временем жизни ссылок; в этом обстоятельстве, отказ от небольшой производительности, чтобы получить простоту, стоит небольшого компромисса.

Компромиссы при использовании метода clone