---
source_image: page_422.png
page_number: 422
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.74
tokens: 7307
characters: 1606
timestamp: 2025-12-24T03:11:54.906679
finish_reason: stop
---

partition_key=aws_dynamodb.Attribute(
    name="id",
    type=aws_dynamodb.AttributeType.STRING),
read_capacity=10,
write_capacity=5)

# Описываем функции Lambda
list_handler = aws_lambda.Function(self, "TodoListFunction",
    code=aws_lambda.Code.asset("./lambda"),
    handler="list.list",
    timeout=Duration.minutes(5),
    runtime=aws_lambda.Runtime.PYTHON_3_7)

create_handler = aws_lambda.Function(self, "TodoCreateFunction",
    code=aws_lambda.Code.asset("./lambda"),
    handler="create.create",
    timeout=Duration.minutes(5),
    runtime=aws_lambda.Runtime.PYTHON_3_7)

get_handler = aws_lambda.Function(self, "TodoGetFunction",
    code=aws_lambda.Code.asset("./lambda"),
    handler="get.get",
    timeout=Duration.minutes(5),
    runtime=aws_lambda.Runtime.PYTHON_3_7)

update_handler = aws_lambda.Function(self, "TodoUpdateFunction",
    code=aws_lambda.Code.asset("./lambda"),
    handler="update.update",
    timeout=Duration.minutes(5),
    runtime=aws_lambda.Runtime.PYTHON_3_7)

delete_handler = aws_lambda.Function(self, "TodoDeleteFunction",
    code=aws_lambda.Code.asset("./lambda"),
    handler="delete.delete",
    timeout=Duration.minutes(5),
    runtime=aws_lambda.Runtime.PYTHON_3_7)

# Передаем имя таблицы во все обработчики через переменную среды
# и предоставляем обработчикам права доступа на чтение/запись
# этой таблицы.
handler_list = [
    list_handler,
    create_handler,
    get_handler,
    update_handler,
    delete_handler
]
for handler in handler_list:
    handler.add_environment('DYNAMODB_TABLE', table.table_name)
    table.grant_read_write_data(handler)