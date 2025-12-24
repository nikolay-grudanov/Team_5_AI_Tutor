---
source_image: page_397.png
page_number: 397
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.70
tokens: 11556
characters: 1254
timestamp: 2025-12-24T10:34:55.559638
finish_reason: stop
---

Файл Cargo.lock верхнего уровня теперь содержит информацию о зависимости add_one к крейту rand. Тем не менее, не смотря на то что rand использован где-то в рабочем пространстве, мы не можем использовать его в других крейтах рабочего пространства, пока не добавим крейт rand в отдельные Cargo.toml файлы. Например, если мы добавим use rand; в файл adder/src/main.rs крейта adder, то получим ошибку:

$ cargo build
--snip--
Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
   |     ^^^^ no external crate `rand`

Чтобы исправить это, отредактируйте файл Cargo.toml для пакета adder и укажите, что rand также является его зависимостью. При сборке пакета adder rand будет добавлен в список зависимостей для adder в Cargo.lock, но никаких дополнительных копий rand загружено не будет. Cargo позаботился о том, чтобы все крейты во всех пакетах рабочей области, использующих пакет rand, использовали одну и ту же версию, экономя нам место и гарантируя, что все крейты в рабочей области будут совместимы друг с другом.

Добавление теста в рабочее пространство

В качестве ещё одного улучшения давайте добавим тест функции add_one::add_one в add_one:

Файл: add_one/src/lib.rs