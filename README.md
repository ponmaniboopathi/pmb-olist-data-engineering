# pmb-olist-data-engineering

## End-to-End Data Engineering Pipeline using Spark and Parquet on AWS S3

## Overview
This project demonstrates an end-to-end **batch data engineering pipeline** built using **Apache Spark** and **AWS S3**, following the **Bronze–Silver–Gold** architecture.

The pipeline ingests raw e-commerce data from Amazon S3, performs data cleaning and joins in the Silver layer, and produces analytics-ready aggregated datasets in the Gold layer using **Parquet** format. The Gold layer is queried using **Amazon Athena**.

---

## Architecture
S3 (Bronze - Raw CSV)  
→ Spark on EC2  
→ S3 (Silver - Cleaned & Joined Parquet)  
→ S3 (Gold - Aggregated Parquet)  
→ Athena (Query Layer)

---

## Dataset
Brazilian e-commerce (Olist) dataset containing:
- Orders
- Order Items
- Payments

---

## Technologies Used
- Apache Spark (PySpark)
- AWS S3
- Amazon Athena
- Parquet
- EC2 (Spark standalone)

---

## Pipeline Layers

### Bronze Layer
- Reads raw CSV files from Amazon S3
- Adds ingestion metadata (`ingest_date`, `ingest_timestamp`)
- No transformations or joins are applied

### Silver Layer
- Selects required business columns
- Joins orders, order items, and payments using `order_id`
- Writes cleaned and joined data as Parquet to Amazon S3

### Gold Layer
- Aggregates business metrics
- Calculates total orders and total revenue by order status
- Writes analytics-ready Parquet datasets to Amazon S3

---

## How to Run
1. Configure Spark with access to Amazon S3 (IAM role recommended)
2. Run the pipeline scripts in sequence:
   ```bash
   python scripts/01_bronze_read.py
   python scripts/02_silver_transform.py
   python scripts/03_gold_aggregate.py

