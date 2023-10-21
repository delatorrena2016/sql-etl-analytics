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
def extract_data(dataset_id, data_dir, file_name):
    """Extract data from URL and return a dataframe"""
    # Check if 'data' folder exists, if not, create it
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download data from Kaggle and save it to 'data' folder
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_id, path=data_dir, unzip=True)

    if "csv" in file_name:
        df = pd.read_csv(f'{data_dir}/{file_name}')
    elif "xlsx" in file_name and "Adidas" in file_name:
        df = pd.read_excel(f'{data_dir}/{file_name}', sheet_name="Data Sales Adidas", skiprows=range(4), usecols="B:N")
    else: 
        df = pd.DataFrame()
    return df

def extract_unique_season_and_category(df):
    #create a copy
    df_copy_2 = df.copy()

    # Extract unique values for 'Season' and 'Category' columns
    unique_seasons = df_copy_2['Season'].unique()
    unique_categories = df_copy_2['Category'].unique()
    
    print("Unique Seasons:", unique_seasons)
    print("Unique Categories:", unique_categories)

    return df_copy_2

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

    # First data extraction from URL
    kaggle_id = 'heemalichaudhari/adidas-sales-dataset'
    data_dir = os.path.join('.', 'src/data')
    file_name_adidas = "Adidas US Sales Datasets.xlsx"
    df_adidas = extract_data(kaggle_id,data_dir, file_name_adidas)
    clean_df_adidas = data_cleaning_and_saving(df_adidas)
    
    table_name = 'data_sales_adidas'
    # Save the cleaned data to DuckDB
    save_to_duckdb(df_adidas, table_name, f'{data_dir}/adidas.duckdb')
# -


    # Second data extraction from URL
    kaggle_id = 'iamsouravbanerjee/customer-shopping-trends-dataset'
    file_name_trends  = "shopping_trends.csv"
    df_trends = extract_data(kaggle_id,data_dir, file_name_trends)
    clean_df_trends = extract_unique_season_and_category(df_trends)
    
    table_name = 'data_shopping_trends'
    # Save the cleaned data to DuckDB
    save_to_duckdb(clean_df_trends, table_name, f'{data_dir}/adidas.duckdb')

    

    # Third data extraction from URL
    kaggle_id = 'kaushiksuresh147/adidas-vs-nike'
    file_name  = "Adidas Vs Nike.csv"
    df = extract_data(kaggle_id,data_dir, file_name)
    
    table_name = 'data_adidasvsnike'
    # Save the cleaned data to DuckDB
    save_to_duckdb(df, table_name, f'{data_dir}/adidas.duckdb')