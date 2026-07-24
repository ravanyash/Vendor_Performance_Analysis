# 📊 Vendor Performance Analysis

An end-to-end Data Analytics project that analyzes vendor performance using **Python, SQL, SQLite, MySQL, Power BI, and Jupyter Notebook**. The project transforms raw transactional data into meaningful business insights through data cleaning, SQL analysis, feature engineering, and an interactive Power BI dashboard.

---

## 📌 Project Overview

The objective of this project is to analyze vendor purchasing and sales performance, identify top and low-performing vendors, evaluate profitability, and provide actionable business insights through an interactive dashboard.

The project follows a complete analytics workflow:

**Raw CSV Files → SQLite Database → SQL Analysis → Exploratory Data Analysis → Feature Engineering → Vendor Summary Dataset → Business Analysis → Power BI Dashboard**

---

# 📂 Dataset

The raw datasets used in this project are available here:

🔗 **Google Drive Dataset**

https://drive.google.com/file/d/1P4pD6dBXr3I58BukHSX6IgwLLPE5uOUR/view?usp=sharing

The dataset contains the following CSV files:

| Dataset | Description |
|---------|-------------|
| begin_inventory.csv | Opening inventory records |
| end_inventory.csv | Closing inventory records |
| purchase_prices.csv | Vendor purchase pricing information |
| purchases.csv | Purchase transaction records |
| sales.csv | Sales transaction records |
| vendor_invoice.csv | Vendor invoice details |

These datasets are imported into a SQLite database before analysis.

---

# 🚀 Project Workflow

## Step 1 — Data Collection

Downloaded the raw datasets consisting of six CSV files containing inventory, purchase, sales, pricing, and vendor information.

---

## Step 2 — Database Creation (SQLite)

Python script:

```
scripts/ingestion_db.py
```

Responsibilities:

- Reads all raw CSV files
- Creates SQLite database
- Creates required database tables
- Loads all datasets into SQLite

This serves as the project's ETL pipeline.

---

## Step 3 — Exploratory Data Analysis (EDA)

Notebook:

```
notebooks/Exploratory Data Analysis.ipynb
```

Tasks performed:

- Data Cleaning
- Missing Value Analysis
- Outlier Detection
- Feature Engineering
- Correlation Analysis
- Distribution Analysis
- SQL Query Analysis
- Business Insight Generation

Numerous SQL queries were executed on the SQLite database to understand purchasing patterns, inventory movement, vendor performance, and sales trends.

---

## Step 4 — Vendor Summary Generation

Python Script:

```
scripts/get_vendor_summary.py
```

Responsibilities:

- Executes SQL joins across multiple tables
- Aggregates vendor-level metrics
- Creates the final analytical dataset

Generated file:

```
Data/vendor_sales_summary.csv
```

This dataset is used for all further analysis and dashboard creation.

---

## Step 5 — Final Business Analysis

Notebook:

```
notebooks/Vendor_Performance_Analysis.ipynb
```

This notebook performs the complete vendor performance analysis.

It includes:

- KPI Calculations
- Vendor Performance Analysis
- Profitability Analysis
- Statistical Analysis
- Business Insights
- Visualizations

---

## Step 6 — Interactive Dashboard

Power BI Dashboard:

```
Dashboard/Vendor_Performance_Analysis.pbix
```

Dashboard Preview:

```
Dashboard/dashboard.png
```

Dashboard KPIs:

- Total Sales
- Total Purchase
- Gross Profit
- Profit Margin
- Unsold Capital

Dashboard Visualizations:

- Purchase Contribution %
- Top Vendors by Sales
- Top Brands by Sales
- Low Performing Vendors
- Low Performing Brands

---

# ❓ Business Questions Answered

This project answers the following business questions:

- Which vendors generate the highest sales?
- Which vendors generate the highest profit?
- Which vendors contribute most to purchases?
- Which brands generate maximum revenue?
- Which vendors perform poorly?
- Which brands perform poorly?
- What is the overall profit margin?
- How much capital is locked in unsold inventory?
- How efficiently are vendors contributing to business growth?

---

# 📁 Repository Structure

```
Vendor_Performance_Analysis
│
├── data
│   ├── Dashboard
│   │   ├── Vendor_Performance_Analysis.pbix
│   │   └── dashboard.png
│   │
│   ├── Data
│   │   └── vendor_sales_summary.csv
│   │
│   ├── notebooks
│   │   ├── Exploratory Data Analysis.ipynb
│   │   ├── Vendor_Performance_Analysis.ipynb
│   │   └── python2db.ipynb
│   │
│   ├── scripts
│   │   ├── ingestion_db.py
│   │   ├── get_vendor_summary.py
│   │   └── import_db_mysql.py
│   │
│   ├── report
│   │   └── Vendor-Performance-Analysis.pdf
│   │
│   └── logs
│
└── README.md
```

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- SQLite3
- MySQL
- SQL
- Matplotlib
- Seaborn
- Jupyter Notebook
- Power BI

---

# 📈 Key Insights

- Identified the highest revenue-generating vendors.
- Determined vendors contributing the highest gross profit.
- Measured overall business profit margin.
- Evaluated purchase contribution by vendor.
- Analyzed low-performing vendors and brands.
- Estimated unsold inventory capital.
- Built an executive dashboard for business decision-making.

---

# 📄 Project Report

The complete project report is available in:

```
data/report/Vendor-Performance-Analysis.pdf
```

---

# 📷 Dashboard Preview

Dashboard Image:

```
data/Dashboard/dashboard.png
```

---

# 👨‍💻 Author

**Yash Ravangave**

📧 Email

yashravangave13@gmail.com

💼 LinkedIn

https://www.linkedin.com/in/yash-ravangave/

🌐 Portfolio

https://ravanyash.github.io/yashravangave.github.io/

🐙 GitHub

https://github.com/RavanYash

---

## ⭐ If you found this project helpful, consider giving it a star on GitHub!
