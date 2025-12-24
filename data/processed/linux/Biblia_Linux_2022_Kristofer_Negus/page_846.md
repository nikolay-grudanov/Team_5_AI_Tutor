---
source_image: page_846.png
page_number: 846
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.34
tokens: 7631
characters: 2262
timestamp: 2025-12-24T05:09:07.760419
finish_reason: stop
---

2. Масштабируйте реплики. Чтобы масштабировать развертывание до четырех наборов реплик, введите следующее:

$ kubectl scale deployments/kubernetes-bootcamp --replicas=4
deployment.extensions/kubernetes-bootcamp scaled

3. Проверьте новые реплики. Перечислите развертывания, чтобы убедиться, что теперь все четыре реплики готовы и доступны:

$ kubectl get deployments
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp 4/4     4            4           8m44s

4. Проверьте поды. Теперь должны быть запущены четыре модуля kubernetes-bootcamp, каждый с собственным IP-адресом внутри кластера. Чтобы убедиться в этом, введите следующую команду:

$ kubectl get pods -o wide
NAME                                      READY   STATUS    RESTARTS   AGE   IP
  NODE         NOMINATED NODE   READINESS GATES
kubernetes-bootcamp-5b4... 1/1   Running   0   8m43s   172.18.0.4
    minikube <none>           <none>
kubernetes-bootcamp-5b4... 1/1   Running   0   12s     172.18.0.8
    minikube <none>           <none>
kubernetes-bootcamp-5b4... 1/1   Running   0   12s     172.18.0.6
    minikube <none>           <none>
kubernetes-bootcamp-5b4... 1/1   Running   0   12s     172.18.0.7
    minikube <none>           <none>

5. Просмотрите сведения о развертывании. Чтобы просмотреть подробные сведения о репликах в развертывании, введите следующие данные:

$ kubectl describe deployments/kubernetes-bootcamp
Name:                 kubernetes-bootcamp
Namespace:             default
...
Replicas:             4 desired | 4 updated | 4 total | 4 available | 0 unavailable
...
NewReplicaSet:        kubernetes-bootcamp-5b48cfdcbd (4/4 replicas created)
Events:
  Type    Reason        Age   From                  Message
  ----    ------        ----  ----                  -------
  Normal  ScalingReplicaSet 17m  deployment-controller  Scaled up replica set kubernetes-bootcamp-5b48cfdcbd to 1
  Normal  ScalingReplicaSet 9m25s deployment-controller  Scaled up replica set kubernetes-bootcamp-5b48cfdcbd to 4

Проверка балансировщика нагрузки
Чтобы удостовериться, что трафик распределяется по всем четырем реплицированным модулям, используйте NodePort, а затем команду curl, убедившись, что несколько подключений к NodePort дают доступ к разным модулям.