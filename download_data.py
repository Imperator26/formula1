#!/usr/bin/env python
# coding: utf-8

import requests as r
import shutil
from zipfile import ZipFile

def download_file(url):
    file_name = url.split("/")[-1]

    res = r.get(url, stream=True)

    with open(file_name, "wb") as f:
        shutil.copyfileobj(res.raw, f)

    return file_name

f1db_url = "http://ergast.com/downloads/f1db_csv.zip"
file_name = download_file(f1db_url)

with ZipFile(file_name, "r") as zip_ref:
    zip_ref.extractall("./data")

f1db_schema_url = "http://ergast.com/schemas/f1db_schema.txt"
file_name = download_file(f1db_schema_url)
