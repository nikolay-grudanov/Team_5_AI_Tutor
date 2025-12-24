---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.82
tokens: 7437
characters: 1689
timestamp: 2025-12-24T03:05:43.518535
finish_reason: stop
---

(http) $ python setup.py install
running install
running bdist_egg
running egg_info
creating api.egg-info
...
creating dist
creating 'dist/api-0.1-py3.6.egg' and adding 'build/bdist.linux-x86_64/egg'
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing api-0.1-py3.6.egg
creating /opt/http/lib/python3.6/site-packages/api-0.1-py3.6.egg
Extracting api-0.1-py3.6.egg to /opt/http/lib/python3.6/site-packages
...
Installed /opt/http/lib/python3.6/site-packages/api-0.1-py3.6.egg
Processing dependencies for api==0.1
Finished processing dependencies for api==0.1

Утилите командной строки pecan требуется файл конфигурации. Он уже был создан для вас в процессе скаффолдинга и располагается в каталоге верхнего уровня. Запустите сервер с config.py в качестве параметра:

(http) $ pecan serve config.py
Starting server in PID 17517
serving on 0.0.0.0:8080, view at http://127.0.0.1:8080

При проверке его в браузере вы получите текстовое сообщение. Вот что отображается, если воспользоваться командой curl:

(http) $ curl localhost:8080
Hello, World!

С помощью команды pecan serve config.py запускается выполнение долгоживущего процесса. Единственный способ остановить его — отправить встроенное исключение KeyboardInterrupt с помощью сочетания клавиш Ctrl+C. Для повторного его запуска требуются активация виртуальной среды и повторное выполнение той же команды pecan serve.

Юниты systemd

В отличие от более старых систем инициализации, работающих с исполняемыми сценариями, systemd работает с неформатированными текстовыми файлами. Итоговая версия unit-файла выглядит вот так:

[Unit]
Description=hello world pecan service
After=network.target

[Service]
Type=simple