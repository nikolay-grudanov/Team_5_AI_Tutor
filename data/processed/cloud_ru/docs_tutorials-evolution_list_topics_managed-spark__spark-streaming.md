---
source_image: docs_tutorials-evolution_list_topics_managed-spark__spark-streaming.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 84.22
tokens: 11147
characters: 8743
timestamp: 2025-12-24T06:02:55.667975
finish_reason: stop
---

### Чтение сообщений из топиков Managed Kafka®

С помощью этого руководства вы настроите чтение сообщений из топика Managed Kafka® и отображение полученных данных в логах задачи Managed Spark. Вы создадите две задачи Managed Spark с использованием скриптов для разового и для непрерывного чтения данных.

В результате вы получите возможность просматривать сообщения из топиков Managed Kafka® в логах задачи Managed Spark.

Вы будете использовать следующие сервисы:

- Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.
- Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.
- Managed Kafka® — сервис для развертывания и управления кластерами Kafka® в инфраструктуре платформы Evolution.

Шаги:

1. Подготовьте скрипты, которые будут обращаться к топику Managed Kafka®.
2. Создайте задачу Managed Spark.
3. Проверьте информацию в логах.
4. Запустите непрерывное чтение топика Managed Kafka®.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.
3. Настройте DNS-сервер и подсеть.
4. Создайте кластер Data Platform, в котором будет размещен инстанс.
5. Скачайте и установите root-сертификат на устройство.
6. Создайте пароль и добавьте его в Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.
7. Создайте инстанс Managed Spark.
8. Убедитесь, что в проекте, где будет запускаться задача Managed Spark, доступен сервис Managed Kafka®.
9. Создайте кластер Managed Kafka®. На шаге Сетевые настройки в списке Подсеть выберите подсеть, указанную при создании инстанса Managed Spark.
10. Подключитесь к кластеру Managed Kafka® и отправьте несколько сообщений в топик.

1. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файлы, содержащие скрипты для чтения топика Managed Kafka®. Скрипт из файла kafka_spark.py выполняет однократное чтение сообщений из топика, а скрипт из файла kafka_spark_streaming.py — непрерывное.

1. Скопируйте скрипт и назовите файл kafka_spark.py.

```python
from pyspark.sql import SparkSession
import os

kafka_user = os.environ["KAFKA_USER"]
kafka_pass = os.environ["KAFKA_PASS"]
kafka_topic = os.environ["KAFKA_TOPIC"]
kafka_server = os.environ["KAFKA_SERVER"]

spark = SparkSession.builder.appName("kafka").getOrCreate()

df = (
    spark.read.format("kafka")
    .option("kafka.bootstrap.servers", kafka_server)
    .option("kafka.security.protocol", "SASL_PLAINTEXT")
    .option("kafka.sasl.mechanism", "SCRAM-SHA-512")
    .option(
        "kafka.sasl.jaas.config",
        "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"{kafka_user}\" password=\"{kafka_pass}\""
    )
    .option("subscribe", kafka_topic)
    .option("startingOffsets", "earliest")
    .option("endingOffsets", "latest")
    .load()
)

df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
df.show(truncate=False)
spark.stop()
```

2. Скопируйте скрипт и назовите файл kafka_spark_streaming.py.

```python
from pyspark.sql import SparkSession
import os

kafka_user = os.environ["KAFKA_USER"]
kafka_pass = os.environ["KAFKA_PASS"]
kafka_topic = os.environ["KAFKA_TOPIC"]
kafka_server = os.environ["KAFKA_SERVER"]

spark = (
    SparkSession.builder.appName("kafka")
    .getOrCreate()
)

df = (
    spark
    .readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_server)
    .option("kafka.security.protocol", "SASL_PLAINTEXT")
    .option("kafka.sasl.mechanism", "SCRAM-SHA-512")
    .option(
        "kafka.sasl.jaas.config",
        "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"{kafka_user}\" password=\"{kafka_pass}\""
    )
    .option("subscribe", kafka_topic)
    .option("startingOffsets", "earliest")
    .load()
)

df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
console = (df
    .writeStream
    .outputMode('append')
    .format('console')
    .start()
)
console.awaitTermination()
spark.stop()
```

3. Откройте ранее созданный бакет Object Storage.
4. Загрузите файлы со скриптами.

2. Создайте задачу Managed Spark

