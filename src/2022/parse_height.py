import csv
with open('data/height.dat') as file:
    data = file.read().splitlines()

with open('data/height.csv', 'w') as outfile:
    for line in data[5:]:
        line = line.replace(',', '.')
        line = line.replace('\t', ' ')
        line = line.replace('..', 'Na')
        line = line.replace('  ', ' ')
        line = line.replace(' ', ', ')

        outfile.write(line +'\n')

    
import pandas as pd
df = pd.read_csv('data/height.csv', header=None)
print(df.head())