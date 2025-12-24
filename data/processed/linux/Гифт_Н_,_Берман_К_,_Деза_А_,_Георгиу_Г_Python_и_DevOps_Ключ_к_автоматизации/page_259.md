---
source_image: page_259.png
page_number: 259
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.26
tokens: 7464
characters: 1911
timestamp: 2025-12-24T03:07:42.435165
finish_reason: stop
---

(validation) $ pytest --help
...
testinfra:
  --connection=CONNECTION
    Remote connection backend (paramiko, ssh, safe-ssh, salt, docker, ansible)
  --hosts=HOSTS
    Hosts list (comma separated)
  --ssh-config=SSH_CONFIG
    SSH config file
  --ssh-identity-file=SSH_IDENTITY_FILE
    SSH identify file
  --sudo
    Use sudo
  --sudo-user=SUDO_USER
    sudo user
  --ansible-inventory=ANSIBLE_INVENTORY
    Ansible inventory file
  --nagios
    Nagios plugin

Пусть даны два работающих сервера. Чтобы продемонстрировать опции соединений, проверим, работает ли на них CentOS 7, заглянув для этого в файл /etc/os-release. Вот как выглядит соответствующая тестовая функция (сохранена в файле test_remote.py):

def test_release_file(host):
    release_file = host.file("/etc/os-release")
    assert release_file.contains('CentOS')
    assert release_file.contains('VERSION="7 (Core)"')

Это отдельная тестовая функция, которая принимает на входе фикстуру host и выполняется для всех указанных узлов.

Флаг --hosts позволяет указать список серверов со схемами соединения (например, в случае SSH — ssh://имя_хоста), допустимы также некоторые варианты с подстановками. Передавать в командной строке удаленные серверы неудобно, если тестировать за раз более чем один-два. Вот как выглядит тестирование двух серверов с помощью SSH:

(validation) $ pytest -v --hosts='ssh://node1,ssh://node2' test_remote.py
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
cachedir: .pytest_cache
rootdir: /home/alfredo/python/python-devops/samples/chapter16
plugins: testinfra-3.0.0, xdist-1.28.0, forked-1.0.2
collected 2 items

test_remote.py::test_release_file[ssh://node1] PASSED [ 50%]
test_remote.py::test_release_file[ssh://node2] PASSED [100%]
============================= 2 passed in 3.82 seconds =========================