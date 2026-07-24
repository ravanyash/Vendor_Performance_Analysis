# 📊 Vendor Performance Analysis

> **End-to-End Data Analytics Project using Python, SQL, SQLite & Power BI**

This project analyzes vendor performance by building a complete data analytics pipeline—from raw transactional data to an interactive Power BI dashboard. The project includes data ingestion, SQL analysis, exploratory data analysis (EDA), KPI generation, automated logging, and dashboard visualization to provide actionable business insights.

---

## 🌐 Connect With Me

**👨‍💻 Author:** Yash Ravangave

📧 Email: yashravangave13@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/yash-ravangave/

🌐 Portfolio: https://ravanyash.github.io/yashravangave.github.io/

🐙 GitHub: https://github.com/ravanyash

---

# 📸 Dashboard Preview

> Dashboard Screenshot

```
data/Dashboard/dashboard.png
```

---

# 📖 Project Overview

The objective of this project is to evaluate vendor performance using sales, purchases, inventory, and pricing data.

The analysis answers important business questions such as:

- Which vendors generate the highest sales?
- Which vendors contribute the most profit?
- Which brands perform best?
- Which vendors are underperforming?
- How much capital is blocked in unsold inventory?
- What is the company's overall profit margin?

The complete workflow demonstrates an end-to-end analytics pipeline using Python, SQL, SQLite, and Power BI.

---

# 🌟 Project Highlights

✔ End-to-End Data Analytics Project

✔ Automated ETL Pipeline

✔ SQLite Database Integration

✔ SQL-Based Business Analysis

✔ Exploratory Data Analysis (EDA)

✔ Feature Engineering

✔ Automated Logging System

✔ KPI Calculation

✔ Interactive Power BI Dashboard

✔ Business Insights & Recommendations

---

# 🛠 Tech Stack

| Category | Technologies |
|------------|-----------------------------|
| Programming | Python |
| Database | SQLite, SQL |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Power BI |
| Development | Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 📂 Dataset

### Dataset Source

Google Drive

https://drive.google.com/file/d/1P4pD6dBXr3I58BukHSX6IgwLLPE5uOUR/view?usp=sharing

### Raw Dataset Files

- begin_inventory.csv
- end_inventory.csv
- purchase_prices.csv
- purchases.csv
- sales.csv
- vendor_invoice.csv

These six datasets contain inventory, purchasing, pricing, sales, and vendor transaction information.

---

# 🔄 Project Workflow

## Step 1 — Data Collection

Downloaded six CSV datasets containing inventory, purchases, pricing, sales, and vendor invoice information.

↓

## Step 2 — Database Creation (ETL)

**Script**

```
scripts/ingestion_db.py
```

Responsibilities

- Reads all raw CSV files
- Creates SQLite database
- Creates database tables
- Imports every dataset into SQLite
- Handles data ingestion automatically
- Generates execution logs

### Output

SQLite Database

### Log Generated

```
logs/ingestion_db.log
```

The log file records:

- Database creation
- Table creation
- CSV import status
- Number of records imported
- Success messages
- Error messages (if any)

↓

## Step 3 — Exploratory Data Analysis (EDA)

**Notebook**

```
notebooks/Exploratory Data Analysis.ipynb
```

Performed

- Data Cleaning
- Missing Value Analysis
- Duplicate Removal
- Outlier Detection
- SQL Queries
- Correlation Analysis
- Feature Engineering
- Business Insights

The notebook also contains multiple SQL queries executed to understand the business data before building the final dataset.

↓

## Step 4 — Vendor Summary Generation

**Script**

```
scripts/get_vendor_summary.py
```

Responsibilities

- Executes SQL joins
- Aggregates vendor data
- Calculates KPIs
- Generates Vendor Sales Summary
- Exports processed CSV

### Output

```
Data/vendor_sales_summary.csv
```

### Log Generated

```
logs/vendor_summary.log
```

The log records:

