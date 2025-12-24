---
source_image: page_389.png
page_number: 389
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.46
tokens: 11776
characters: 2146
timestamp: 2025-12-24T10:35:03.727704
finish_reason: stop
---

Допустим, у вас есть крейт, который вы хотите опубликовать. Перед публикацией вам нужно добавить некоторые метаданные в раздел [package] файла Cargo.toml крейта.

Вашему крейту понадобится уникальное имя. Пока вы работаете над крейтом локально, вы можете назвать его как угодно. Однако названия крейтов на crates.io фиксируются в момент первой публикации. Как только крейту присвоено название, никто другой не сможет опубликовать крейт с таким же именем. Перед тем как опубликовать крейт, поищите название, которое вы хотите использовать. Если такое имя уже используется, вам придётся подобрать другое и отредактировать поле name в файле Cargo.toml в разделе [package], чтобы использовать новое имя в качестве публикуемого, например, так:

Файл: Cargo.toml

[package]
name = "guessing_game"

Даже если вы выбрали уникальное имя, когда вы запустите cargo publish чтобы опубликовать крейт, вы получите предупреждение, а затем ошибку:

$ cargo publish
  Updating crates.io index
warning: manifest has no description, license, license-file, documentation, homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields: description, license. Please see https://doc.rust-lang.org/cargo/reference/manifest.html for how to upload metadata

Это ошибка, потому что вам не хватает важной информации: необходимы описание и лицензия, чтобы люди знали, что делает ваш крейт и на каких условиях они могут его использовать. В поле Cargo.toml добавьте описание, состоящее из одного-двух предложений, поскольку оно будет появляться вместе с вашим крейтом в результатах поиска. Для поля license нужно указать значение идентификатора лицензии. В Linux Foundation's Software Package Data Exchange (SPDX) перечислены идентификаторы, которые можно использовать для этого значения. Например, чтобы указать, что вы лицензировали свой crate, используя лицензию MIT, добавьте идентификатор MIT:

Файл: Cargo.toml

[package]
name = "guessing_game"
license = "MIT"