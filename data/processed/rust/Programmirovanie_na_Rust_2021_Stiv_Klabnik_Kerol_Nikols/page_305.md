---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.32
tokens: 7539
characters: 2222
timestamp: 2025-12-24T10:53:53.275667
finish_reason: stop
---

вателя — "rust", "RUST", "Rust" и "rUsT" — этот запрос рассматривался так, как если бы это был "rust", нечувствительный к регистру.

Обратите внимание, что query теперь относится к типу String, а не к строковому срезу, поскольку вызов метода to_lowercase создает новые данные, а не ссылается на существующие. Допустим, что запросом, к примеру, является "rUsT": этот строковый срез не содержит строчной буквы u или t, поэтому мы должны выделить новый экземпляр типа String, содержащий "rust". Когда мы теперь передаем query в качестве аргумента в метод contains, нам нужно добавить амперсанд ③, потому что сигнатура метода contains по определению берет строковый срез.

Далее мы добавляем вызов метода to_lowercase для каждой line, который переводит все символы строки текста в нижний регистр, перед проверкой на наличие запроса query ②. Теперь, конвертировав line и query в нижний регистр, мы найдем совпадения независимо от регистра запроса.

Давайте посмотрим, пройдет ли эта реализация проверку:

running 2 tests
test tests::case_insensitive ... ok
test tests::case_sensitive ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Отлично! Проверка пройдена. Теперь давайте вызовем новую функцию search_case_insensitive из функции run. Сначала мы добавим вариант конфигурации в структуру Config, чтобы переключать поиск с чувствительного к регистру на нечувствительный и наоборот. Добавление этого поля вызовет ошибки компилятора, так как мы еще нигде не инициализируем это поле:

src/lib.rs
pub struct Config {
    pub query: String,
    pub filename: String,
    pub case_sensitive: bool,
}

Обратите внимание, что мы добавили поле case_sensitive, которое содержит булево значение. Далее нужно, чтобы функция run проверяла значение поля case_sensitive и использовала его для принятия решения о том, какую функцию вызывать — search или search_case_insensitive, как показано в листинге 12.22. Обратите внимание, что этот код пока не компилируется.

Листинг 12.22. Вызов функции search либо search_case_insensitive в зависимости от значения в config.case_sensitive
src/lib.rs
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;