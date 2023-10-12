# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None


# +
import os
import kaggle
import pandas as pd
import duckdb


# Check if 'data' folder exists, if not, create it
# Set the path relative to the script
def extract_data(dataset_id, data_dir):
    """Extract data from URL and return a dataframe"""
    # Check if 'data' folder exists, if not, create it
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download data from Kaggle and save it to 'data' folder
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_id, path=data_dir, unzip=True)

    df = pd.read_excel(f'{data_dir}/Adidas US Sales Datasets.xlsx', sheet_name="Data Sales Adidas", skiprows=range(4), usecols="B:N")
    return df

def save_to_duckdb(df, table_name, db_path):
    """Save dataframe to duckdb"""
    conn = duckdb.connect(db_path)
    conn.register('df', df)
    
    # Check if table already exists, if not, create it
    tables = conn.execute("SHOW TABLES").fetchall()
    if table_name not in [table[0] for table in tables]:
        conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
    
    conn.close()

# Get range of data dates
def data_cleaning_and_saving(df):
    df_copy = df.copy()
    # Get the start date (oldest date)
    start_date = df_copy['Invoice Date'].min()

    # Get the last date
    last_date = df_copy['Invoice Date'].max()

    print("Start Date:", start_date)
    print("Last Date:", last_date)

    df_copy['Invoice Date'] = pd.to_datetime(df['Invoice Date'])

    return df_copy



if __name__ == "__main__":

    # Extract data from URL
    kaggle_id = 'heemalichaudhari/adidas-sales-dataset'
    data_dir = os.path.join('.', 'data')
    df = extract_data(kaggle_id,data_dir)
    clean_df = data_cleaning_and_saving(df)
    
    table_name = 'data_sales_adidas'
    # Save the cleaned data to DuckDB
    save_to_duckdb(df, table_name, f'{data_dir}/adidas.duckdb')
