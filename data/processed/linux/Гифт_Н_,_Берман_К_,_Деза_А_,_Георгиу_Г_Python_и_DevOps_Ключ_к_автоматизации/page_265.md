---
source_image: page_265.png
page_number: 265
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.84
tokens: 7493
characters: 1935
timestamp: 2025-12-24T03:07:56.204356
finish_reason: stop
---

Из этого видно, что Nginx привязывается к порту 80, просто не к тому интерфейсу, который нужен. Дополнительный тест в данном случае — прекрасный способ улучшить детализацию за счет увеличения объема выводимой информации.

Запустим только что добавленный тест:

(validate) $ pytest -q --hosts='ssh://node4' test_webserver.py
..F
============================= FAILURES ================================
_________________ test_nginx_listens_on_port_80[ssh://node4] ________________
host = <testinfra.host.Host object at 0x7fbaa64f26a0>

    def test_nginx_listens_on_port_80(host):
>       assert host.socket("tcp://0.0.0.0:80").is_listening
E           AssertionError: assert False
E           + where False = <socket tcp://0.0.0.0:80>.is_listening
E           +     where <socket tcp://0.0.0.0:80> = <class 'LinuxSocketSS'>

test_webserver.py:11: AssertionError
1 failed, 2 passed in 2.98 seconds

Ни на одном IP-адресе не производилось прослушивание на порте 80. Из конфигурации Nginx становится ясно, что он был настроен на прослушивание на порте 8080 с помощью инструкции настройки порта в сайте по умолчанию:

(validate) $ grep "listen 8080" /etc/nginx/sites-available/default
    listen 8080 default_server;

После изменения на порт 80 и перезапуска сервиса nginx тест снова проходит успешно:

(validate) $ grep "listen 80" /etc/nginx/sites-available/default
    listen 80 default_server;
(validate) $ systemctl restart nginx
(validate) $ pytest -q --hosts='ssh://node4' test_webserver.py
...
3 passed in 2.92 seconds

А поскольку встроенной фикстуры для обработки HTTP-запросов к конкретному адресу не существует, последний тест извлекает контент запущенного веб-сайта с помощью утилиты wget и выполняет операторы контроля результатов, чтобы убедиться в правильной визуализации статического сайта:

def test_get_content_from_site(host):
    output = host.check_output('wget -qO- 0.0.0.0:80')
    assert 'Welcome to nginx' in output