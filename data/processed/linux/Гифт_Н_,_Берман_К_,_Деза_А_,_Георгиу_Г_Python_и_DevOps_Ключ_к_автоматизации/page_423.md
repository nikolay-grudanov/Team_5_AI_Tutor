---
source_image: page_423.png
page_number: 423
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.27
tokens: 7416
characters: 1993
timestamp: 2025-12-24T03:11:58.722953
finish_reason: stop
---

# Описываем конечную точку API
api = aws_apigateway.LambdaRestApi(self, "TodoApi",
    handler=list_handler,
    proxy=False)

# Описываем LambdaIntegrations
list_lambda_integration = \
    aws_apigateway.LambdaIntegration(list_handler)
create_lambda_integration = \
    aws_apigateway.LambdaIntegration(create_handler)
get_lambda_integration = \
    aws_apigateway.LambdaIntegration(get_handler)
update_lambda_integration = \
    aws_apigateway.LambdaIntegration(update_handler)
delete_lambda_integration = \
    aws_apigateway.LambdaIntegration(delete_handler)

# Описываем модель API REST и связываем методы с LambdaIntegrations
api.root.add_method('ANY')
todos = api.root.add_resource('todos')
todos.add_method('GET', list_lambda_integration)
todos.add_method('POST', create_lambda_integration)
todo = todos.add_resource('{id}')
todo.add_method('GET', get_lambda_integration)
todo.add_method('PUT', update_lambda_integration)
todo.add_method('DELETE', delete_lambda_integration)

Стоит отметить несколько особенностей только что приведенного кода.

• Мы воспользовались методом add_environment объектов handler для передачи переменной среды DYNAMODB_TABLE, применяемой в Python-коде для функций Lambda, задав для нее значение table.table_name. Название таблицы DynamoDB на этапе формирования неизвестно, так что CDK меняет его на токен, заменяемый на правильное название при развертывании стека (см. подробности в документации по токенам (https://oreil.ly/XfdEU)).

• Мы использовали все возможности простой конструкции языка программирования, цикла for, когда проходили в цикле по всем обработчикам. И хотя это может показаться очевидным, но все равно заслуживает упоминания, поскольку циклы и передача переменных реализованы в утилитах типа «инфраструктура как код», таких как Terraform, очень неуклюже, если вообще реализованы.

• Мы описали HTTP-методы (GET, POST, PUT, DELETE), связанные с различными конечными точками API Gateway и соответствующей функцией Lambda для каждого из них.