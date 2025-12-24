---
source_image: docs_tutorials-evolution_list_topics_managed-spark__spark-s3.jpg
page_number: 3
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 86.15
tokens: 10641
characters: 7113
timestamp: 2025-12-24T06:02:19.878506
finish_reason: stop
---

Обработка данных из Object Storage

С помощью этого руководства вы научитесь использовать сервис Managed Spark для обработки данных, хранящихся в Evolution Object Storage.

В качестве примера вы построите витрину данных, отражающую полную информацию о клиентах и продажах.

Будут использоваться данные из двух таблиц:

• Таблица client.csv содержит информацию о клиентах: номер заказа, дату, город, имя и фамилию клиента, модель автомобиля и др.
• Таблица sales.csv содержит информацию о продажах: номер заказа и его сумму.

В результате получится таблица, в которой данные объединены по номеру заказа.

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

1. Подготовьте файл CSV
На этом шаге вы загрузите в хранилище Object Storage файлы с данными для обработки.

1. Скачайте sales.csv и client.csv: нажмите Скачать в правом верхнем углу.
2. В ранее созданном бакете Object Storage создайте папку input .
3. В папке создайте папку car-sales .
4. Загрузите CSV-таблицы в папку car-sales .

2. Подготовьте скрипт задачи
На этом шаге вы загрузите в хранилище Object Storage файл, содержащий скрипт для обработки данных из CSV-таблицы.

1. Скопируйте скрипт и назовите файл spark-sales-etl.py .

import time
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import count
from pyspark.sql.types import IntegerType, BooleanType, DateType
from pyspark.sql.functions import col
from pyspark.sql.functions import sum, avg, max
bucket_name = 'your-bucket-name'

spark = (SparkSession.builder \
    .appName("sales") \
    .getOrCreate())

df_sales = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .load(f"s3a://{bucket_name}/input/car-sales/sales.csv")

df_client = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .load(f"s3a://{bucket_name}/input/car-sales/client.csv")

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
        df_client.zipcode,
        df_client.contact_last_name,
        df_client.contact_first_name,
        df_client.deal_size,
        df_client.car,
        df_sales.sales
    )

df_result.write.mode('overwrite').csv(f"s3a://{bucket_name}/output/sales")

2. В строке bucket_name = 'your-bucket-name' замените your-bucket-name на название бакета Object Storage.
3. В ранее созданном бакете Object Storage создайте папку jobs .
4. Загрузите скрипт в папку jobs .

В результате получится следующая структура бакета с файлами:

• <bucket>
  • input
    • car-sales
      • client.csv
      • sales.csv
  • jobs
    • spark-sales-etl.py

3. Создайте задачу Managed Spark
На этом шаге вы запустите задачу Managed Spark с использованием подготовленного скрипта.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например spark-sales .
6. В блоке Скрипт приложения:
   • В поле Тип запускаемой задачи выберите Python .
   • В поле Путь к запускаемому файлу укажите путь к файлу spark-sales-etl.py . В данном случае путь s3a://{bucket_name}/jobs/spark-sales-etl.py , где {bucket_name} — название созданного бакета Object Storage.
7. Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи.

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

Spark Jobs (?)
User: root
Total Uptime: 18 min
Scheduling Mode: FIFO
Completed Jobs: 4

<table>
  <tr>
    <th>Job Id</th>
    <th>Description</th>
    <th>Submitted</th>
    <th>Duration</th>
    <th>Stages: Succeeded/Total</th>
    <th>Tasks (for all stages): Succeeded/Total</th>
  </tr>
  <tr>
    <td>3</td>
    <td>save at &lt;unknown&gt;:0<br>save at &lt;unknown&gt;:0</td>
    <td>2024/07/17 12:54:35</td>
    <td>2.6 min</td>
    <td>1/1</td>
    <td>2/2</td>
  </tr>
  <tr>
    <td>2</td>
    <td>SanonRunWithThreadLocalCaptured$1 at &lt;unknown&gt;:0<br>SanonRunWithThreadLocalCaptured$1 at &lt;unknown&gt;:0</td>
    <td>2024/07/17 12:54:34</td>
    <td>0.1 s</td>
    <td>1/1</td>
    <td>2/2</td>
  </tr>
  <tr>
    <td>1</td>
    <td>csv at &lt;unknown&gt;:0<br>csv at &lt;unknown&gt;:0</td>
    <td>2024/07/17 12:54:27</td>
    <td>6 s</td>
    <td>1/1</td>
    <td>2/2</td>
  </tr>
  <tr>
    <td>0</td>
    <td>csv at &lt;unknown&gt;:0<br>csv at &lt;unknown&gt;:0</td>
    <td>2024/07/17 12:54:24</td>
    <td>3 s</td>
    <td>1/1</td>
    <td>1/1</td>
  </tr>
</table>

Результат
Когда задача перейдет в статус «Выполнено», откройте бакет Object Storage. В бакете появятся:

• новая папка sales ;
• таблица с объединенными данными из sales.csv и client.csv .

Вы обработали данные из Object Storage с помощью сервиса Managed Spark и получили таблицу с объединенными данными.