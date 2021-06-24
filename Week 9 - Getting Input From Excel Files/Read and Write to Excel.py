# Reading and writing to Excel requires a number of libraries.
# Although we only import pandas, you need to install xlrd and openpyxl
import pandas as pd
import os

cwd=os.getcwd()
print("Current working directry:", cwd)
print("Trying to identify coffee addicts in the office using a small sample over a short period.")
# The file name is for a file in the same folder
print("Populating data structure from file")
filename = cwd+"/"+"Week-9-Company-Trip.xlsx"

# We will demonstrate a few features of read_excel
# Please read the documentation to understand what other features exist
# Here is a link -- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

df = pd.read_excel(filename, converters={'Phone Number':str})
#                             ^ We'd like to keep the phone number column as text, so we explicitly specify it
# This is more common than you'd expect. ZIP codes, product codes, etc usually have 0's at their beginning and we want to keep those zeroes
# For some examples on how to work with documents, see -- https://pbpython.com/pandas-excel-range.html

# Let's apply some filters
filter_results=df["Phone Number"].str.startswith("5")
# filter results are not the rows but boolean results that show if a row matches the filters
# This is useful, because not this particular filter's results can ben transmitted to other locations. 
print(filter_results)

# To access filtered rows
filtered_rows=df.loc[filter_results]
print(filtered_rows)

# Those who put 0 in front of the phone number did not appear. So let's resolve that issue.
for i, row in df.iterrows():
    phone_number = df.at[i, "Phone Number"]
    #                 ^ We get the value in the cell.
    #                 Note that this is a string
    if phone_number.startswith("0") == True:
        phone_number = phone_number[1:]
        # Simple string slicing is enough in this case      
    df.at[i, "Phone Number"] = phone_number
    # We can also assign values to cells using df.at[]
print(df)

# Output to Excel
out_fname=cwd+"/"+"filtered.xlsx"
df.to_excel(out_fname)
# Note that there are many options here as well -- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
print("Filtered results are written on an excel file.")

# Note: If you want to process Excel files, there are many options out of Pandas as well.
# Some of these options enable charts, textboxes and even VBA macros
# Please see -- https://xlsxwriter.readthedocs.io/index.html