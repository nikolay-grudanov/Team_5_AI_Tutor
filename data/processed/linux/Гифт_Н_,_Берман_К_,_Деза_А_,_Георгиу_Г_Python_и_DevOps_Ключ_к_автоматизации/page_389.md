---
source_image: page_389.png
page_number: 389
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.20
tokens: 7341
characters: 1621
timestamp: 2025-12-24T03:11:04.716572
finish_reason: stop
---

$ kubectl describe pod prometheus-server-779ffd445f-4llqr -nmonitoring
OUTPUT OMITTED
    Args:
    --storage.tsdb.retention.time=30d
    --config.file=/etc/config/prometheus.yml
    --storage.tsdb.path=/data
    --web.console.libraries=/etc/prometheus/console_libraries
    --web.console.templates=/etc/prometheus/consoles
    --web.enable-lifecycle

Удаление кластера GKE

Очистка используемых для тестирования ресурсов, которые больше не нужны, окупается буквально сторицей. В противном случае в конце месяца вас может ждать неприятный сюрприз в виде счета от поставщика облачных сервисов.

Удалить кластер GKE можно с помощью команды pulumi destroy:

$ pulumi destroy

Previewing destroy (dev):

    Type                Name                Plan
- pulumi:pulumi:Stack pythonfordevops-gke-pulumi-dev delete
- ├── kubernetes:core:Service ingress           delete
- ├── kubernetes:apps:Deployment canary          delete
- ├── pulumi:providers:kubernetes gke_k8s         delete
- ├── gcp:container:Cluster   gke-cluster        delete
- └── random:index:RandomString password         delete

Resources:
    - 6 to delete

Do you want to perform this destroy? yes
Destroying (dev):

    Type                Name                Status
- pulumi:pulumi:Stack pythonfordevops-gke-pulumi-dev deleted
- ├── kubernetes:core:Service ingress           deleted
- ├── kubernetes:apps:Deployment canary          deleted
- ├── pulumi:providers:kubernetes gke_k8s         deleted
- ├── gcp:container:Cluster   gke-cluster        deleted
- └── random:index:RandomString password         deleted

Resources:
    - 6 deleted

Duration: 3m18s