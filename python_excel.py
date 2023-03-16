import pandas as pd

# Step 1: Read the Excel file into a DataFrame
data_frame = pd.read_excel('path/to/excel/file.xlsx', sheet_name='Sheet1')

# Step 2: Select the column containing the dates
dates_column = data_frame['Date']

# Step 3: Convert the dates column to a list
dates_list = dates_column.tolist()

# Step 4: Print out the dates list
print(dates_list)
