---
source_image: page_178.png
page_number: 178
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.55
tokens: 7466
characters: 1570
timestamp: 2025-12-23T23:08:33.131905
finish_reason: stop
---

"version": "14.0.297.0",
"result": "Trojan.Ransom.WannaCryptor.H",
"update": "20180712"}
.
.
.

Хотя JSON отлично подходит для структурирования данных, у людей при чтении могут возникнуть трудности. С помощью grep вы можете извлечь некоторые важные сведения, например, был ли файл определен как вредоносный:

$ grep -Po '{"detected": true.*?"result":.*?,}' Calc_VirusTotal.txt

{"detected": true, "version": "1.3.0.9466", "result": "W32.WannaCrypLTE.Trojan",
{"detected": true, "version": "14.0.297.0", "result": "Trojan.Ransom.WannaCryptor.H",
{"detected": true, "version": "14.00", "result": "Trojan.Mauvaise.SL1",

В grep параметр -P применяется для включения движка Perl, который позволяет использовать шаблон .*? как ленивый квантификатор. Этот ленивый квантификатор соответствует только минимальному количеству символов, необходимых для соответствия всему регулярному выражению, что позволяет извлекать ответ из каждого антивирусного ядра по отдельности, а не из большой группы.

Хотя этот метод работает, наилучшее решение можно создать с помощью сценария bash, как показано в примере 11.2.

Пример 11.2. vtjson.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# vtjson.sh
#
# Описание:
# Поиск вредоносных программ в файле JSON
#
# Использование:
# vtjson.awk [<json file>]
#   <json file> Файл с результатами VirusTotal
#     по умолчанию: Calc_VirusTotal.txt

RE='^.(.*)...{\.*detect..(.*),.vers.*result....(.*).,..update.*$' ①

FN="${1:-Calc_VirusTotal.txt}"
sed -e 's/{"scans": {/\n /' -e 's/},/&\n/g' "$FN" | ②
while read ALINE
do
    if [[ $ALINE =~ $RE ]] ③