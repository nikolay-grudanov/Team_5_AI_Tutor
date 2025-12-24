---
source_image: page_845.png
page_number: 845
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.67
tokens: 7491
characters: 1902
timestamp: 2025-12-24T05:08:50.397886
finish_reason: stop
---

Удаление службы

Если вы закончили пользоваться службой, ее можно удалить. Следующий процесс удаляет доступ к службе из порта узла, но не удаляет само развертывание.

1. Проверьте службу. Убедитесь, что служба kubernetes-bootcamp все еще существует:

$ kubectl get services
NAME                TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)
AGE
kubernetes          ClusterIP      10.96.0.1      <none>        443/TCP
63m
kubernetes-bootcamp NodePort      10.96.66.230   <none>        8/TCP 30m

2. Удалите службу. Используя имя метки, удалите службу:

$ kubectl delete service -l run=kubernetes-bootcamp
service "kubernetes-bootcamp" deleted

3. Проверьте службу и развертывание. Убедитесь, что служба удалена, но развертывание на месте:

$ kubectl get services
NAME                TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)
AGE
kubernetes          ClusterIP      10.96.0.1      <none>        443/TCP
64m
$ kubectl get deployment
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp 1/1     1            1           65m

Масштабирование приложения

Одна из самых мощных функций Kubernetes — его способность масштабировать приложение по мере необходимости. Этот процесс начинается с развертывания kubernetes-bootcamp, которое запускает один модуль и масштабирует его, чтобы добавить дополнительные модули, работающие с использованием функции ReplicaSet и других средств предоставления приложению внешнего доступа.

1. Найдите развертывание. Перечислите информацию о развертывании kubernetes-bootcamp и обратите внимание на то, что оно настроено на активацию только одного набора реплик (rs):

$ kubectl get deployments
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp 1/1     1            1           107s
$ kubectl get rs
NAME                DESIRED   CURRENT   READY   AGE
kubernetes-bootcamp-5b48cfdbd 1         1         1       3m4s