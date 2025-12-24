---
source_image: page_227.png
page_number: 227
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.23
tokens: 7443
characters: 2069
timestamp: 2025-12-24T03:06:53.234041
finish_reason: stop
---

Ресан и Pyramid, все они предоставляют интерфейсы для ранней настройки журналирования. Пользуйтесь!

Следующий пример демонстрирует настройку утилиты командной строки, можно заметить некоторое сходство с basicConfig:

import logging
import os

BASE_FORMAT = "[%(name)s][%(levelname)-6s] %(message)s"
FILE_FORMAT = "[%(asctime)s]" + BASE_FORMAT

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

try:
    file_logger = logging.FileHandler('application.log')
except (OSError, IOError):
    file_logger = logging.FileHandler('/tmp/application.log')
file_logger.setLevel(logging.INFO)
console_logger.setFormatter(logging.Formatter(BASE_FORMAT))
root_logger.addHandler(file_logger)

В этом примере происходит много интересного. Производится запрос к корневому механизму журналирования путем вызова getLogger() без каких-либо аргументов, причем уровень журналирования устанавливается равным DEBUG. Для начала это неплохо, ведь другие дочерние механизмы журналирования могут менять уровень. Далее мы задаем настройки механизма журналирования в файл. В данном случае он пытается открыть файл журнала, а если нет возможности записывать в него, то использует временный файл в каталоге tmp. Далее его уровень журналирования устанавливается в INFO, а формат сообщений меняется и теперь включает метки даты/времени (удобно для файлов журналов).

Обратите внимание на то, что в конце к root_logger добавляется механизм журналирования в файл. Это кажется странным, но в данном случае задается такая конфигурация корневого механизма журналирования, чтобы он отвечал за все. Благодаря добавлению к корневому механизму журналирования потокового обработчика (stream handler) приложение будет отправлять журналы в файл и в стандартный поток ошибок одновременно:

console_logger = logging.StreamHandler()
console_logger.setFormatter(BASE_FORMAT)
console_logger.setLevel(logging.WARNING)
root_logger.addHandler(console_logger)

В данном случае мы воспользовались форматом BASE_FORMAT, поскольку информация будет выводиться в терминал, где метки даты/времени будут только