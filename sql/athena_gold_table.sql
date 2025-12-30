-- Create external table on Gold layer Parquet data
CREATE EXTERNAL TABLE IF NOT EXISTS pmb_olist.gold_order_metrics (
    order_status STRING,
    total_orders BIGINT,
    total_revenue DOUBLE
)
STORED AS PARQUET
LOCATION 's3://pmb-olist-gold/order_metrics/';

-- Validate data
SELECT *
FROM pmb_olist.gold_order_metrics
LIMIT 10;
