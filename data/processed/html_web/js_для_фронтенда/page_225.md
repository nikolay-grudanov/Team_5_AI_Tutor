---
source_image: page_225.png
page_number: 225
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.38
tokens: 6220
characters: 1569
timestamp: 2025-12-24T10:07:09.713933
finish_reason: stop
---

этой главе мы будем работать с ее Node.js-версией, которая называется nodeload (https://github.com/benschmaus/nodeload).

Первым делом установим утилиту:

% sudo npm install nodeload -g

Примечание

Таким образом, вы не установите nodeload ни в Windows, ни в Linux. Через npm install программа почему-то отказывается устанавливаться, что в Windows, что в Linux. Рассмотрим, как правильно установить nodeload в Linux. Первым делом нужно установить сам npm:

sudo apt-get install npm

Затем нам нужно установить программу git, необходимую для загрузки исходного кода nodeload:

sudo apt-get install git

После чего загружаем саму программу nodeload:

git clone git://github.com/benschmaus/nodeload.git

cd nodeload

В каталоге nodeload, в который мы только что перешли, будет исполняемый файл nl.js. Откройте его. Первая строчка этого файла будет такой:

#!/usr/bin/env node

В Linux исполняемый файл node называется nodejs, поэтому эту строчку нужно изменить так:

#!/usr/bin/env nodejs

После этого можно приступить к использованию программы, как описано далее в книге.

Рассмотрим формат использования утилиты nl.js (с утилитой ab (исполняемый файл Apache Bench) все примерно то же самое):

% nl.js
1 Aug 20:28:52 - nodeload.js [options] <host>:<port>[<path>]
Available options:
-n, --number NUMBER    Number of requests to make.
Defaults to value of --concurrency unless a time limit is specified.
-c, --concurrency NUMBER    Concurrent number of connections.
Defaults to 1.
-t, --time-limit NUMBER    Number of seconds to spend running test. No timelimit by default.