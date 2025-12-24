---
source_image: page_379.png
page_number: 379
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.80
tokens: 7464
characters: 1528
timestamp: 2025-12-24T03:10:54.866987
finish_reason: stop
---

volumes:
    - name: dbdata
      persistentVolumeClaim:
        claimName: dbdata
  containers:
    - name: debugger
      image: busybox
      command: ['sleep', '3600']
      volumeMounts:
        - mountPath: "/data"
          name: dbdata

$ kubectl create -f pvc-inspect.yaml
pod/pvc-inspect created

$ kubectl get pods
NAME                   READY   STATUS    RESTARTS   AGE
canary-aqw8jtfo-f54b9749-q5wqj   1/1     Running   0          20m
pvc-inspect            1/1     Running   0          35s
redis-9946db5cc-8g6zz   1/1     Running   0          14m

С помощью команды kubectl exec открываем командную оболочку внутри модуля, чтобы просмотреть содержимое каталога /data:

$ kubectl exec -it pvc-inspect -- sh
/ # cd /data
/data # ls -la
total 24
drwx------  3 999 root 4096 Aug  3 17:57 .
drwxr-xr-x  1 root root 4096 Aug  3 18:08 ..
drwx------  2 999 root 16384 Aug  3 17:57 lost+found
/data # rm -rf lost\+found/
/data # exit

Обратите внимание на то, что каталог /data содержит подкаталог lost+found, который необходимо удалить.

Удаляем временный модуль:

$ kubectl delete pod pvc-inspect
pod "pvc-inspect" deleted

Снова создаем развертывание db, на этот раз успешно:

$ kubectl create -f db-deployment.yaml
deployment.extensions/db created

$ kubectl get pods
NAME                   READY   STATUS    RESTARTS   AGE
canary-aqw8jtfo-f54b9749-q5wqj   1/1     Running   0          23m
db-6b4fbb57d9-8h978             1/1     Running   0          19s
redis-9946db5cc-8g6zz           1/1     Running   0          17m