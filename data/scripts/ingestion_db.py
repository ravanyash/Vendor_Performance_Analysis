import os
import time
import logging
import pandas as pd
from sqlalchemy import create_engine

# --------------------------------------------------
# Create logs directory if it doesn't exist
# --------------------------------------------------
os.makedirs("logs", exist_ok=True)

# --------------------------------------------------
# Configure Logging
# --------------------------------------------------
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# --------------------------------------------------
# Create SQLite Database Connection
# --------------------------------------------------
engine = create_engine("sqlite:///inventory.db")


def ingest_db(df, table_name, engine):
    """
    Ingest a DataFrame into the SQLite database.

    Parameters:
        df (DataFrame): DataFrame to store.
        table_name (str): Name of the SQL table.
        engine: SQLAlchemy database engine.
    """
    try:
        df.to_sql(
            table_name,
            con=engine,
            if_exists="replace",
            index=False
        )
        logging.info(f"Successfully ingested table '{table_name}'")

    except Exception as e:
        logging.error(f"Error ingesting '{table_name}': {e}")


def load_raw_data():
    """
    Load all CSV files from the current directory
    and ingest them into the SQLite database.
    """
    start_time = time.time()

    logging.info("------------ Data Ingestion Started ------------")

    csv_found = False

    for file in os.listdir():

        if file.endswith(".csv"):
            csv_found = True

            try:
                logging.info(f"Reading file: {file}")

                df = pd.read_csv(file)

                table_name = os.path.splitext(file)[0]

                ingest_db(df, table_name, engine)

            except Exception as e:
                logging.error(f"Failed to process {file}: {e}")

    if not csv_found:
        logging.warning("No CSV files found in the current directory.")

    end_time = time.time()
    total_time = (end_time - start_time) / 60

    logging.info("------------ Data Ingestion Completed ------------")
    logging.info(f"Total Time Taken: {total_time:.2f} minutes")


if __name__ == "__main__":
    load_raw_data()
    print("Data ingestion completed successfully!")