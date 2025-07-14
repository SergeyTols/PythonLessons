# Zip

from zipfile import ZipFile
import os

# csv_files = [f for f in os.listdir() if f.endswith('.csv')]
# # print(csv_files)
# with ZipFile('archive.zip', 'w') as myzip:
#     for file in csv_files:
#         myzip.write(file)
#         os.remove(file)

# получить список
with ZipFile('archive.zip', 'r') as zip_obj:
    print(zip_obj.namelist())

# распаковать определенный
# files_to_extract = ['people.csv', 'file.csv']
#
# with ZipFile('archive.zip', 'r') as zip_obj:
#     zip_obj.extractall(members=files_to_extract)

# распаковать все
with ZipFile('archive.zip', 'r') as zip_obj:
     zip_obj.extractall()