---
source_image: docs_tutorials-evolution_list_topics_managed-spark__spark-iceberg.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 85.34
tokens: 11804
characters: 7273
timestamp: 2025-12-24T06:01:31.424053
finish_reason: stop
---

### Работа с таблицами Iceberg

С помощью этого руководства вы научитесь использовать сервис Managed Spark для обработки таблиц формата Iceberg и преобразования их в таблицы Parquet.

В качестве примера вы построите витрину данных, отражающую информацию о продажах, и сохраните результат в формате Iceberg. Вы используете CSV-таблицу с данными о поездке, JAR-файл Iceberg и Python-скрипт, который прочитает CSV-таблицу, создаст схему Data Frame и выгрузит данные в таблицу Parquet.

Вы будете использовать следующие сервисы:

• Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.

• Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

Шаги:

1. Подготовьте файл CSV.
2. Подготовьте скрипт задачи.
3. Подготовьте файл Iceberg JAR.
4. Создайте задачу Managed Spark.
5. Наблюдайте за ходом выполнения задачи.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.
3. Настройте DNS-сервер и подсеть.
4. Создайте кластер Data Platform, в котором будет размещен инстанс.
5. Скачайте и установите root-сертификат на устройство.
6. Создайте пароль и добавьте его в Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.
7. Создайте инстанс Managed Spark.
8. Сверьте совместимость версий Spark и Iceberg.

1. Подготовьте файл CSV

На этом шаге вы загрузите в хранилище Object Storage файлы с данными для обработки.

1. Скачайте CSV-таблицу iceberg-table.csv: нажмите Скачать в правом верхнем углу.
2. В ранее созданном бакете Object Storage создайте папку input .
3. Загрузите CSV-таблицу в папку input .

2. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файл, содержащий скрипт для обработки данных из CSV-таблицы.

1. Скопируйте скрипт и назовите файл iceberg-script.py .

import time
from pyspark.sql.types import DoubleType, FloatType, LongType, StructType,StructField, StringType
from pyspark.sql import SparkSession
spark = (SparkSession.builder
    .appName('iceberg test')
    .enableHiveSupport()
    .getOrCreate())
DB_NAME = f"db_{time.strftime('%Y_%m_%d_%H_%M_%S')}"
CATALOG_NAME = "local"
TABLE_NAME = "my_table"
TABLE_PATH = f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}"

ROOT_PATH = "s3a://<your-bucket-name>/input/"
CSV_PATH = ROOT_PATH + "iceberg-table.csv"

SCHEMA = StructType([
    StructField("vendor_id", LongType(), True),
    StructField("trip_id", LongType(), True),
    StructField("trip_distance", FloatType(), True),
    StructField("fare_amount", DoubleType(), True),
    StructField("store_and_fwd_flag", StringType(), True)
])

def create_table():
    df = spark.createDataFrame([], SCHEMA)
    df.writeTo(TABLE_PATH).create()

def read_csv_to_table():
    csv_df = (
        spark
        .read
        .option("delimiter", ",")
        .option("header", True)
        .csv(CSV_PATH, schema=SCHEMA)
    )
    csv_df.show()
    return csv_df

def insert_data_to_table(df):
    df.writeTo(TABLE_PATH).append()

def read_data_from_table():
    spark.table(TABLE_PATH).show()

if __name__ == "__main__":
    create_table()
    csv_df = read_csv_to_table()
    insert_data_to_table(csv_df)
    read_data_from_table()
    spark.stop()

2. В строке ROOT_PATH = "s3a://<your-bucket-name>/input/" замените your-bucket-name на название бакета Object Storage.
3. В ранее созданном бакете Object Storage создайте папку jobs .
4. Загрузите скрипт в папку jobs .

3. Подготовьте файл Iceberg JAR

На этом шаге вы загрузите файл Iceberg JAR.

1. Скачайте JAR-файл Iceberg для соответствующей версии Spark. Например, если версия Spark 3.5, скачайте 1.9.2 Spark 3.5,with Scala 2.12 runtime Jar .
   В этом руководстве используется файл iceberg-spark-runtime-3.5.2.12-1.9.2.jar .
2. В ранее созданном бакете Object Storage создайте папку iceberg .
3. Загрузите файл Iceberg JAR в папку iceberg .

В результате получится следующая структура бакета с файлами:

• <bucket>
  o input
    ▪ iceberg-table.csv
  o jobs
    ▪ iceberg-script.py
  o iceberg
    ▪ iceberg-spark-runtime-3.5.2.12-1.6.1.jar

4. Создайте задачу Managed Spark

На этом шаге вы создадите задачу Managed Spark с использованием подготовленного скрипта.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например iceberg .
6. В блоке Скрипт приложения:
   • В поле Тип запускаемой задачи выберите Python .
   • В поле Путь к запускаемому файлу укажите путь к файлу iceberg-script.py . В данном случае путь s3a://{bucket_name}/jobs/iceberg-script.py , где {bucket_name} — название созданного бакета Object Storage.
7. В блоке Настройки:
   • активируйте опцию Добавить Spark конфигурацию (-conf). Добавьте следующие параметры и их значения:

<table>
  <tr>
    <th>Параметр</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>spark.sql.catalog.local</td>
    <td>org.apache.iceberg.spark.SparkCatalog</td>
  </tr>
  <tr>
    <td>spark.sql.catalog.local.type</td>
    <td>hadoop</td>
  </tr>
  <tr>
    <td>spark.sql.catalog.local.warehouse</td>
    <td>s3a://{bucket_name}/</td>
  </tr>
  <tr>
    <td></td>
    <td>{bucket_name} — название созданного бакета Object Storage</td>
  </tr>
</table>

• В поле Добавить зависимости укажите путь к JAR-файлу. В данном случае путь s3a://{bucket_name}/iceberg/iceberg-spark-runtime-3.5.2.12-1.9.2.jar , где {bucket_name} — название созданного бакета Object Storage.
8. Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи.

5. Наблюдайте за ходом выполнения задачи

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

Когда задача перейдет в статус «Выполнено», откройте бакет Object Storage. В бакете появится новая папка с названием формата db_<YYYY_MM_DD_hrs_min_sec> .

Внутри этой папки находятся две папки:

• metadata с описательной частью данных;
• data с таблицей Parquet с результатом работы скрипта.

Вы обработали данные и преобразовали таблицу формата Iceberg в таблицу Parquet с помощью сервиса Managed Spark.