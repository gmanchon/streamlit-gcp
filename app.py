
import streamlit as st

import pandas as pd

from google.cloud import storage

BUCKET_NAME = "le-wagon-data"
storage_filename = "data/train_1k.csv"
local_filename = "train_1k_downloaded.csv"
upload_storage_filename = "data/train_1k_uploaded.csv"

# download file
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob(storage_filename)
blob.download_to_filename(local_filename)

# df
df = pd.read_csv(local_filename)
df

# upload file
upload_blob = bucket.blob(upload_storage_filename)
upload_blob.upload_from_filename(local_filename)