- SQL query execution
- Vendor summary generation
- CSV export status
- Processing messages
- Error tracking

↓

## Step 5 — Final Business Analysis

**Notebook**

```
notebooks/Vendor_Performance_Analysis.ipynb
```

Performed

- KPI Analysis
- Vendor Performance Analysis
- Brand Performance Analysis
- Profitability Analysis
- Purchase Contribution Analysis
- Statistical Analysis
- Data Visualization
- Business Recommendations

This notebook uses the generated Vendor Sales Summary dataset to perform complete business analysis.

↓

## Step 6 — Dashboard Development

**Power BI Dashboard**

```
Dashboard/Vendor_Performance_Analysis.pbix
```

The final dashboard visualizes all KPIs and business insights interactively.

---

# 📁 Repository Structure

```
Vendor_Performance_Analysis
│
├── data
│
├── Dashboard
│   ├── Vendor_Performance_Analysis.pbix
│   └── dashboard.png
│
├── Data
│   └── vendor_sales_summary.csv
│
├── logs
│   ├── ingestion_db.log
│   └── vendor_summary.log
│
├── notebooks
│   ├── Exploratory Data Analysis.ipynb
│   ├── Vendor_Performance_Analysis.ipynb
│   └── python2db.ipynb
│
├── scripts
│   ├── ingestion_db.py
│   ├── get_vendor_summary.py
│   └── import_db_mysql.py
│
├── report
│   └── Vendor-Performance-Analysis.pdf
│
└── README.md
```

---

# 📄 Project Files

### scripts/

**ingestion_db.py**

- Creates SQLite database
- Imports all CSV files
- Automates ETL process
- Generates ingestion logs

---

**get_vendor_summary.py**

- Executes SQL queries
- Creates vendor summary dataset
- Exports processed CSV
- Generates execution logs

---

**import_db_mysql.py**

- Database connectivity utility used during project development.

---

### notebooks/

**Exploratory Data Analysis.ipynb**

Contains

- Data Cleaning
- SQL Analysis
- Missing Value Analysis
- Outlier Detection
- Feature Engineering
- Correlation Analysis
- Business Insights

---

**Vendor_Performance_Analysis.ipynb**

Contains

- Final KPI calculations
- Vendor Analysis
- Brand Analysis
- Profitability Analysis
- Business Visualizations

---

### Dashboard/

Contains

- Power BI Dashboard (.pbix)
- Dashboard Screenshot

---

### Data/

Contains the processed dataset used for dashboard creation.

```
vendor_sales_summary.csv
```

---

### report/

Contains the final business report.

```
Vendor-Performance-Analysis.pdf
```

---

### logs/

Contains execution logs generated automatically by Python scripts.

#### ingestion_db.log

Stores

- Database creation status
- Table creation status
- CSV import details
- Success messages
- Error messages

#### vendor_summary.log

Stores

- SQL query execution
- Vendor summary generation
- CSV export status
- Processing information
- Error tracking

Logging was implemented using Python's built-in **logging** module to improve debugging, monitoring, and maintainability.

---

# 📈 Dashboard KPIs

- Total Sales
- Total Purchase
- Gross Profit
- Profit Margin
- Unsold Capital

---

# 📊 Dashboard Visualizations

- Purchase Contribution %
- Top Vendors by Sales
- Top Brands by Sales
- Low Performing Vendors
- Low Performing Brands

---

# 💡 Key Business Insights

- Identified top-performing vendors based on sales.
- Measured vendor profitability using Gross Profit and Profit Margin.
- Evaluated purchase contribution by vendor.
- Identified low-performing vendors and brands.
- Estimated unsold inventory capital.
- Built an executive Power BI dashboard to support business decision-making.

---

# 📑 Project Report

The complete project report is available in

```
report/Vendor-Performance-Analysis.pdf
```

---

# ⭐ Support

If you found this project helpful or interesting, please consider giving this repository a ⭐ on GitHub.

Thank you for visiting this project!
