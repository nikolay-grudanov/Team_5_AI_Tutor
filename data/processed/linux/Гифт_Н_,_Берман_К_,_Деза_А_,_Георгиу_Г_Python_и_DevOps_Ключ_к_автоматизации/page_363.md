---
source_image: page_363.png
page_number: 363
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.15
tokens: 7325
characters: 1255
timestamp: 2025-12-24T03:10:14.785279
finish_reason: stop
---

postgres=# \q

$ kubectl exec -it db-67659d85bf-vrnw7 -- psql -U postgres wordcount
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

wordcount=# CREATE ROLE wordcount_dbadmin;
CREATE ROLE
wordcount=# ALTER ROLE wordcount_dbadmin LOGIN;
ALTER ROLE
wordcount=# ALTER USER wordcount_dbadmin PASSWORD 'MYPASS';
ALTER ROLE
wordcount=# \q

Следующий шаг — создание соответствующего развертыванию db объекта Service, благодаря которому развертывание станет видимым для остальных сервисов, работающих в данном кластере, например для сервиса-исполнителя Redis и основного сервиса приложения. Файл манифеста для сервиса db выглядит вот так:

$ cat db-service.yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    kompose.cmd: kompose convert
    kompose.version: 1.16.0 (0c01309)
  creationTimestamp: null
  labels:
    io.kompose.service: db
  name: db
spec:
  ports:
  - name: "5432"
    port: 5432
    targetPort: 5432
  selector:
    io.kompose.service: db
status:
  loadBalancer: {}

Стоит обратить внимание на следующий раздел:

  labels:
    io.kompose.service: db

Он присутствует как в манифесте развертывания, так и в манифесте сервиса и, собственно, связывает их между собой. Сервис связывается с любым развертыванием с той же меткой.