import csv
import configparser
import psycopg2

# Read config from config file (Don't hardcode credentials)
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("postgres_config", "host")
port = parser.get("postgres_config", "port")
username = parser.get("postgres_config", "username")
password = parser.get("postgres_config", "password")
dbname = parser.get("postgres_config", "database")

# Make connection to database
conn = psycopg2.connect(
    host=host,
    port=port,
    user=username,
    password=password,
    dbname=dbname  
)
cursor = conn.cursor()

## Table 1 addresses ##
# Define destination folder
DATA_FOLDER = "data"
table = "addresses"
header = ["address_id", "address", "zipcode", "state", "country"]

# Write data to CSV file
with open(f"{DATA_FOLDER}/{table}.csv", "w") as f:
    writer = csv.writer(f)
    # Write header from given list
    writer.writerow(header)

    # Query data from database
    query = f"SELECT * FROM {table}"
    cursor.execute(query)

    # Write data to CSV file
    results = cursor.fetchall()
    for each in results:
        writer.writerow(each)

# ลองดึงข้อมูลจากตาราง order_items และเขียนลงไฟล์ CSV
# YOUR CODE HERE
## Table 2 order_items ##
# Define destination folder
table = "order_items"
header = ["order_id", "product_id", "quantity"]

# Write data to CSV file
with open(f"{DATA_FOLDER}/{table}.csv", "w") as f:
    writer = csv.writer(f)
    # Write header from given list
    writer.writerow(header)

    # Query data from database
    query = f"SELECT * FROM {table}"
    cursor.execute(query)

    # Write data to CSV file
    results = cursor.fetchall()
    for each in results:
        writer.writerow(each)