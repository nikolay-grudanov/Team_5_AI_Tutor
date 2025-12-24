---
source_image: page_494.png
page_number: 494
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.13
tokens: 7383
characters: 1594
timestamp: 2025-12-24T03:13:50.615598
finish_reason: stop
---

# Настраиваем журналирование
import logging
from pythonjsonlogger import jsonlogger
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
LOG.addHandler(logHandler)

# Корзина S3
REGION = "us-east-1"

### Утилиты для работы с SQS ###
def sqs_queue_resource(queue_name):
    """Возвращает ресурс соединения для очереди SQS

Пример использования:
In [2]: queue = sqs_queue_resource("dev-job-24910")
In [4]: queue.attributes
Out[4]:
{'ApproximateNumberOfMessages': '0',
 'ApproximateNumberOfMessagesDelayed': '0',
 'ApproximateNumberOfMessagesNotVisible': '0',
 'CreatedTimestamp': '1476240132',
 'DelaySeconds': '0',
 'LastModifiedTimestamp': '1476240132',
 'MaximumMessageSize': '262144',
 'MessageRetentionPeriod': '345600',
 'QueueArn': 'arn:aws:sqs:us-west-2:414930948375:dev-job-24910',
 'ReceiveMessageWaitTimeSeconds': '0',
 'VisibilityTimeout': '120'}

"""
    sqs_resource = boto3.resource('sqs', region_name=REGION)
    log_sqs_resource_msg =\
        "Creating SQS resource conn with qname: [%s] in region: [%s]" %\
        (queue_name, REGION)
    LOG.info(log_sqs_resource_msg)
    queue = sqs_resource.get_queue_by_name(QueueName=queue_name)
    return queue

def sqs_connection():
    """Создает SQS-соединение по умолчанию в регионе,
соответствующем глобальной переменной REGION"""
    sqs_client = boto3.client("sqs", region_name=REGION)
    log_sqs_client_msg = "Creating SQS connection in Region: [%s]" % REGION
    LOG.info(log_sqs_client_msg)
    return sqs_client