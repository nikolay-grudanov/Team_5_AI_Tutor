---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__app-in-karmada.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 64.24
tokens: 10323
characters: 7420
timestamp: 2025-12-24T05:51:49.256983
finish_reason: stop
---

### Развертывание nginx в кластерах-участниках Karmada

С помощью этого руководства вы развернете приложение nginx в кластерах-участниках платформы Karmada с помощью политики распространения ресурсов. В результате вы получите опыт централизованного управления несколькими кластерами Kubernetes, настройки политик распределения ресурсов и проверки корректности работы приложения во всех выбранных кластерах. Доступ к nginx будет предоставляться только внутри кластера для целей демонстрации. Настройка сетевой связанности между кластерами-участниками в рамках этого сценария не выполняется.

Вы будете использовать следующие сервисы:

• Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
• Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для управления и подключения к кластерам Kubernetes.
• Karmada — Kubernetes-совместимая платформа для централизованного управления и оркестрации приложений в мультикластерной инфраструктуре.

Шаги:

1. Создайте манифест для развертывания nginx
2. Настройте политику распространения ресурсов Karmada
3. Примените манифесты через control-plane Karmada
4. Проверьте развертывание и статус ресурсов
5. Проверьте работу nginx в кластерах-участниках

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Разверните платформу Karmada по инструкции. Убедитесь, что k8s-кластеры evo1 и evo2 подключены как кластеры-участники в control-plane Karmada и доступны для дальнейшей работы.

1. Создайте манифест для развертывания nginx

Создайте Kubernetes-манифесты для развертывания nginx и сервиса типа ClusterIP. Эти манифесты будут основой для дальнейшего управления их распространением через Karmada.

1. Создайте директорию `nginx-manifests` в домашней директории пользователя:

```sh
mkdir $HOME/nginx-manifests
```

2. Создайте файл `nginx-deployment.yaml` со следующим содержимым:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: default
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
          resources:
            requests:
              memory: "64Mi"
              cpu: "100m"
            limits:
              memory: "128Mi"
              cpu: "200m"
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  namespace: default
  labels:
    app: nginx
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
  - name: http
    port: 80
    targetPort: 80
    protocol: TCP
```

Этот манифест создает в Kubernetes два ресурса:
• Deployment с одной репликой контейнера nginx и ограничениями по ресурсам на pod.
• Service типа ClusterIP для доступа к приложению nginx внутри кластера Kubernetes.

3. Проверьте содержимое созданного файла:

```sh
cat $HOME/nginx-manifests/nginx-deployment.yaml
```

Команда должна вывести YAML-манифесты Deployment и Service, которые были записаны на предыдущем шаге.

2. Настройте политику распространения ресурсов Karmada

На этом этапе опишите политику распространения ресурсов (PropagationPolicy) для управления автоматическим размещением развертываемых ресурсов nginx в кластерах-участниках Karmada.

1. В директории манифестов создайте файл `nginx-propagation-policy.yaml` со следующим содержимым:

```yaml
apiVersion: policy.karmada.io/v1alpha1
kind: PropagationPolicy
metadata:
  name: nginx-propagation-policy
  namespace: default
spec:
  resourceSelectors:
  - apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  - apiVersion: v1
    kind: Service
    name: nginx-service
  placement:
    clusterAffinity:
      clusterNames:
      - evo1
      - evo2
  replicaScheduling:
    replicaSchedulingType: Duplicated
```

Параметры политики распространения определяют:
• `resourceSelectors` — какие ресурсы (Deployment и Service nginx) распространять из control-plane Karmada;
• `clusterAffinity` — список кластеров (evo1 и evo2), в которые отправлять ресурсы;
• `replicaSchedulingType: Duplicated` — дублировать ресурсы во все указанные кластеры (дополнительно смотрите возможные режимы в документации Karmada: Duplicated или Weighted).

2. Проверьте содержимое файла политики:

```sh
cat $HOME/nginx-manifests/nginx-propagation-policy.yaml
```

3. Примените манифесты через control-plane Karmada

Теперь создайте ресурсы Deployment и Service в control-plane Karmada и включите их распространение в кластеры-участники с помощью PropagationPolicy.

1. Убедитесь, что вы подключены к control-plane Karmada:

```sh
karmadactl --karmada-context karmada-apiserver get clusters
```

Команда должна вывести список кластеров-участников Karmada (ожидаются evo1 и evo2).
2. Примените манифест развертывания nginx:

```sh
karmadactl --karmada-context karmada-apiserver apply -f $HOME/nginx-manifests/nginx-deployment.yaml
```

На этом этапе ресурсы Deployment и Service будут созданы в control-plane, но еще не распространены в кластеры-участники.
3. Примените политику распространения PropagationPolicy:

```sh
karmadactl --karmada-context karmada-apiserver apply -f $HOME/nginx-manifests/nginx-propagation-policy.yaml
```

После выполнения команды начнется процесс распространения ресурсов nginx в указанные кластеры-участники согласно правилам размещения.

4. Проверьте развертывание и статус ресурсов

Проверьте, что Karmada корректно распространила ресурсы nginx на все целевые кластеры, а сервисы и поды работают должным образом.

1. Проверьте список развертываний:

```sh
karmadactl --karmada-context karmada-apiserver get deployments
```

2. Проверьте статус подов nginx во всех кластерах-участниках:

```sh
karmadactl --karmada-context karmada-apiserver get pods --operation-scope members
```

Эта команда выведет все поды во всех кластерах-участниках и позволит увидеть, как распределена нагрузка.
3. Проверьте наличие и статусы сервисов nginx:

```sh
karmadactl --karmada-context karmada-apiserver get services --operation-scope members
```

В результатах должны отображаться сервисы nginx во всех кластерах-участниках.
4. Проверьте политику распространения ресурсов:

```sh
karmadactl --karmada-context karmada-apiserver get propagationpolicy nginx-propagation-policy -o yaml
```

Эта команда отобразит конфигурацию вашей политики распространения и текущий статус доставки ресурсов в кластеры.

5. Проверьте работу nginx в кластерах-участниках

Теперь проверьте, что приложение nginx корректно функционирует в каждом из кластеров evo1 и evo2, и сервис доступен на уровне кластера.

1. Проверьте работу nginx в кластере evo1, выполнив команду:

```sh
kubectl --kubeconfig $HOME/join-clusters/evo1 run curl --rm -i --restart=Never --image=curlimages/curl
```

В ответе должна отобразиться страница приветствия nginx по умолчанию, что свидетельствует о корректном функционировании сервиса.
2. Проверьте работу nginx в кластере evo2 аналогичной командой:

```sh
kubectl --kubeconfig $HOME/join-clusters/evo2 run curl --rm -i --restart=Never --image=curlimages/curl
```

Результат

Вы развернули приложение nginx с помощью централизованной платформы Karmada, создали политику автоматического распределения ресурсов и проверили работу развернутого сервиса в каждом из целевых кластеров.