---
source_image: page_497.png
page_number: 497
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.38
tokens: 7230
characters: 1026
timestamp: 2025-12-24T03:13:47.931212
finish_reason: stop
---

LOG.info(f"Deleted SQS receipt_handle {receipt_handle} with res {res}", extra=extra_logging)

# Создаем объект DataFrame Pandas с фрагментами из "Википедии"
LOG.info(f"Creating dataframe with values: {names}")
df = names_to_wikipedia(names)

# Анализируем тональности
df = apply_sentiment(df)
LOG.info(f"Sentiment from FANG companies: {df.to_dict()}")

# Запись результата в S3
write_s3(df=df, bucket="fangsentiment")

Один из простейших способов скачать эти файлы — воспользоваться CLI AWS:

noah:/tmp $ aws s3 cp --recursive s3://fangsentiment/ .
download: s3://fangsentiment/netflix_sentiment.csv to ./netflix_sentiment.csv
download: s3://fangsentiment/google_sentiment.csv to ./google_sentiment.csv
download: s3://fangsentiment/facebook_sentiment.csv to ./facebook_sentiment.csv

Итак, чего же мы достигли? На рис. 15.16 приведен наш бессерверный конвейер ИИ для работы с данными.

![Бессерверный конвейер ИИ для работы с данными](https://i.imgur.com/1234567.png)

Рис. 15.16. Бессерверный конвейер ИИ для работы с данными