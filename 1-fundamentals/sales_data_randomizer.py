import csv
import shutil

filename = '1-fundamentals\sales_data.csv'
backup_directory = '1-fundamentals\csv_backup'

shutil.copy(filename, backup_directory)

with open(filename, 'r', encoding='utf-8', newline='') as csv_file:
  sample = ''
  for line in range(3):
    sample += csv_file.readline()
  
  data_dialet = csv.Sniffer().sniff(sample)
  csv_file.seek(0)
  reader = csv.reader(csv_file, data_dialet)
  for row in reader:
    print(row)
  
  # todo: write