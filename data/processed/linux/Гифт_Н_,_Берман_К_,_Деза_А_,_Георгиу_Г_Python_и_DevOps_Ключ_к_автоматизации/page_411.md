---
source_image: page_411.png
page_number: 411
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.76
tokens: 7522
characters: 1744
timestamp: 2025-12-24T03:11:49.096469
finish_reason: stop
---

Генерируем случайный пароль для минимальной аутентификации шлюза OpenFaaS:

$ PASSWORD=$(head -c 12 /dev/urandom | shasum| cut -d' ' -f1)

$ kubectl -n openfaas create secret generic basic-auth \
--from-literal=basic-auth-user=admin \
--from-literal=basic-auth-password="$PASSWORD"
secret/basic-auth created

Развертываем OpenFaaS путем установки чарта Helm:

$ helm repo update \
&& helm upgrade openfaas --install openfaas/openfaas \
    --namespace openfaas \
    --set basic_auth=true \
    --set serviceType=LoadBalancer \
    --set functionNamespace=openfaas-fn

ВЫВОД ОПУЩЕН

NOTES:
To verify that openfaas has started, run:
kubectl --namespace=openfaas get deployments -l "release=openfaas,app=openfaas"

Подобную минимальную аутентификацию без TLS следует использовать только для экспериментов/изучения. Любую более или менее важную среду нужно настроить так, чтобы учетные данные передавались через защищенное TLS-соединение.

Проверяем, какие сервисы запущены в пространстве имен openfaas:

$ kubectl get service -n openfaas
NAME                TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)
alertmanager        ClusterIP      10.43.193.61   <none>        9093/TCP
basic-auth-plugin   ClusterIP      10.43.83.12    <none>        8080/TCP
gateway             ClusterIP      10.43.7.46     <none>        8080/TCP
gateway-external    LoadBalancer   10.43.91.91    10.0.0.185    8080:31408/TCP
nats                ClusterIP      10.43.33.153   <none>        4222/TCP
prometheus          ClusterIP      10.43.122.184  <none>        9090/TCP

Выполняем перенаправление с порта 8080 удаленного инстанса на локальный порт 8080:

$ kubectl port-forward -n openfaas svc/gateway 8080:8080 &
[1] 29183
Forwarding from 127.0.0.1:8080 -> 8080