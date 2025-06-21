import csv
import configparser
import requests

# Read config from config file (Don't hardcode credentials)
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("api_config", "host")
port = parser.get("api_config", "port")

API_URL = f"http://{host}:{port}"

# Define destination folder
DATA_FOLDER = "data"

### Events
data = "events"
date = "2021-02-10"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
print(f"({data}) Request URL: {f"{API_URL}/{data}/?created_at={date}"}")
data = response.json()

# Write data to CSV file
with open(f"{DATA_FOLDER}/events.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    # Write header from first row's key
    writer.writerow(header)

    # Write data to CSV file
    for each in data:
        writer.writerow(each.values())

### Users
data = "users"
date = "2020-10-23"
# ลองดึงข้อมูลจาก API เส้น users และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
print(f"({data}) Request URL: {f"{API_URL}/{data}/?created_at={date}"}")
data = response.json()

# Write data to CSV file
with open(f"{DATA_FOLDER}/users.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    # Write header from first row's key
    writer.writerow(header)

    # Write data to CSV file
    for each in data:
        writer.writerow(each.values())

### Orders
data = "orders"
date = "2021-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
print(f"({data}) Request URL: {f"{API_URL}/{data}/?created_at={date}"}")
data = response.json()

# Write data to CSV file
with open(f"{DATA_FOLDER}/orders.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    # Write header from first row's key
    writer.writerow(header)

    # Write data to CSV file
    for each in data:
        writer.writerow(each.values())