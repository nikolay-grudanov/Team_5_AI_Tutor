---
source_image: page_580.png
page_number: 580
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.80
tokens: 11797
characters: 2322
timestamp: 2025-12-24T10:42:55.766403
finish_reason: stop
---

use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // Construct a representation of Rust code as a syntax tree
    // that we can manipulate
    let ast = syn::parse(input).unwrap();

    // Build the trait implementation
    impl_hello_macro(&ast)
}

Листинг 19-31: Код, который потребуется в большинстве процедурных макро крейтов для обработки Rust кода

Обратите внимание, что мы разделили код на функцию hello_macro_derive, которая отвечает за синтаксический анализ TokenStream и функцию impl_hello_macro, которая отвечает за преобразование синтаксического дерева: это делает написание процедурного макроса удобнее. Код во внешней функции (hello_macro_derive в данном случае) будет одинаковым для почти любого процедурного макрос крейта, который вы видите или создаёте. Код, который вы указываете в теле внутренней функции (в данном случае impl_hello_macro) будет отличаться в зависимости от цели вашего процедурного макроса.

Мы представили три новых крейта: proc_macro, syn и quote. Макрос proc_macro поставляется с Rust, поэтому нам не нужно было добавлять его в зависимости внутри Cargo.toml. Макрос proc_macro - это API компилятора, который позволяет нам читать и манипулировать Rust кодом из нашего кода.

Крейт syn разбирает Rust код из строки в структуру данных над которой мы может выполнять операции. Крейт quote превращает структуры данных syn обратно в код Rust. Эти крейты упрощают разбор любого вида Rust кода, который мы хотели бы обрабатывать: написание полного синтаксического анализатора для кода Rust не является простой задачей.

Функция hello_macro_derive будет вызываться, когда пользователь нашей библиотеки указывает своему типу #[derive(HelloMacro)]. Это возможно, потому что мы аннотировали функцию hello_macro_derive с помощью proc_macro_derive и указали имя HelloMacro, которое соответствует имени нашего типажа; это соглашение, которому следует большинство процедурных макросов.

Функция hello_macro_derive сначала преобразует input из TokenStream в структуру данных, которую мы можем затем интерпретировать и над которой выполнять операции. Здесь крейт syn вступает в игру. Функция parse в syn принимает TokenStream и возвращает структуру DeriveInput, представляющую разобранный код