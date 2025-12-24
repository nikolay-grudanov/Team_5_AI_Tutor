---
source_image: page_522.png
page_number: 522
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.65
tokens: 7497
characters: 2006
timestamp: 2025-12-24T10:59:28.707581
finish_reason: stop
---

Нам нужно объявить hello_macro_derive как упаковку для процедурных макрокоманд. Нам также понадобится функциональность из упаковок syn и quote, как вы вскоре увидите, поэтому нужно добавить их в качестве зависимостей. Добавьте в файл Cargo.toml для hello_macro_derive следующее:

hello_macro_derive/Cargo.toml
    [lib]
    proc-macro = true

    [dependencies]
    syn = "0.14.4"
    quote = "0.6.3"

Для того чтобы начать определение процедурной макрокоманды, поместите код из листинга 19.31 в файл src/lib.rs для упаковки hello_macro_derive. Обратите внимание, этот код не будет компилироваться до тех пор, пока мы не добавим определение функции impl_hello_macro.

Листинг 19.31. Код, который потребуется для обработки кода Rust большинству упаковок для процедурных макрокоманд
hello_macro_derive/src/lib.rs
    extern crate proc_macro;

    use crate::proc_macro::TokenStream;
    use quote::quote;
    use syn;

    #[proc_macro_derive(HelloMacro)]
    pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
        // Сконструировать представление кода Rust в виде синтаксического дерева,
        // которым можно манипулировать
        let ast = syn::parse(input).unwrap();

        // Создать реализацию типажа
        impl_hello_macro(&ast)
    }

Обратите внимание, мы разделили код на функцию hello_macro_derive, которая отвечает за разбор потока TokenStream, и функцию impl_hello_macro, которая отвечает за преобразование синтаксического дерева: это делает написание процедурной макрокоманды удобнее. Код во внешней функции (в данном случае hello_macro_derive) будет одинаковым почти для каждой процедурной макрокоманды, которую вы встретите или создадите. Код, который вы приводите в теле внутренней функции (в данном случае impl_hello_macro), будет отличаться в зависимости от назначения процедурной макрокоманды.

Мы ввели три новые упаковки: proc_macro, syn (доступна на https://crates.io/crates/syn) и quote (доступна на https://crates.io/crates/quote). Упаковка proc_macro постав-