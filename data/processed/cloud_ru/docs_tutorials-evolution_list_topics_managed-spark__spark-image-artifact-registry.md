---
source_image: docs_tutorials-evolution_list_topics_managed-spark__spark-image-artifact-registry.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 84.78
tokens: 10657
characters: 7540
timestamp: 2025-12-24T06:01:38.375362
finish_reason: stop
---

### Работа с пользовательским образом

Эта статья полезна?

С помощью этого руководства вы научитесь обрабатывать данные, применяя пользовательский образ Spark. Вы примените пользовательский образ, включающий библиотеки для работы с Object Storage и библиотеку NumPy. Для обработки данных вы используете скрипт, который объединит информацию о заказах из двух таблиц в единую витрину данных, найдет среднюю стоимость заказа и подсчитает разницу с ней для каждого заказа.

Вы будете использовать следующие сервисы:

• Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.

• Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

• Artifact Registry — сервис для хранения и распространения артефактов.

Шаги:

1. Подготовьте файлы с данными.
2. Подготовьте скрипт задачи.
3. Подготовьте образ в Artifact Registry.
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
8. Создайте реестр Artifact Registry, в котором будет храниться пользовательский образ Managed Spark.

1. Подготовьте файлы с данными

На этом шаге вы загрузите в хранилище Object Storage файлы с данными для обработки.

1. Скачайте CSV-таблицы client-spark-image.csv и sales-spark-image.csv: нажмите Скачать в правом верхнем углу.
2. В ранее созданном бакете Object Storage создайте папку input .
3. Загрузите CSV-таблицы в папку input .

2. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файл, содержащий скрипт для обработки данных из CSV-таблицы.

1. Скопируйте скрипт и назовите файл script-spark-image.py .

```python
import numpy as np
import time

from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType
from pyspark.sql.functions import lit, udf

bucket_name = 'your-bucket-name'

spark = (SparkSession.builder
    .appName("sales")
    .getOrCreate())

# Read the source data from csv
df_sales = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .load(f"s3a://{bucket_name}/input/sales-spark-image.csv")

df_client = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .load(f"s3a://{bucket_name}/input/client-spark-image.csv")

# get average cost for all sales
np_arr = np.array(df_sales.select('sales').collect())
avg = np.average(np_arr)
print(f"Average cost: {avg}")

@udf(returnType=FloatType())
def calc_diff_avg(avg, val):
    return val - avg

# Create result with sale price and diff between sale price and average price
df_result = df_sales \
    .join(df_client, df_sales.order_number == df_client.order_number,"inner") \
    .select(
        df_client.order_number,
        df_client.order_date,
        df_client.phone,
        df_client.address_line1,
        df_client.address_line2,
        df_client.city,
        df_client.state,
        df_client.postal_code,
        df_client.country,
        df_client.territory,
        df_client.contact_last_name,
        df_client.contact_first_name,
        df_client.deal_size,
        df_client.car,
        df_sales.sales,
        calc_diff_avg(lit(avg), df_sales.sales).alias("diff_with_avg")
    )

# Write the result to csv file
df_result.write.mode("overwrite").option("Header","true").csv(f"s3a://{bucket_name}/output/sales")
```

2. В строке bucket_name = 'your-bucket-name' замените your-bucket-name на название бакета Object Storage.
3. В ранее созданном бакете Object Storage создайте папку jobs .
4. Загрузите скрипт в папку jobs .

В результате получится следующая структура бакета с файлами:

• <bucket>
  o input
    ▪ sales-spark-image.csv
    ▪ client-spark-image.csv
  o jobs
    ▪ script-spark-image.py

3. Подготовьте образ в Artifact Registry

На этом шаге вы подготовите пользовательский образ Managed Spark и загрузите его в сервис Artifact Registry.

1. Создайте Dockerfile для сборки образа.

```Dockerfile
FROM apache/spark:3.5.0-scala2.12-java11-python3-ubuntu

# add s3 libs
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle:1.12.262.tar.gz -o /opt/aws-java-sdk-bundle.tar.gz
RUN curl https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar -o /opt/hadoop-aws-3.3.4.jar
ARG SPARK_USER=root
USER $SPARK_USER

# install compatible numpy version
RUN pip install numpy==1.21.6
```

2. Чтобы собрать образ, выполните команду:

```bash
docker build . --tag <IMAGE-NAME>:<TAG> --platform linux/amd64
```

Где:
• <IMAGE-NAME> — имя образа.
• <TAG> — тег образа.

3. Откройте сервис Artifact Registry.
4. Создайте репозиторий.
5. Загрузите образ.

4. Создайте задачу Managed Spark

На этом шаге вы запустите задачу Managed Spark с использованием подготовленного скрипта.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например spark-image-sales .
6. В блоке Образ:
   a. Выберите Пользовательский.
   b. Под полем URI образа нажмите Выбрать из реестра и выберите добавленный ранее образ.
7. В блоке Скрипт приложения:
   • В поле Тип запускаемой задачи выберите Python .
   • В поле Путь к запускаемому файлу укажите путь к файлу script-spark-image.py . В данном случае путь s3a://{bucket_name}/jobs/script-spark-image.py , где {bucket_name} — название созданного бакета Object Storage.
8. Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи.

5. Наблюдайте за ходом выполнения задачи

На этом шаге вы будете наблюдать за ходом выполнения задачи, просматривая информацию, поступающую в логи.

Вы можете посмотреть логи задачи, когда задача находится в статусах «Выполняется» и «Готово», то есть как в процессе выполнения, так и по завершению задачи.

Перейдите к логам.

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

Результат

Когда задача перейдет в статус «Выполнено», откройте файловый менеджер Object Storage. В бакете появится новая папка output , в которой будет храниться сводная таблица данных.

Вы применили пользовательский образ Managed Spark и скрипт для обработки данных и получили объединенную таблицу со всеми данными.