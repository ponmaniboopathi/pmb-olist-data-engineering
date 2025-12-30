# pmb-olist-data-engineering

# End-to-End Data Engineering Pipeline using Spark and Parquet on AWS S3

## Overview
This project demonstrates an end-to-end batch data engineering pipeline built using Apache Spark and AWS S3 following the Bronze–Silver–Gold architecture.

The pipeline ingests raw e-commerce data from Amazon S3, performs data cleaning and joins in the Silver layer, and produces analytics-ready aggregated datasets in the Gold layer using Parquet format.

## Architecture
S3 (Bronze - Raw CSV)
→ Spark on EC2
→ S3 (Silver - Cleaned & Joined Parquet)
→ S3 (Gold - Aggregated Parquet)

## Dataset
Brazilian e-commerce (Olist) dataset including:
- Orders
- Order Items
- Payments

## Technologies Used
- Apache Spark
- AWS S3
- Python (PySpark)
- Parquet
- EC2 (Spark standalone)

## Pipeline Layers

### Bronze Layer
- Reads raw CSV files from S3
- Adds ingestion metadata (ingest_date, ingest_timestamp)
- No transformations or joins

### Silver Layer
- Selects required business columns
- Joins orders, items, and payments using order_id
- Writes cleaned data as Parquet

### Gold Layer
- Aggregates business metrics
- Calculates total orders and total revenue by order status
- Writes analytics-ready Parquet datasets

## How to Run
1. Configure Spark with S3 access (IAM role recommended)
2. Run scripts in order:
   ```bash
   python scripts/01_bronze_read.py
   python scripts/02_silver_transform.py
   python scripts/03_gold_aggregate.py
