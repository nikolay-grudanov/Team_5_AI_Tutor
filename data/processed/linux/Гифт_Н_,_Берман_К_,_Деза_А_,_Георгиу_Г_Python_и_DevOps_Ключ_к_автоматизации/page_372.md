---
source_image: page_372.png
page_number: 372
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.30
tokens: 7251
characters: 1567
timestamp: 2025-12-24T03:10:36.836331
finish_reason: stop
---

kompose.version: 1.16.0 (0c01309)
creationTimestamp: null
labels:
    io.kompose.service: app
name: app
spec:
    replicas: 1
    strategy: {}
    template:
        metadata:
            creationTimestamp: null
            labels:
                io.kompose.service: app
        spec:
            initContainers:
            - args:
                - manage.py
                - db
                - upgrade
            env:
                - name: APP_SETTINGS
                  value: config.ProductionConfig
                - name: DBPASS
                  valueFrom:
                    secretKeyRef:
                      name: fbe-secret
                      key: dbpass
                - name: DATABASE_URL
                  value: postgresql://wordcount_dbadmin:${DBPASS}@db/wordcount
            image: griggheo/flask-by-example:v1
            name: migrations
            resources: {}
            containers:
            - args:
                - manage.py
                - runserver
                - --host=0.0.0.0
            env:
                - name: APP_SETTINGS
                  value: config.ProductionConfig
                - name: DBPASS
                  valueFrom:
                    secretKeyRef:
                      name: fbe-secret
                      key: dbpass
                - name: DATABASE_URL
                  value: postgresql://wordcount_dbadmin:${DBPASS}@db/wordcount
                - name: REDISTOGO_URL
                  value: redis://redis:6379
            image: griggheo/flask-by-example:v1
            name: app