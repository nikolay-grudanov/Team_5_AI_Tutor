---
source_image: page_432.png
page_number: 432
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.59
tokens: 7650
characters: 2126
timestamp: 2025-12-24T03:12:23.869925
finish_reason: stop
---

Метрики DynamoDB демонстрируют, что мы выделили слишком мало единиц пропускной способности по чтению DynamoDB. В результате возникает задержка, особенно для функции List (отображена на графике длительности выполнения функции Lambda красной линией, доходящей до 14,7 секунды), извлекающей все элементы todo из таблицы DynamoDB, что требует большого количества операций чтения. При создании таблицы DynamoDB мы задали параметр выделения единиц пропускной способности по чтению равным 10, а график CloudWatch демонстрирует, что он доходит до 25.

Изменим тип таблицы DynamoDB с PROVISIONED на PAY_PER_REQUEST. Внесите соответствующее изменение в файл cdk_lambda_dynamodb_fargate/cdk_lambda_dynamodb_stack.py:

table = aws_dynamodb.Table(self, "Table",
    partition_key=aws_dynamodb.Attribute(
        name="id",
        type=aws_dynamodb.AttributeType.STRING),
    billing_mode = aws_dynamodb.BillingMode.PAY_PER_REQUEST)

Выполните команду cdk deploy, после чего запустите локальный контейнер Docker для нагрузочного тестирования.

На этот раз результаты намного лучше:

<table>
  <tr>
    <th>Percentile, %</th>
    <th>Resp. Time, s</th>
  </tr>
  <tr>
    <td>0.0</td>
    <td>0.136</td>
  </tr>
  <tr>
    <td>50.0</td>
    <td>0.505</td>
  </tr>
  <tr>
    <td>90.0</td>
    <td>1.296</td>
  </tr>
  <tr>
    <td>95.0</td>
    <td>1.444</td>
  </tr>
  <tr>
    <td>99.0</td>
    <td>1.806</td>
  </tr>
  <tr>
    <td>99.9</td>
    <td>2.226</td>
  </tr>
  <tr>
    <td>100.0</td>
    <td>2.86</td>
  </tr>
</table>

Лучше выглядят и графики длительности выполнения функции Lambda (рис. 13.3) и выделяемых и потребляемых единиц пропускной способности по чтению/записи DynamoDB (рис. 13.4).

Отметим, что потребляемые единицы пропускной способности по чтению автоматически выделяются DynamoDB по мере необходимости и выполняется вертикальное масштабирование, чтобы выдержать возросшее количество запросов на чтение от функций Lambda. Наибольший вклад в смысле запросов на чтение вносит функция List, вызываемая при выводе списка, обновлении и удалении в сценарии loadtest.py Molotov с помощью session.get(base_url + /todos).