---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__vpa.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.35
tokens: 8544
characters: 4785
timestamp: 2025-12-24T05:57:11.342563
finish_reason: stop
---

### Развертывание Deployment с вертикальным масштабированием подов

В сценарии развернем Deployment с тремя подами, каждый из которых запускает контейнер с nginx. В Deployment укажем:

- запросы на лимиты — 500m CPU и 1 ГиБ памяти;
- запросы на ресурсы — 150m CPU и 100 МиБ памяти.

Далее создадим объект VerticalPodAutoscaler с режимом Auto.

Перед началом работы

1. Создайте кластер Managed Kubernetes и хотя бы одну группу узлов.
2. Установите плагины Metrics Server и Vertical Pod Autoscaler.
3. Подключитесь к кластеру Managed Kubernetes.

Шаг 1. Создайте Deployment

1. Создайте файл cloudru-nginx.yaml и скопируйте следующую спецификацию:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudru-nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cloudru-nginx
  template:
    metadata:
      labels:
        app: cloudru-nginx
    spec:
      containers:
      - name: cloudru-nginx
        image: mk8s.registry.smk.sbercloud.dev/nginx:latest
        resources:
          limits:
            cpu: 500m
            memory: 1Gi
          requests:
            cpu: 150m
            memory: 100Mi
        command: ["bin/sh"]
        args: ["-c", "while true; do timeout 0.5s yes >/dev/null; sleep 0.5s; done"]
```

2. Выполните команду:

```sh
kubectl create -f cloudru-nginx.yaml
```

Если команда выполнена успешно, появится сообщение:

```sh
deployment.apps/cloudru-nginx created
```

3. Подождите несколько минут, а затем посмотрите информацию о запущенных подах:

```sh
kubectl get pods -l app=cloudru-nginx
```

Результат должен выглядеть примерно так:

<table>
  <tr>
    <th>NAME</th>
    <th>READY</th>
    <th>STATUS</th>
    <th>RESTARTS</th>
    <th>AGE</th>
  </tr>
  <tr>
    <td>cloudru-nginx-435634132-jwr37</td>
    <td>1/1</td>
    <td>Running</td>
    <td>0</td>
    <td>6m21s</td>
  </tr>
  <tr>
    <td>cloudru-nginx-435634132-fn21</td>
    <td>1/1</td>
    <td>Running</td>
    <td>0</td>
    <td>5m09s</td>
  </tr>
  <tr>
    <td>cloudru-nginx-435634132-qj79</td>
    <td>1/1</td>
    <td>Running</td>
    <td>0</td>
    <td>3m44s</td>
  </tr>
</table>

4. Получите подробную информацию об одном из подов:

```sh
kubectl describe pod <pod_name>
```

Вместо `<pod_name>` укажите название любого пода из результата предыдущей команды.

Результат должен выглядеть примерно так:

```yaml
...
cloudru-nginx:
  Container ID: containerd://...
  Image: mk8s.registry.smk.sbercloud.dev/nginx:latest
  Image ID: sha256:...
  Port: <none>
  Host Port: <none>
  Command:
    /bin/sh
  Args:
    -c
    while true; do timeout 0.5s yes >/dev/null; sleep 0.5s; done
  State:
    Running
  Started: Wed, 14 Aug 2024 10:19:12 -0400
  Ready: True
  Restart Count: 0
  Limits:
    cpu: 500m
    memory: 1Gi
  Requests:
    cpu: 150m
    memory: 100Mi
  Environment: <none>
...
```

Установлены лимиты: CPU — 500m и RAM — 1 ГиБ и запросы на ресурсы: CPU — 150m и RAM — 100 МиБ.

Шаг 2. Создайте Vertical Pod Autoscaler

1. Создайте файл cloudru-vpa.yaml и сохраните следующую спецификацию:

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: cloudru-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: cloudru-nginx
  updatePolicy:
    updateMode: "Auto"
```

Где:

- `spec.targetRef.name` — название Deployment, для которого будет выполняться вертикальное масштабирование.
- `spec.updatePolicy.updateMode` — режим обновления запросов на ресурсы.

2. Выполните команду:

```sh
kubectl create -f cloudru-vpa.yaml
```

В результате будет создан объект Vertical Pod Autoscaler для Deployment cloudru-nginx.

3. Подождите несколько минут, пока cloudru-vpa пересоздаст поды.

Вы можете отслеживать создание новых подов. Для этого в терминале, отличном от терминала, на котором вы выполняли предыдущий шаг, выполните команду:

```sh
kubectl get --watch Pods -l app=cloudru-nginx
```

4. Выполните команду:

```sh
kubectl describe pod <pod_name>
```

Где `<pod_name>` — название нового пода.

Результат должен выглядеть примерно так:

```yaml
...
State: Running
Started: Wed, 14 Aug 2024 10:21:22 -0400
Ready: True
Restart Count: 0
Limits:
  cpu: 1166m
  memory: 2560Mi
Requests:
  cpu: 350m
  memory: 262144k
Environment: <none>
...
```

Мы видим, что VPA изменил:
- лимиты: CPU — 1166m и RAM — 2560 МиБ;
- запросы на ресурсы: CPU — 350m и RAM — 262144 КиБ.

Шаг 3. Удалите ресурсы

Если вы закончили работать с VPA, удалите созданные ресурсы.

1. Удалите cloudru-vpa:

```sh
kubectl delete vpa cloudru-vpa
```

При удалении VPA Deployment остается с существующими запросами.

2. Удалите Deployment:

```sh
kubectl delete deployment cloudru-nginx
```

Результат:

```sh
deployment.apps "cloudru-nginx" deleted
```

Поды удалятся вместе с Deployment.

3. Если необходимо, удалите кластер.