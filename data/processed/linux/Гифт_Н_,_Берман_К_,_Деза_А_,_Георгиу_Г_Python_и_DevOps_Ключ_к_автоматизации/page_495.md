---
source_image: page_495.png
page_number: 495
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.89
tokens: 7334
characters: 1792
timestamp: 2025-12-24T03:13:47.804484
finish_reason: stop
---

def sqs_approximate_count(queue_name):
    """Возвращает приблизительное количество оставшихся в очереди сообщений"""
    queue = sqs_queue_resource(queue_name)
    attr = queue.attributes
    num_message = int(attr['ApproximateNumberOfMessages'])
    num_message_not_visible = int(attr['ApproximateNumberOfMessagesNotVisible'])
    queue_value = sum([num_message, num_message_not_visible])
    sum_msg = """'ApproximateNumberOfMessages' and\
'ApproximateNumberOfMessagesNotVisible' =\
*** [%s] *** for QUEUE NAME: [%s]""" %\
    (queue_value, queue_name)
    LOG.info(sum_msg)
    return queue_value

def delete_sqs_msg(queue_name, receipt_handle):

    sqs_client = sqs_connection()
    try:
        queue_url = sqs_client.get_queue_url(QueueName=queue_name)["QueueUrl"]
        delete_log_msg = "Deleting msg with ReceiptHandle %s" % receipt_handle
        LOG.info(delete_log_msg)
        response = sqs_client.delete_message(QueueUrl=queue_url,
            ReceiptHandle=receipt_handle)
    except botocore.exceptions.ClientError as error:
        exception_msg =\
            "FAILURE TO DELETE SQS MSG: Queue Name [%s] with error: [%s]" %\
                (queue_name, error)
        LOG.exception(exception_msg)
        return None

    delete_log_msg_resp = "Response from delete from queue: %s" % response
    LOG.info(delete_log_msg_resp)
    return response

def names_to_wikipedia(names):

    wikipedia_snippit = []
    for name in names:
        wikipedia_snippit.append(wikipedia.summary(name, sentences=1))
    df = pd.DataFrame(
        {
            'names':names,
            'wikipedia_snippit': wikipedia_snippit
        }
    )
    return df

def create_sentiment(row):
    """С помощью AWS Comprehend выявляет тональности DataFrame"""
    LOG.info(f"Processing {row}")