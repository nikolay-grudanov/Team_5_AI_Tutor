---
source_image: page_924.png
page_number: 924
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.18
tokens: 7124
characters: 627
timestamp: 2025-12-24T05:10:45.927700
finish_reason: stop
---

8. Чтобы получить IP-адрес вашего инструмента Minikube и номер порта открытой службы hello-node, введите следующее:

$ minikube ip
192.168.39.150
$ kubectl describe service hello-node | grep NodePort
NodePort:           <unset>   31302/TCP

9. Примените команду curl для запроса службы hello-node, используя IP-адрес и номер порта из предыдущего пункта, например:
$ curl 192.168.39.105:31302
Hello World!

10. Чтобы удалить службу hello-node и ее развертывание, а затем остановить виртуальную машину Minikube, введите следующие данные:

$ kubectl delete service hello-node
$ kubectl delete deployment hello-node
$ minikube stop