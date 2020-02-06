# importing pandas package
import pandas as pd
import csv

data1 = pd.read_csv("MOCK_DATA.csv")
data2 = pd.read_csv("MOCK_DATA2.csv")

dataFinal = pd.merge(data1, data2, how="inner", on='ip address') # find the matching column between both of the files, which is ip address.

print(dataFinal)

dataFinal.to_csv(r'MOCK_DATA_WRITE_TO.csv', index=False)

# append rows to the end of the csv file

mockObject = csv.reader('MOCK_DATA_WRITE_TO.csv')

row_count = len(dataFinal)

with open('MOCK_DATA_WRITE_TO.csv', mode='a') as output_file:
    output_file.write("\n" + "Total Count: " + str(row_count) + " computers need to be patched")
