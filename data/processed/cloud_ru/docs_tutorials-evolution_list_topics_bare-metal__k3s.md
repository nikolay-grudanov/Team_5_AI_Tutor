---
source_image: docs_tutorials-evolution_list_topics_bare-metal__k3s.jpg
page_number: 3
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.32
tokens: 4930
characters: 2268
timestamp: 2025-12-24T05:28:51.915239
finish_reason: stop
---

Развертывание K3s на сервере Bare Metal

С помощью этого руководства вы развернете сервер Bare Metal с K3s — упрощенной версией Kubernetes для сред с ограниченными ресурсами. Решение сохраняет все возможности Kubernetes и подходит для тестирования и разработки небольших приложений.

Шаги:

1. Разверните инфраструктуру.
2. Установите K3s.
3. Настройте удаленный доступ.
4. Добавьте дополнительные узлы.

1. Разверните инфраструктуру
1. Арендуйте сервер Bare Metal с публичным IP-адресом.
2. Подключитесь к серверу по SSH или через виртуальную консоль.
3. Обновите систему и установите утилиту Curl:
   ```
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y curl
   ```

4. Откройте порт 6443:
   ```
   sudo ufw allow 6443
   ```

2. Установите K3s
1. Выполните команду:
   ```
   curl -sSL https://get.k3s.io | sh -
   ```

2. Проверьте установку:
   ```
   systemctl status k3s
   ```
   Результат:
   ```
   ● k3s.service - Lightweight Kubernetes
      Loaded: loaded (/etc/systemd/system/k3s.service; enabled; preset: enabled)
      Active: active (running) since Thu 2025-07-17 13:26:31 MSK; 1s ago
   ```

3. Настройте удаленный доступ
1. Получите содержимое конфигурационного файла:
   ```
   cat /etc/rancher/k3s/config.yaml
   ```
   Скопируйте содержимое.
2. Вставьте содержимое в файл /.kube/config на вашем устройстве.
   Замените IP-адрес 127.0.0.1 на IP-адрес сервера или DNS-имя вашего хоста.

4. Добавьте дополнительные узлы
Дополнительным узлом может стать виртуальная машина, другой сервер или пользовательское устройство.
1. Сгенерируйте токен на сервере:
   ```
   sudo k3s token create --ttl lh
   ```

2. Установите K3s на новый узел:
   ```
   curl -sSL https://get.k3s.io | K3S_URL=https://<server_ip>:6443 K3S_TOKEN=<token> sh -
   ```
   Где:
   • <server_ip> — IP-адрес сервера.
   • <token> — токен, полученный на предыдущем шаге.

3. Проверьте подключение узла:
   ```
   k3s kubectl get nodes
   ```
   Результат:
   ```
   NAME     STATUS    ROLES    AGE   VERSION
   server.local   Ready   control-plane,master   3d   v1.31.5+k3s1
   ```

Вы установили K3s, настроили к нему удаленный доступ и добавили дополнительные узлы для расширения кластера. Такую конфигурацию можно использовать как среду для небольших приложений.