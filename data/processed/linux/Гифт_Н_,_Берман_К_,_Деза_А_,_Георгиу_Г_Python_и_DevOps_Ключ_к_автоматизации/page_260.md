---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.10
tokens: 7415
characters: 1693
timestamp: 2025-12-24T03:07:38.473762
finish_reason: stop
---

Выводимая при повышенном уровне детализации (флаг -v) информация демонстрирует, что Testinfra выполняет одну тестовую функцию для двух указанных в спецификации вызова серверов.

При настройке серверов важно обеспечить возможность соединения без пароля. Никаких запросов паролей быть не должно, а при использовании SSH желательно применять конфигурацию на основе ключей.

При автоматизации подобных тестов (в качестве части задания в системе непрерывной интеграции, например) удобно генерировать серверы, определяя тип подключения и любые специальные инструкции. Testinfra может читать информацию о том, к каким серверам подключиться, из файла конфигурации SSH. При предыдущем запуске теста для создания этих серверов со специальными ключами и настройками соединений использовался Vagrant (https://www.vagrantup.com). Он может генерировать специализированные файлы конфигурации SSH для создаваемых им серверов:

(validation) $ vagrant ssh-config
Host node1
  HostName 127.0.0.1
  User vagrant
  Port 2200
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /home/alfredo/.vagrant.d/insecure_private_key
  IdentitiesOnly yes
  LogLevel FATAL

Host node2
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /home/alfredo/.vagrant.d/insecure_private_key
  IdentitiesOnly yes
  LogLevel FATAL

Экспорт выводимого содержимого в файл с последующей передачей его в Testinfra обеспечивает большую гибкость, если серверов несколько:

(validation) $ vagrant ssh-config > ssh-config
(validation) $ pytest --hosts=default --ssh-config=ssh-config test_remote.py