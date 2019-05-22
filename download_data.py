#!/usr/bin/env python
# coding: utf-8

import requests
import io
from zipfile import ZipFile

f1db_url = "http://ergast.com/downloads/f1db_csv.zip"
f1db_schema_url = "http://ergast.com/schemas/f1db_schema.txt"

r = requests.get(f1db_url, stream=True)
file = ZipFile(io.BytesIO(r.content))
file.extractall("./data/")

r = requests.get(f1db_schema_url)
with open("./data/f1db_schema.txt", "w") as f:
    f.write(r.text)
