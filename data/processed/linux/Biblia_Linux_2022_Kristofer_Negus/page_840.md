---
source_image: page_840.png
page_number: 840
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.30
tokens: 7501
characters: 1810
timestamp: 2025-12-24T05:08:48.025463
finish_reason: stop
---

Pod Template:
    Labels:    app=kubernetes-bootcamp
    Containers:
        kubernetes-bootcamp:
            Image:        gcr.io/google-samples/kubernetes-bootcamp:v1
            Port:         <none>
            Host Port:    <none>
            Environment:  <none>
            Mounts:       <none>
            Volumes:      <none>
...

В развертывании kubernetes-bootcamp обратите внимание на то, что устанавливается один инстанс (replica) модуля, связанного с развертыванием. Развертывание выполняется в текущем пространстве имен, которое имеет значение default. Обратите внимание также на то, что для модулей по умолчанию не открыты порты и не смонтированы тома.

Информация о подах (модулях) развертывания

После выполнения развертывания вы можете запросить информацию о созданном из него поде и предоставить API Kubernetes виртуальной машины своей локальной системе через прокси-службу.

1. Предоставьте доступ к API Kubernetes локальной системе. Чтобы открыть прокси-сервер из вашей системы к API Kubernetes, работающему в Minikube (kubectl proxy), введите следующее:

$ kubectl proxy
Starting to serve on 127.0.0.1:8001

2. Запросите API Kubernetes. Откройте второй терминал и запросите API Kubernetes, работающий на Minikube, введя следующее:

$ curl http://localhost:8001/version
{
  "major": "1",
  "minor": "17",
  "gitVersion": "v1.17.2",
  "gitCommit": "59603c6e503c87169aea6106f57b9f242f64df89",
  "gitTreeState": "clean",
  "buildDate": "2020-01-18T23:22:30Z",
  "goVersion": "go1.13.5",
  "compiler": "gc",
  "platform": "linux/amd64"

3. Запросите информацию о поде. Имя модуля, используемого в этом развертывании, — это kubernetes-bootcamp, за которым следует уникальная строка символов. Введите команды, приведенные далее, чтобы вывести имя пода, а затем перечислить описание этого модуля: