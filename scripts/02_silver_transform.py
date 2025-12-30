from pyspark.sql import SparkSession
from config.paths import (
    BRONZE_ORDERS_PATH,
    BRONZE_ITEMS_PATH,
    BRONZE_PAYMENTS_PATH,
    SILVER_PATH
)

spark = SparkSession.builder.appName("silver-transform").getOrCreate()

orders = spark.read.option("header", True).csv(BRONZE_ORDERS_PATH)
items = spark.read.option("header", True).csv(BRONZE_ITEMS_PATH)
payments = spark.read.option("header", True).csv(BRONZE_PAYMENTS_PATH)

orders_s = orders.select("order_id", "customer_id", "order_status", "order_purchase_timestamp")
items_s = items.select("order_id", "product_id", "price", "freight_value")
payments_s = payments.select("order_id", "payment_type", "payment_value")

silver_df = orders_s.join(items_s, "order_id") \
                    .join(payments_s, "order_id", "left")

silver_df.write.mode("overwrite").parquet(SILVER_PATH)

spark.stop()
