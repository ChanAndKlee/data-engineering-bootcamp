import configparser
import pysftp

# Read config from config file (Don't hardcode credentials)
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
username = parser.get("sftp_config", "username")
password = parser.get("sftp_config", "password")
host = parser.get("sftp_config", "host")
port = parser.getint("sftp_config", "port")

# Security risk! Don't do this on production
# You lose a protection against Man-in-the-middle attacks
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Define destination folder
DATA_FOLDER = "data"

# โค้ดด้านล่างจะเป็นการโหลดไฟล์ orders.csv ซึ่งเป็นข้อมูล orders
# ให้แก้โค้ดด้านล่างให้ไปโหลดไฟล์ข้อมูล products และ promos แทน
files = [
    "orders.csv",
    # YOUR CODE HERE
    "products.csv",
    "promos.csv"
]

# Destination path (SFTP directory)
REMOTE_FOLDER = "/"

# Get/download files from SFTP server
with pysftp.Connection(host, username=username, password=password, port=port, cnopts=cnopts) as sftp:
    for f in files:
        sftp.get(f"{REMOTE_FOLDER}/{f}", f"{DATA_FOLDER}/{f}")
        print(f"Finished downloading: {f}")