---
source_image: page_369.png
page_number: 369
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.04
tokens: 7742
characters: 2367
timestamp: 2025-12-24T03:10:56.573087
finish_reason: stop
---

Events:
<table>
  <tr>
    <th>Type</th>
    <th>Reason</th>
    <th>Age</th>
    <th>From</th>
    <th>Message</th>
  </tr>
  <tr>
    <td>Normal</td>
    <td>Scheduled</td>
    <td>2m51s</td>
    <td>default-scheduler</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="5">Successfully assigned default/worker-7dbf5ff56c-vgs42 to minikube</td>
  </tr>
  <tr>
    <td>Normal</td>
    <td>Pulling</td>
    <td>76s (x4 over 2m50s)</td>
    <td>kubelet, minikube</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="5">Pulling image "griggheo/flask-by-example:v1"</td>
  </tr>
  <tr>
    <td>Warning</td>
    <td>Failed</td>
    <td>75s (x4 over 2m49s)</td>
    <td>kubelet, minikube</td>
    <td>Failed to pull image "griggheo/flask-by-example:v1": rpc error: code = Unknown desc = Error response from daemon: pull access denied for griggheo/flask-by-example, repository does not exist or may require 'docker login'</td>
  </tr>
  <tr>
    <td>Warning</td>
    <td>Failed</td>
    <td>75s (x4 over 2m49s)</td>
    <td>kubelet, minikube</td>
    <td>Error: ErrImagePull</td>
  </tr>
  <tr>
    <td>Warning</td>
    <td>Failed</td>
    <td>62s (x6 over 2m48s)</td>
    <td>kubelet, minikube</td>
    <td>Error: ImagePullBackOff</td>
  </tr>
  <tr>
    <td>Normal</td>
    <td>BackOff</td>
    <td>51s (x7 over 2m48s)</td>
    <td>kubelet, minikube</td>
    <td>Back-off pulling image "griggheo/flask-by-example:v1"</td>
  </tr>
</table>

Развертывание попыталось извлечь частный образ Docker griggheo/flask-by-example:v1 без необходимых для доступа к частному реестру Docker учетных данных. В Kubernetes есть специальный тип объектов как раз для такого сценария — imagePullSecret.

Создаем с помощью sops зашифрованный файл, содержащий учетные данные Docker Hub и вызов kubectl create secret:

$ sops --pgp E14104A0890994B9AC9C9F6782C1FF5E679EFF32 \
create_docker_credentials_secret.sh.enc

Содержимое файла выглядит вот так:

DOCKER_REGISTRY_SERVER=docker.io
DOCKER_USER=Type your dockerhub username, same as when you `docker login`
DOCKER_EMAIL=Type your dockerhub email, same as when you `docker login`
DOCKER_PASSWORD=Type your dockerhub pw, same as when you `docker login`

kubectl create secret docker-registry myregistrykey \
--docker-server=$DOCKER_REGISTRY_SERVER \
--docker-username=$DOCKER_USER \
--docker-password=$DOCKER_PASSWORD \
--docker-email=$DOCKER_EMAIL