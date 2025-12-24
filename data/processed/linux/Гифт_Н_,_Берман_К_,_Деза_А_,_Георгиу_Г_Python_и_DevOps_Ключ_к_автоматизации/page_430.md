---
source_image: page_430.png
page_number: 430
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.20
tokens: 7684
characters: 1945
timestamp: 2025-12-24T03:12:24.297102
finish_reason: stop
---

Запускаем локальный образ Docker и монтируем локальный каталог artifacts внутри контейнера Docker в качестве каталога /tmp/artifacts:

$ docker run --rm -d \
--env BASE_URL=https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod \
-v `pwd`/artifacts:/tmp/artifacts cdk-loadtest

Производим отладку сценария Molotov, изучая файл artifacts/molotov.out.

Результаты работы Taurus можно просмотреть либо с помощью команды docker logs CONTAINER_ID, либо просто изучая содержимое файла artifacts/bzt.log.

Результаты изучения журнала Docker:

$ docker logs -f a228f8f9a2bc
19:26:26 INFO: Taurus CLI Tool v1.13.8
19:26:26 INFO: Starting with configs: ['/bzt-configs/taurus.yaml']
19:26:26 INFO: Configuring...
19:26:26 INFO: Artifacts dir: /tmp/artifacts
19:26:26 INFO: Preparing...
19:26:27 INFO: Starting...
19:26:27 INFO: Waiting for results...
19:26:32 INFO: Changed data analysis delay to 3s
19:26:32 INFO: Current: 0 vu 1 succ 0 fail 0.546 avg rt /
Cumulative: 0.546 avg rt, 0% failures
19:26:39 INFO: Current: 1 vu 1 succ 0 fail 1.357 avg rt /
Cumulative: 0.904 avg rt, 0% failures
ETC
19:41:00 WARNING: Please wait for graceful shutdown...
19:41:00 INFO: Shutting down...
19:41:00 INFO: Post-processing...
19:41:03 INFO: Test duration: 0:14:33
19:41:03 INFO: Samples count: 1857, 0.00% failures
19:41:03 INFO: Average times: total 6.465, latency 0.000, connect 0.000
19:41:03 INFO: Percentiles:
+----------------+--------------+
| Percentile, % | Resp. Time, s |
+----------------+--------------+
|      0.0      |      0.13   |
|     50.0      |      1.66   |
|     90.0      |     14.384  |
|     95.0      |     26.88   |
|     99.0      |     27.168  |
|    99.9       |     27.584  |
|    100.0      |     27.792  |
+----------------+--------------+

Создайте инструментальные панели для длительности выполнения функции Lambda (рис. 13.1) и выделяемых и потребляемых единиц пропускной способности по чтению/записи DynamoDB (рис. 13.2).