---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__hpa.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 71.96
tokens: 10511
characters: 6762
timestamp: 2025-12-24T05:54:13.997389
finish_reason: stop
---

### Развертывание Deployment с горизонтальным масштабированием подов

В сценарии развернем Deployment с Apache и PHP, а затем зададим условия изменения количества подов в зависимости от нагрузки на виртуальный процессор:

• Пороговая нагрузка на виртуальный процессор — 60% от запрошенного на запуск контейнера.
• Минимальное количество реплик — 2.
• Максимальное количество реплик — 7.

Перед началом работы

1. Создайте кластер Managed Kubernetes и хотя бы одну группу узлов.
2. Установите плагин Metrics Server.
3. Подключитесь к кластеру Managed Kubernetes.

Шаг 1. Создайте Deployment

Сохраните следующую спецификацию в файл cloudru-php-apache.yaml:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudru-php-apache
spec:
  replicas: 3
  selector:
    matchLabels:
      run: cloudru-php-apache
  template:
    metadata:
      labels:
        run: cloudru-php-apache
    spec:
      containers:
      - name: hpa-example
        image: mks.registry.smk.mbercloud.dev/hpa-example
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "250m"
---
apiVersion: v1
kind: Service
metadata:
  name: cloudru-php-apache
  labels:
    run: cloudru-php-apache
spec:
  ports:
  - port: 80
  selector:
    run: cloudru-php-apache
```

Обязательно укажите параметр resources.requests.cpu — запрос CPU для запуска контейнера, чтобы выполнять автоматическое масштабирование на основе использования ресурса в процентах.

Выполните команду:

```sh
kubectl create -f cloudru-php-apache.yaml
```

Если команда выполнена успешно, появится сообщение:

```sh
deployment.apps/cloudru-php-apache created
```

Шаг 2. Создайте Horizontal Pod Autoscaler одним из способов

Способ 1

Сохраните следующую спецификацию в файл cloudru-hpa.yaml:

```yaml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: cloudru-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: cloudru-php-apache
  minReplicas: 2
  maxReplicas: 7
  targetCPUUtilizationPercentage: 60
```

Затем выполните команду:

```sh
kubectl create -f cloudru-hpa.yaml
```

Способ 2

Выполните команду:

```sh
kubectl autoscale deployment cloudru-php-apache --cpu-percent=60 --min=2 --max=7
```

В результате будет создан Horizontal Pod Autoscaler для Deployment cloudru-php-apache.

При нагрузке на виртуальный процессор:

• выше 60% от запрошенной нагрузки на каждый контейнер — количество подов будет постепенно увеличиваться, пока не достигнет семи;
• ниже 60% от запрошенной нагрузки на каждый контейнер — количество подов будет постепенно уменьшаться, пока не достигнет двух.

Для горизонтального масштабирования подов можно использовать не только метрики CPU, но и RAM. В этом случае для создания НРА используйте следующую спецификацию:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: cloudru-php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: cloudru-php-apache
  minReplicas: 2
  maxReplicas: 7
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 60
  - type: Resource
    resource:
      name: memory
      target:
        type: AverageValue
        averageValue: 500Mi
```

При увеличении нагрузки на виртуальный процессор выше 60% от запрошенной нагрузки на каждый контейнер и занятой оперативной памяти более 500 Мб, количество подов будет увеличиваться, пока не достигнет семи подов.

При уменьшении нагрузки на виртуальный процессор ниже 60% от запрошенной нагрузки на каждый контейнер и занятой оперативной памяти менее 500 Мб, количество подов будет уменьшаться, пока не достигнет двух подов.

Шаг 3. Получите список НРА в кластере

Выполните команду:

```sh
kubectl get hpa
```

Ответ будет содержать следующее:

<table>
  <tr>
    <th>NAME</th>
    <th>REFERENCE</th>
    <th>TARGETS</th>
    <th>MINPODS</th>
    <th>MAXPODS</th>
    <th>REPLICAS</th>
    <th>AGE</th>
  </tr>
  <tr>
    <td>cloudru-php-apache</td>
    <td>Deployment/cloudru-php-apache</td>
    <td>60%/60%</td>
    <td>2</td>
    <td>7</td>
    <td>3</td>
    <td>12h</td>
  </tr>
</table>

Шаг 4. Создайте нагрузку для веб-сервера

Выполните команду:

```sh
kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01;"
```

Чтобы наблюдать за масштабированием, периодически запускайте следующую команду в терминале, отличном от терминала, на котором вы выполняли предыдущий шаг:

```sh
kubectl get hpa cloudru-php-apache --watch
```

Ответ будет содержать следующее:

<table>
  <tr>
    <th>NAME</th>
    <th>REFERENCE</th>
    <th>TARGETS</th>
    <th>MINPODS</th>
    <th>MAXPODS</th>
    <th>REPLICAS</th>
    <th>AGE</th>
  </tr>
  <tr>
    <td>cloudru-php-apache</td>
    <td>Deployment/cloudru-php-apache</td>
    <td>200%/60%</td>
    <td>2</td>
    <td>7</td>
    <td>3</td>
    <td>5m34s</td>
  </tr>
</table>

Так как потребление процессора возросло до 200% от запрошенного, количество реплик было увеличено до 5:

<table>
  <tr>
    <th>NAME</th>
    <th>REFERENCE</th>
    <th>TARGETS</th>
    <th>MINPODS</th>
    <th>MAXPODS</th>
    <th>REPLICAS</th>
    <th>AGE</th>
  </tr>
  <tr>
    <td>cloudru-php-apache</td>
    <td>Deployment/cloudru-php-apache</td>
    <td>200%/60%</td>
    <td>2</td>
    <td>7</td>
    <td>5</td>
    <td>7m</td>
  </tr>
</table>

Увеличение количества подов может занять несколько минут.

Шаг 5. Остановите нагрузку для веб-сервера

Чтобы завершить генерацию нагрузки, в терминале, где вы создали под, запускающий образ busybox, нажмите Ctrl + C.

Затем через несколько минут выполните команду:

```sh
kubectl get hpa cloudru-php-apache --watch
```

Результат:

<table>
  <tr>
    <th>NAME</th>
    <th>REFERENCE</th>
    <th>TARGETS</th>
    <th>MINPODS</th>
    <th>MAXPODS</th>
    <th>REPLICAS</th>
    <th>AGE</th>
  </tr>
  <tr>
    <td>cloudru-php-apache</td>
    <td>Deployment/cloudru-php-apache</td>
    <td>0%/60%</td>
    <td>2</td>
    <td>7</td>
    <td>1</td>
    <td>10m</td>
  </tr>
</table>

Шаг 6. Удалите ресурсы

Если вы закончили работать с НРА, удалите созданные ресурсы.

1. Удалите cloudru-hpa:

```sh
kubectl delete hpa cloudru-hpa cloudru-php-apache
```

При удалении НРА Deployment остается в существующем масштабе и не возвращается к количеству реплик, указанному в исходной спецификации Deployment.

Если необходимо, измените количество реплик, например, до трех:

```sh
kubectl scale deployment cloudru-php-apache --replicas=3
```

2. Удалите Deployment:

```sh
kubectl delete deployment cloudru-php-apache
```

Результат:

```sh
deployment.apps "cloudru-php-apache" deleted
```

Поды удалятся вместе с Deployment.

3. Если необходимо, удалите кластер.