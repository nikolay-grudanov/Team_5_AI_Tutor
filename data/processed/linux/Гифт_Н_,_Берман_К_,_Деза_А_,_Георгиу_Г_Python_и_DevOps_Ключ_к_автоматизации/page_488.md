---
source_image: page_488.png
page_number: 488
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.47
tokens: 7386
characters: 1655
timestamp: 2025-12-24T03:13:44.210604
finish_reason: stop
---

def send_sqs_msg(msg, queue_name, delay=0):
    '''Отправляем сообщение SQS

Ожидает на входе SQS queue_name и msg в виде ассоциативного массива.
Возвращает ассоциативный массив response.
'''

    queue_url = SQS.get_queue_url(QueueName=queue_name)["QueueUrl"]
    queue_send_log_msg = "Send message to queue url: %s, with body: %s" %\
        (queue_url, msg)
    LOG.info(queue_send_log_msg)
    json_msg = json.dumps(msg)
    response = SQS.send_message(
        QueueUrl=queue_url,
        MessageBody=json_msg,
        DelaySeconds=delay)
    queue_send_log_msg_resp = "Message Response: %s for queue url: %s" %\
        (response, queue_url)
    LOG.info(queue_send_log_msg_resp)
    return response

def send_emissions(table, queue_name):
    '''Отправка'''
    items = scan_table(table=table)
    for item in items:
        LOG.info(f"Sending item {item} to queue: {queue_name}")
        response = send_sqs_msg(item, queue_name=queue_name)
        LOG.debug(response)

def lambda_handler(event, context):
    '''
    Точка входа функции Lambda
    '''
    extra_logging = {"table": TABLE, "queue": QUEUE}
    LOG.info(f"event {event}, context {context}", extra=extra_logging)
    send_emissions(table=TABLE, queue_name=QUEUE)


Приведенный код делает следующее.

1. Извлекает названия компаний из Amazon DynamoDB.
2. Помещает эти названия в Amazon SQS.

Для проверки работы можно выполнить локальный тест в Cloud9 (рис. 15.10).

Далее можно проверить сообщения в SQS, как показано на рис. 15.11.

Не забудьте задать правильную роль IAM! Необходимо присвоить функции Lambda роль IAM с правами на запись сообщений в SQS, как показано на рис. 15.12.