---
source_image: page_484.png
page_number: 484
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.00
tokens: 7299
characters: 1292
timestamp: 2025-12-24T03:13:34.562839
finish_reason: stop
---

tasks = []
LOG.info(f"sending aysnc events TOTAL {count}", extra=extra_msg)
num = 0
for _ in range(count):
    tasks.append(asyncio.ensure_future(put_record(gen_uuid_events(),
        client)))
    LOG.info(f"sending aysnc events: COUNT {num}/{count}")
    num +=1
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end = time.time()
LOG.info("Total time: {}".format(end - start))

Kinesis Data Firehose получает захваченные данные и непрерывно перенаправляет их в произвольное количество точек назначения: Amazon S3, Amazon Redshift, сервис Amazon Elasticsearch или какие-либо сторонние сервисы наподобие Splunk. В качестве альтернативы Kinesis с открытым исходным кодом можно рассматривать Apache Kafka. Apache Kafka работает на основе схожих принципов архитектуры обмена сообщениями по типу «издатель/подписчик».

Ситуационный анализ: создание доморощенного конвейера данных

Давным-давно, в начале 2000-х, когда Ной работал техническим директором и главным менеджером стартапа, он столкнулся с задачей создания первого в компании конвейера машинного обучения и обработки данных. Примерный эскиз получившегося приведен на следующей схеме конвейера данных Jenkins (рис. 15.6).

![Конвейер данных Jenkins](../images/chapter_15/jenkins_pipeline.png)

Рис. 15.6. Конвейер данных Jenkins