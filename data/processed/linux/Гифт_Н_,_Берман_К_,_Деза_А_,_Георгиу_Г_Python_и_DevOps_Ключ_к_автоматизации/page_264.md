---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.05
tokens: 7552
characters: 2132
timestamp: 2025-12-24T03:07:58.118519
finish_reason: stop
---

Повторный запуск теста, казалось бы, должен опять пройти успешно:

(validate) $ pytest -q --hosts='ssh://node4' test_webserver.py
.F
============================= FAILURES ================================
____________________ test_nginx_is_running[ssh://node4] ______________________

host = <testinfra.host.Host object at 0x7f629bf1d668>

    def test_nginx_is_running(host):
>       assert host.service('nginx').is_running
E           AssertionError: assert False
E           + where False = <service nginx>.is_running
E           +     where <service nginx> = <class 'SystemdService'>('nginx')

test_webserver.py:7: AssertionError
1 failed, 1 passed in 2.45 seconds

Некоторые дистрибутивы Linux не разрешают пакетам запускать сервисы при установке. Более того, тест обнаружил, что сервис Nginx не запущен, как сообщает systemd (сервис по умолчанию для работы с юнитами). Если запустить Nginx вручную и выполнить тест еще раз, он снова должен пройти успешно:

(validate) $ systemctl start nginx
(validate) $ pytest -q --hosts='ssh://node4' test_webserver.py
..
2 passed in 2.38 seconds

Как упоминалось в начале раздела, веб-сервер должен выдавать статическую стартовую страницу на порте 80. Следующий шаг — добавление еще одного теста (в тот же файл test_webserver.py) для проверки порта:

def test_nginx_listens_on_port_80(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening

Этот тест несколько сложнее, так что имеет смысл обратить внимание на некоторые его нюансы. По умолчанию он проверяет TCP-соединения на порте 80 для всех IP-адресов данного сервера. Хотя для текущего теста никакой разницы нет, но, если у сервера есть несколько интерфейсов и он настроен на привязку к конкретному адресу, значит, нужно добавить еще один тест. Добавление еще одного теста для проверки прослушивания на порте 80 на конкретном IP-адресе может показаться перебором, но если задуматься о выводимом тестом отчете, станет ясно, что из него будет понятнее, что происходит.

1. Тест, проверяющий, что nginx прослушивает на порте 80: ПРОЙДЕН.
2. Тест, проверяющий, что nginx прослушивает по адресу 192.168.0.2 на порте 80: не пройден.