На этом шаге вы создадите задачу Managed Spark с использованием подготовленного скрипта. Скрипт выполнит чтение сообщений, отправленных в топик Managed Kafka®, и выведет данные из них в логи задачи Managed Spark.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например kafka-spark-streaming.
6. В блоке Образ выберите базовый образ Spark-3.5.0.
7. В блоке Скрипт приложения:
   - В поле Тип запускаемой задачи выберите Python.
   - В поле Путь к запускаемому файлу укажите путь к файлу kafka_spark.py.
8. В блоке Настройки активируйте опцию Добавить параметры окружения. Добавьте следующие параметры и их значения:

<table>
  <tr>
    <th>Параметр</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>KAFKA_USER</td>
    <td>Логин для подключения к кластеру Managed Kafka®, например, cloud-admin.</td>
  </tr>
  <tr>
    <td>KAFKA_PASS</td>
    <td>Пароль для подключения к кластеру Managed Kafka® с указанным логином.</td>
  </tr>
  <tr>
    <td>KAFKA_TOPIC</td>
    <td>Имя топика Managed Kafka®.</td>
  </tr>
  <tr>
    <td>KAFKA_SERVER</td>
    <td>Внутренний IP-адрес кластера Managed Kafka®.</td>
  </tr>
</table>

Чтобы узнать внутренний IP-адрес, логин и пароль, откройте сервис Managed Kafka® в отдельной вкладке, в списке кластеров нажмите на название созданного ранее кластера и перейдите в блок Данные для подключения.

9. В блоке Настройки активируйте опцию Добавить Spark конфигурацию (- conf).
   - В поле Аргумент укажите spark.jars.packages.
   - В поле Значение укажите org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0.
10. Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи.

Подробнее о развертывании на официальном сайте.

3. Проверьте логи

На этом шаге вы проверите логи задачи Managed Spark и отображение в них данных из топика Managed Kafka®.

Для продолжения работы убедитесь, что статус задачи Managed Spark изменился на «Завершена».

1. В строке задачи нажмите *** и выберите Перейти к логам.
2. Используйте фильтр, чтобы найти логи, содержащие сообщения из топика Managed Kafka®.

Пример данных, полученных из топика Managed Kafka®:

<table>
  <tr>
    <th>2025-09-24T18:29:25...</th>
    <th>UNDEF</th>
    <th>+------------------------+------------------------+</th>
  </tr>
  <tr>
    <td>2025-09-24T18:29:25...</td>
    <td>UNDEF</td>
    <td>[32][62 61 72] [k-forstream]0 |6 [2025-09...</td>
  </tr>
  <tr>
    <td>2025-09-24T18:29:25...</td>
    <td>UNDEF</td>
    <td>[31][66 6F 6F] [k-forstream]0 |5 [2025-09...</td>
  </tr>
  <tr>
    <td>2025-09-24T18:29:25...</td>
    <td>UNDEF</td>
    <td>+------------------------+------------------------+</td>
  </tr>
  <tr>
    <td>2025-09-24T18:29:25...</td>
    <td>UNDEF</td>
    <td>|key|value|topic|partition|offset|timestamp...</td>
  </tr>
  <tr>
    <td>2025-09-24T18:29:25...</td>
    <td>UNDEF</td>
    <td>+------------------------+------------------------+</td>
  </tr>
</table>

4. Запустите непрерывное чтение топика Managed Kafka®

На этом шаге вы создадите вторую задачу Managed Spark с использованием скрипта, который будет непрерывно поддерживать соединение с топиком Managed Kafka® и выполнять чтение поступающих в него сообщений.

1. В строке задачи Managed Spark, выполненной ранее, нажмите *** и выберите Скопировать задачу.
2. В блоке Скрипт приложения в поле Путь к запускаемому файлу укажите путь к файлу kafka_spark_streaming.py.
3. Нажмите Создать.
4. Дождитесь, пока статус задачи изменится на «Выполняется».
5. В строке задачи нажмите *** и выберите Перейти к логам.
6. Используйте фильтр, чтобы найти логи, содержащие сообщения из топика Managed Kafka®. Если в топик Managed Kafka® не поступают новые данные, в логах будут только отправленные ранее сообщения и информация об ожидании.
7. Отправьте новое сообщение в топик Managed Kafka®.
8. Посмотрите в логах задачи Managed Spark информацию о новом сообщении.
9. Задача Managed Spark с данными параметрами будет выполняться, пока вы ее не завершите. Чтобы завершить задачу, в строке задачи нажмите *** и выберите Остановить.

Результат

Вы настроили чтение сообщений из топика Managed Kafka® и вывод полученных данных в логи задачи Managed Spark с помощью скриптов.