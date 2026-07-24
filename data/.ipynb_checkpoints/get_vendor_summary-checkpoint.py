import sqlite3
import pandas as pd
import numpy as np
import logging
import time

# --------------------------------------------------
# Configure Logging
# --------------------------------------------------
logging.basicConfig(
    filename="logs/vendor_summary.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


def create_vendor_summary(conn):
    """
    Merge purchase_prices, purchases, sales and vendor_invoice
    tables to create a consolidated vendor summary.
    """

    query = """
    WITH sales_summary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    ),

    purchase_summary AS (
        SELECT
            VendorNumber,
            Brand,
            SUM(Quantity) AS TotalPurchaseQuantity,
            SUM(Dollars) AS TotalPurchaseDollars
        FROM purchases
        GROUP BY VendorNumber, Brand
    ),

    freight_summary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS TotalFreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    )

    SELECT

        pp.VendorNumber,
        TRIM(pp.VendorName) AS VendorName,
        pp.Brand,
        pp.Description,
        pp.Volume,
        pp.Price AS ActualPrice,
        pp.PurchasePrice,

        COALESCE(ss.TotalSalesQuantity,0) AS TotalSalesQuantity,
        COALESCE(ss.TotalSalesDollars,0) AS TotalSalesDollars,
        COALESCE(ss.TotalSalesPrice,0) AS TotalSalesPrice,
        COALESCE(ss.TotalExciseTax,0) AS TotalExciseTax,

        COALESCE(ps.TotalPurchaseQuantity,0) AS TotalPurchaseQuantity,
        COALESCE(ps.TotalPurchaseDollars,0) AS TotalPurchaseDollars,

        COALESCE(fs.TotalFreightCost,0) AS TotalFreightCost

    FROM purchase_prices pp

    LEFT JOIN sales_summary ss
        ON pp.VendorNumber = ss.VendorNo
       AND pp.Brand = ss.Brand

    LEFT JOIN purchase_summary ps
        ON pp.VendorNumber = ps.VendorNumber
       AND pp.Brand = ps.Brand

    LEFT JOIN freight_summary fs
        ON pp.VendorNumber = fs.VendorNumber

    ORDER BY pp.VendorNumber, pp.Brand;
    """

    logging.info("Vendor summary created successfully.")

    return pd.read_sql_query(query, conn)


def clean_data(df):
    """
    Clean the vendor summary and create business metrics.
    """

    logging.info("Cleaning vendor summary data...")

    # Remove leading/trailing spaces
    df["VendorName"] = df["VendorName"].str.strip()

    # Convert Volume to numeric
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

    # Remove missing values
    df.dropna(subset=["Description", "Volume"], inplace=True)

    # Create new business metrics

    df["GrossProfit"] = (
        df["TotalSalesDollars"] -
        df["TotalPurchaseDollars"]
    )

    df["ProfitMargin"] = np.where(
        df["TotalSalesDollars"] != 0,
        (df["GrossProfit"] / df["TotalSalesDollars"]) * 100,
        0
    )

    df["ROI"] = np.where(
        df["TotalPurchaseDollars"] != 0,
        (df["GrossProfit"] / df["TotalPurchaseDollars"]) * 100,
        0
    )

    df["StockTurnover"] = np.where(
        df["TotalPurchaseQuantity"] != 0,
        df["TotalSalesQuantity"] /
        df["TotalPurchaseQuantity"],
        0
    )

    df["SalesToPurchaseRatio"] = np.where(
        df["TotalPurchaseDollars"] != 0,
        df["TotalSalesDollars"] /
        df["TotalPurchaseDollars"],
        0
    )

    return df


def save_summary(df, conn):
    """
    Save the cleaned vendor summary into SQLite.
    """

    df.to_sql(
        "vendor_sales_summary",
        conn,
        if_exists="replace",
        index=False
    )

    logging.info("vendor_sales_summary table created successfully.")



if __name__ == "__main__":
    start_time = time.time()

    # Create database connection
    conn = sqlite3.connect("inventory.db")

    logging.info("------------ Vendor Summary Pipeline Started ------------")

    try:

        # Create summary table
        logging.info("Creating Vendor Summary Table...")
        summary_df = create_vendor_summary(conn)

        # Clean data
        logging.info("Cleaning Data...")
        clean_df = clean_data(summary_df)

        # Save into database
        logging.info("Ingesting Data into Database...")
        save_summary(clean_df, conn)

        logging.info("Vendor Summary Table Created Successfully.")

    except Exception as e:

        logging.error(f"Pipeline Failed: {e}")

    finally:

        conn.close()

        end_time = time.time()

        logging.info(f"Execution Time: {end_time-start_time:.2f} seconds")
        logging.info("------------ Vendor Summary Pipeline Completed ------------")

        print("Vendor summary created successfully!")
