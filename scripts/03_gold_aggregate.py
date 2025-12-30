from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, countDistinct
from config.paths import SILVER_PATH, GOLD_PATH

spark = SparkSession.builder.appName("gold-aggregate").getOrCreate()

silver_df = spark.read.parquet(SILVER_PATH)

gold_df = silver_df.groupBy("order_status").agg(
    countDistinct("order_id").alias("total_orders"),
    sum("payment_value").alias("total_revenue")
)

gold_df.write.mode("overwrite").parquet(GOLD_PATH)

spark.stop()

