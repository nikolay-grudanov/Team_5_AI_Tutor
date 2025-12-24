---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__time-slicing.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.86
tokens: 8831
characters: 5416
timestamp: 2025-12-24T05:56:58.469700
finish_reason: stop
---

### Настройка Time-Slicing GPU

NVIDIA GPU Operator поддерживает возможность настройки Time-Slicing — механизма виртуального разделения одной физической GPU между несколькими подами на уровне рабочего узла.

Например, если на узле установлена одна GPU V100, а в кластере есть пять подов, каждый из которых запрашивает всю GPU, то без использования Time-Slicing на узел будет назначен только один под. Остальные останутся в статусе «Pending» из-за нехватки ресурсов. При включении Time-Slicing ресурсы одной физической GPU делятся между пятью подами.

Таким образом, все пять подов смогут быть запущены на одном узле одновременно, несмотря на то, что физически доступна только одна GPU.

В сценарии настроим Time-Slicing, развернем пять реплик приложения, которое требует для своей работы GPU-ресурсов, проверим состояние подов и логи.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте кластер Managed Kubernetes.
3. В кластере создайте группу узлов с параметрами для GPU:
   a. Графический процессор (GPU) — активно.
   b. Модель GPU — GPU NVIDIA Tesla V100.
   c. GPU — 1.
      По умолчанию в Managed Kubernetes установлена нулевая квота на создание узлов с GPU. Чтобы запросить увеличение квоты, обратитесь в техническую поддержку.
4. Подключитесь к кластеру Managed Kubernetes.

Шаг 1. Настойте Time-Slicing

1. Создайте пространство имен gpu-operator:

   ```
   kubectl create ns gpu-operator
   ```

2. Перезапишите метку:

   ```
   kubectl label --overwrite ns gpu-operator pod-security.kubernetes.io/enforce=privileged
   ```

3. Создайте файл cloudru-time-slicing.yaml со следующим содержимым:

   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: time-slicing-config
     namespace: gpu-operator
   data:
     tenla-v100: |
       version: v1
       sharing:
         timeSlicing:
           resources:
             - name: nvidia.com/gpu
               replicas: 5

4. Выполните команду:

   ```
   kubectl apply -f cloudru-time-slicing.yaml
   ```

Результат:

   configmap/time-slicing-config created

5. Проверьте статус:

   ```
   kubectl get cm time-slicing-config -n gpu-operator
   ```

Результат:

   NAME                DATA   AGE
   time-slicing-config  1      114s

В дополнение к стандартным меткам, которые применяются к узлам после настройки Time-Slicing, для узла применяется метка:

   nvidia.com/gpu.replicas = <replicas-count>

Здесь <replicas-count> указывает, сколько раз выделенный ресурс gpu может быть переподписан на узле.

Также по умолчанию модифицируется метка nvidia.com/gpu.product :

   nvidia.com/gpu.product = <product-name>-SHARED

Суффикс -SHARED помогает отличать узлы с поддержкой Time-Slicing.

Шаг 2. Установите NVIDIA GPU Operator

Личный кабинет    API

1. В личном кабинете перейдите в кластер, для которого создали группу узлов с GPU.
2. Перейдите в раздел Плагины и справа над списком установленных плагинов нажмите Добавить плагин.
3. Выберите NVIDIA GPU Operator.
4. Нажмите Установить.
5. В разделе Расширенная конфигурация → YAML укажите параметры:

   devicePlugin:
     config:
       name: time-slicing-config
       default: tenla-v100

6. Нажмите Установить.

Дождитесь, когда состояние плагина изменится на «Установлен».

Шаг 3. Протестируйте настройку Time-Slicing

1. Создайте файл cloudru-time-slicing-check.yaml со следующим содержимым:

   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: cloudru-time-slicing-check
   labels:
     app: cloudru-time-slicing-check
   spec:
     replicas: 5
     selector:
       matchLabels:
         app: cloudru-time-slicing-check
     template:
       metadata:
         labels:
           app: cloudru-time-slicing-check
       spec:
         tolerations:
           - key: nvidia.com/gpu
             operator: Exists
             effect: NoSchedule
         hostPID: true
         containers:
           - name: cuda-sample-vector-add
             image: "nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cudatoolkit7.1-ubuntu20.04"
             args:
               - while true; do /cuda-samples/vectorAdd; done
             resources:
               limits:
                 nvidia.com/gpu: 1

2. Выполните команду:

   ```
   kubectl apply -f cloudru-time-slicing-check.yaml
   ```

Результат:

   deployment.apps/cloudru-time-slicing-check created

3. Проверьте, что все пять реплик в статусе «Running»:

   ```
   kubectl get pods
   ```

Примерный результат:

   NAME                                 READY   STATUS    RESTARTS   AGE
   cloudru-time-slicing-check-6dce7495bc-6dr4k   1/1     Running   0          6m25s
   cloudru-time-slicing-check-6dce7495bc-7vdwv   1/1     Running   0          6m25s
   cloudru-time-slicing-check-6dce7495bc-3jxdr   1/1     Running   0          6m25s
   cloudru-time-slicing-check-6dce7495bc-xhxd9   1/1     Running   0          6m25s
   cloudru-time-slicing-check-6dce7495bc-zxux8   1/1     Running   0          6m25s

4. Посмотрите логи одного из подов:

   ```
   kubectl logs deploy/cloudru-time-slicing-check
   ```

Примерный результат:

   Found 5 pods, using pod/cloudru-time-slicing-check-6dce7495bc-7vdwv
   [Vector addition of 50000 elements]
   Copy input data from the host memory to the CUDA device
   CUDA kernel launch with 196 blocks of 256 threads
   Copy output data from the CUDA device to the host memory
   Test PASSED
   ...