---
source_image: page_292.png
page_number: 292
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.04
tokens: 6096
characters: 1082
timestamp: 2025-12-24T10:08:19.210095
finish_reason: stop
---

длина функции больше 30 строк, у функции более пяти аргументов, цикломатическая сложность больше 9.

Мы будем использовать npm-пакет jscheckstyle (https://github.com/nomiddlename/jscheckstyle) для получения значения сложности для каждой функции:

% npm install jscheckstyle -g

Этот пакет добавляет преимущества вывода в Jenkins-совместимом формате. Рассмотрим сценарий предварительной фиксации (/git/hooks/pre-commit):

#!/usr/bin/perl
# Get file list
my @files = `git diff --cached --name-only HEAD`;
my $failed = 0;
foreach (@files) {
    # Проверяем только файлы *.js
    if (/\.js$/) {
        my @style = `jscheckstyle --violations $_`;
        if ($?) {
            # Отправляем сообщение об ошибке клиенту
            print @style;
            $failed++;
        }
    }
}
exit $failed;

Этот код просто получает список файлов, которые должны быть зафиксированы и запускает jscheckstyle для каждого из них. Если любой из файлов провалит проверку, клиенту будет отправлено сообщение об ошибке и фиксация будет отменена.

Фиксация сложного файла из моего npm-пакета Injectify: