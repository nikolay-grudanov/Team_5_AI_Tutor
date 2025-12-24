---
source_image: docs_tutorials-evolution_list_topics_managed-spark__spark-delta-lake.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 95.63
tokens: 12258
characters: 7545
timestamp: 2025-12-24T06:00:53.710571
finish_reason: stop
---

### Работа с таблицами Delta Lake

С помощью этого руководства вы научитесь использовать сервис Managed Spark для обработки таблиц формата Delta Lake.

Вы построите витрину данных, отражающую полную информацию о клиентах и их пути, сохраните результат в формате Delta Lake и выгрузите историю изменений таблицы в логи.

Вы будете использовать следующие сервисы:

• Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.

• Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

Шаги:

1. Подготовьте файл CSV.
2. Подготовьте скрипт задачи.
3. Создайте задачу Managed Spark.
4. Наблюдайте за ходом выполнения задачи.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.
3. Настройте DNS-сервер и подсеть.
4. Создайте кластер Data Platform, в котором будет размещен инстанс.
5. Скачайте и установите root-сертификат на устройство.
6. Создайте пароль и добавьте его в Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.
7. Создайте инстанс Managed Spark.
8. Создайте публичный SNAT-шлюз для доступа инстанса к внешним источникам.
9. Сверьте совместимость версий Spark и Delta Lake.

1. Подготовьте файл CSV

На этом шаге вы загрузите в хранилище Object Storage файлы с данными для обработки.

1. Скачайте CSV-таблицу delta-table.csv: нажмите Скачать в правом верхнем углу.
2. В ранее созданном бакете Object Storage создайте папку input .
3. Загрузите CSV-таблицу в папку input .

2. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файл, содержащий скрипт для обработки данных из CSV-таблицы.

1. Скопируйте скрипт и назовите файл delta-script.py .

import time
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, FloatType, LongType, StructType, StructField, StringType
from delta import *

spark = (SparkSession.builder
    .appName("delta test")
    .enableHiveSupport()
    .getOrCreate())

SCHEMA = StructType([
    StructField("vendor_id", LongType(), True),
    StructField("trip_id", LongType(), True),
    StructField("trip_distance", FloatType(), True),
    StructField("fare_amount", DoubleType(), True),
    StructField("store_and_fwd_flag", StringType(), True)
])

TABLE_TIME = time.strftime('%Y_%m_%d_%H_%M_%S')
TABLE_NAME = f"warehouse_delta_{TABLE_TIME}"
ROOT_PATH = "s3a://your-bucket-name/"
CSV_PATH = ROOT_PATH + "input/delta-table.csv"
FULL_PATH_DELTA_TABLE = ROOT_PATH + "warehouse_delta/" + TABLE_NAME

def read_csv_to_table():
    csv_df = (
        spark
        .read
        .option("delimiter", ";")
        .option("header", "true")
        .csv(CSV_PATH, schema=SCHEMA)
    )
    csv_df.show()
    return csv_df

def insert_data_to_table(df):
    df.write.format("delta").save(FULL_PATH_DELTA_TABLE)

def read_data_from_table():
    df = spark.read.format("delta").load(FULL_PATH_DELTA_TABLE)
    df.show()

def update_delta_table():
    delta_table = DeltaTable.forPath(spark, FULL_PATH_DELTA_TABLE)
    delta_table.update(
        condition="vendor_id % 2 = 0",
        set={
            "trip_distance": "trip_distance + 2"
        }
    )

def show_history_delta():
    delta_table = DeltaTable.forPath(spark, FULL_PATH_DELTA_TABLE)
    history = delta_table.history()
    history.show()

def read_specific_version_delta(version: int):
    df = spark.read.format("delta").option("versionAsOf", version).load(FULL_PATH_DELTA_TABLE)
    df.show()

if __name__ == "__main__":
    csv_df = read_csv_to_table()
    insert_data_to_table(csv_df)
    read_data_from_table()
    update_delta_table()
    read_data_from_table()
    show_history_delta()
    read_specific_version_delta(version=1)
    spark.stop()

2. В строке ROOT_PATH = "s3a://your-bucket-name/" скрипта замените your-bucket-name на название бакета Object Storage.
3. В ранее созданном бакете Object Storage создайте папку jobs .
4. Загрузите скрипт в папку jobs .

В результате получится следующая структура бакета с файлами:

• <bucket>
  o input
    ▪ delta-table.csv
  o jobs
    ▪ delta-script.py

Описание работы Python-скрипта

3. Создайте задачу Managed Spark

На этом шаге вы создадите задачу Managed Spark с использованием подготовленного скрипта.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например delta .
6. В блоке Скрипт приложения:
   • В поле Тип запускаемой задачи выберите Python .
   • В поле Путь к запускаемому файлу укажите путь к файлу delta-script.py . В данном случае путь s3a://{bucket_name}/jobs/delta-script.py , где {bucket_name} — название созданного бакета Object Storage.
7. В блоке Настройки активируйте опцию Добавить Spark-конфигурацию (-conf) . Добавьте следующие параметры и их значения:

<table>
  <tr>
    <th>Параметр</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>spark.jars.packages</td>
    <td>io.delta:delta-spark_2.12:3.2.0</td>
  </tr>
  <tr>
    <td>spark.sql.extensions</td>
    <td>io.delta.sql.DeltaSparkSessionExtension</td>
  </tr>
  <tr>
    <td>spark.sql.catalog.spark_catalog</td>
    <td>org.apache.spark.sql.delta.catalog.DeltaCatalog</td>
  </tr>
  <tr>
    <td>spark.log.level</td>
    <td>ERROR</td>
  </tr>
</table>

8. Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи .

4. Наблюдайте за ходом выполнения задачи

На этом шаге вы будете наблюдать за ходом выполнения задачи, просматривая информацию, поступающую в логи.

Вы можете посмотреть логи задачи, когда задача находится в статусах «Выполняется» и «Готово», то есть как в процессе выполнения, так и по завершению задачи.

Перейдите к логам

1. В строке задачи нажмите *** и выберите Перейти к логам.
2. Используйте фильтр, чтобы найти логи, например, за определенное время.

Перейдите в Spark UI

1. Откройте инстанс Managed Spark.
2. Во вкладке Задачи нажмите Spark UI. В соседней вкладке откроется интерфейс Spark UI.
3. Вернитесь в инстанс и откройте вкладку Информация.
4. Скопируйте данные из блока Настройки доступа.
5. Введите данные инстанса:
   • Username — значение поля Пользователь.
   • Password — значение секрета в поле Пароль.

В интерфейсе Spark UI вы найдете информацию о ходе выполнения задачи.

![Spark UI](https://example.com/spark-ui.png)

Результат

Когда задача перейдет в статус «Выполнено», откройте бакет Object Storage. В бакете появится новая папка с названием формата delta-lab_<TIME_STAMP> . В этой папке хранятся:

• версии таблицы «delta-table.csv»;
• папка _delta_log с логами задачи.

Чтобы посмотреть историю изменений таблицы с помощью метода history() :

1. Откройте сервис Managed Spark.
2. Перейдите на вкладку Задачи.
3. Скопируйте ID задачи.
4. Нажмите *** и выберите Перейти к логам.
5. В поле Запрос введите labels.spark.job.id="ID" , где ID — идентификатор задачи, скопированный ранее.
6. Нажмите Скачать журнал логов.
7. Выберите формат файла.
8. Нажмите Скачать.
9. Откройте скачанный файл.

История изменений отображается в нескольких сообщениях.

Вы обработали таблицу формата Delta Lake с помощью сервиса Managed Spark и просмотрели информацию об изменениях в таблице.