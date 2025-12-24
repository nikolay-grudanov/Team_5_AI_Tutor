---
source_image: page_496.png
page_number: 496
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.90
tokens: 7398
characters: 1791
timestamp: 2025-12-24T03:13:51.894565
finish_reason: stop
---

```python
comprehend = boto3.client(service_name='comprehend')
payload = comprehend.detect_sentiment(Text=row, LanguageCode='en')
LOG.debug(f"Found Sentiment: {payload}")
sentiment = payload['Sentiment']
return sentiment

def apply_sentiment(df, column="wikipedia_snippit"):
    """Анализирует тональности с помощью функции apply библиотеки Pandas"""
    df['Sentiment'] = df[column].apply(create_sentiment)
    return df

### S3 ###

def write_s3(df, bucket):
    """Запись в корзину S3"""

    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    res = s3_resource.Object(bucket, 'fang_sentiment.csv').\
        put(Body=csv_buffer.getvalue())
    LOG.info(f"result of write to bucket: {bucket} with:\n {res}")

def lambda_handler(event, context):
    """Точка входа функции Lambda"""

    LOG.info(f"SURVEYJOB LAMBDA, event {event}, context {context}")
    receipt_handle = event['Records'][0]['receiptHandle'] #sqs message
    #'eventSourceARN': 'arn:aws:sqs:us-east-1:561744971673:producer'
    event_source_arn = event['Records'][0]['eventSourceARN']

    names = [] #Захвачено из очереди

    # Обработка очереди
    for record in event['Records']:
        body = json.loads(record['body'])
        company_name = body['name']

        # Захвачено для обработки
        names.append(company_name)

        extra_logging = {"body": body, "company_name":company_name}
        LOG.info(f"SQS CONSUMER LAMBDA, splitting arn: {event_source_arn}",
            extra=extra_logging)
        qname = event_source_arn.split(":")[-1]
        extra_logging["queue"] = qname
        LOG.info(f"Attempting Delete SQS {receipt_handle} {qname}",
            extra=extra_logging)
        res = delete_sqs_msg(queue_name=qname, receipt_handle=receipt_handle)
```