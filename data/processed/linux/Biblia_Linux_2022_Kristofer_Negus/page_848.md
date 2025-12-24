---
source_image: page_848.png
page_number: 848
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.06
tokens: 7576
characters: 2347
timestamp: 2025-12-24T05:09:05.946028
finish_reason: stop
---

$ kubectl get deployments
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp 2/2     2            2           52m

$ kubectl get pods -o wide
NAME                                 READY   STATUS    RESTARTS   AGE   IP
NODE      NOMINATED NODE   READINESS GATES
kubernetes-bootcamp-5b4... 1/1   Running   0          8m43s   172.18.0.4
minikube <none> <none>
kubernetes-bootcamp-5b4... 1/1   Running   0          12s    172.18.0.8

На этом этапе уже понятно, как вручную запрашивать свой кластер Kubernetes различными способами, а также запускать развертывания, модули и реплики и работать с ними. Чтобы продолжить работу с более продвинутыми руководствами Kubernetes, вернитесь на главную страницу Kubernetes Tutorials (kubernetes.io/docs/tutorials/). Я также рекомендую сайт Kubernetes By Example, где содержится дополнительная информация об использовании Kubernetes (kubernetesby-example.com).

Корпоративная платформа Kubernetes с технологией OpenShift

Платформа Red Hat OpenShift Container Platform (www.openshift.com) — это продукт, предназначенный для предоставления корпоративной платформы Kubernetes, которая может использоваться для критически важных приложений. Как гибридная облачная платформа, OpenShift создана для развертывания и на пустом компьютере, и в облачных средах.

Kubernetes — это проект с открытым исходным кодом, который может быть построен и запущен огромным количеством способов, а продукты на базе Kubernetes, такие как OpenShift, предназначены для применения надежной поддерживаемой платформы, на которую может положиться бизнес. OpenShift также поставляется в различных вариантах, которые могут быть установлены в центре обработки данных и в облачных средах, таких как AWS и Azure, или просто использоваться из выделенного кластера OpenShift, поддерживаемого Red Hat.

Если заблокировать функции Kubernetes, которые Red Hat встраивает в OpenShift, их тщательно протестируют и проверят. Обучение и документация основаны на этих функциях. Кроме того, в систему можно встроить более сложные функции, которые соответствуют требованиям правительства или тесно интегрируются с различными облачными средами.

Благодаря интуитивно понятной веб-консоли Red Hat OpenShift становится проще в применении для пользователей, начинающих работать с Kubernetes. Пример консоли OpenShift показан на рис. 30.2.