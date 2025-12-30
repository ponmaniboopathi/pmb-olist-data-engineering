from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date, current_timestamp
from config.paths import (
    BRONZE_ORDERS_PATH,
    BRONZE_ITEMS_PATH,
    BRONZE_PAYMENTS_PATH
)

spark = SparkSession.builder.appName("bronze-read").getOrCreate()

orders = spark.read.option("header", True).csv(BRONZE_ORDERS_PATH)
items = spark.read.option("header", True).csv(BRONZE_ITEMS_PATH)
payments = spark.read.option("header", True).csv(BRONZE_PAYMENTS_PATH)

orders = orders.withColumn("ingest_date", current_date()) \
               .withColumn("ingest_timestamp", current_timestamp())

orders.show(5, False)

spark.stop()
