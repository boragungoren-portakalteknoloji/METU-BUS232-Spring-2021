# Better file access with pandas library
# Please install pandas and optionally numpy.
# In Thonny this is done through Tools -> Manage Packages

import pandas as pd
import os

# Pandas is used to create a columnar structure from files which have comma (or any other) delimited lines.
# Because there is a delimiter (or separator), we can visualize them as columns..

# Here are first three lines of coffee.txt
# Name;Date;Coffee
# Bora;2021-05-18;7
# Tufan;2021-05-18;3

# Now assume it was an Excel file
# ------------------------------- 
# | Name  |     Date   | Coffee |
# -------------------------------
# | Bora  | 2021-05-18 |    7   |
# -------------------------------
# | Tufan | 2021-05-18 |    3   |
# -------------------------------

# Pandas provides this (and much more). 

cwd=os.getcwd()
print("Current working directry:", cwd)
print("Trying to identify coffee addicts in the office using a small sample over a short period.")
# The file name is for a file in the same folder
print("Populating data structure from file")
filename = cwd+"/"+"coffee.txt"


df = pd.read_csv(filename, sep=";") # reads into a dataframe, sep is the delimiter. Default value is ","
# Note that, in Turkish  and many European locales numbers are written like 1.000.000,00
# Whereas in US locale, numbers are written like: 1,000,000.00
# So using "," as delimiter is problematic in many cases. ";" is the second most used delimiter.
# It is also very common to use ";" in Turkey.

# Now that we have a pandas "dataframe" let's see what it can do.
print("Indexes:")
print(df.index) # gives me a guide on using an index variable to access individual rows in a while/for loop
print("Column names:")
print(df.columns) # gives me a guide on *how* the column names have been read. This should be done before coding. 
print("Entire table:")
print(df)

# Pandas is column oriented.
# As long as the characters in a column name are OK wit Python variable names, you can access a entire column like this:
print("Coffee consumption in general")
avg = df.Coffee.mean()
#     ^ df.Coffee is the column with the name "Coffee" in the header.
#               ^ mean() function is called through this particular column, so it operates on the *entire* column
#                 No need for looping.

# Another way to access an individual column is to use [] operator.
# This is more suitable with column names including non-English characters or spaces in between
avg = df["Coffee"].mean()
#       ^ In this way, the [] operator searches for the column with title "Coffee" and returns the column as a separate object
#       Then mean() is called similar to the previous method.

print("Average:","{:.2f}".format(avg))
#                     ^ Note: If you'd like to use this method of formatting,
#                     here is a short explanation -- https://mkaz.blog/code/python-string-format-cookbook/

# We can also do some Linux-esque filtering. Look up commands head, tail, grep, etc. 
print("The first two lines in the Coffee column:")
print(df.Coffee.head(2))
print("The last two lines in the Coffee column:")
print(df["Coffee"].tail(2))
input("Press enter to continue")

print("Unique values in the Name column:")
unique_names = df["Name"].unique()
                    #     ^ returns a list of unique values. 
print(unique_names)

# We can also do Excel-like data filters and groupings
print("Total coffee consumption by person:")
print( df.groupby("Name")["Coffee"].sum() )

# A pandas groupby() splits the table into data groups based on some (column-based) criteria.
# In the above example, the grouping is based on the value of "Name" column.
# Then for each of the groupings, ["Coffee"]

# We can also have multiple groupings
print( df.groupby(["Name", "Date"]).sum() )
#                  ^ Group by Name, then within each (Name) group, group by Date.
#                                    ^ Then calculate sum for these groups (i.e. for each person and each day)
input("Press enter to continue")

# If your work is about columns, Pandas maybe the best tool for you.
# If you work with rows, Pandas might look a bit awkward to use at first
# But there are many ways to do iterations. 

# You can use the autogenerated index.
print("Autogenerated index")
for index in df.index:
    # The index attribute is auto-generated by Pandas when reading the table from the file
    print(index, df["Name"][index])
# You can use index-1, index2, etc but because of the nature of for .. in loop, it is hard to construct a loop using
# calculated indexes.
input("Press enter to continue")

# You can use the length and a range, and access using loc()
print("Using loc() to access")
size = len(df)
# The row indexes are 0, 1, .... , size-1
# range function builds a sequence just like that
for index in range(size):
    print(index, df.loc[index,"Name"])
#                    ^ loc takes you to the row with the given index.
#                      In this loop, there is no iteration conducted by the data frame
#                      We iterate a number that matches the index on the data frame, that's all.
#                      using index-1, index-2, etc arithmetic still requires care.
#                      But this time, we are more aware of the risks, because we explicitly create the index range
input("Press enter to continue")

# You might prefer to use column indexes instead of column names, and access using iloc()
print("Using iloc() to access")
size = len(df)
for index in range(size):
    print(index, df.iloc[index,0])
#                    ^ iloc works exactly like loc, but with column indexes as numbers
input("Press enter to continue")

# If you'd like to be able to access the entire row while iterating with an index,
# then iterrows() is a perfect tool 
print("Using iterrows() to access")
for index, row in df.iterrows():
#                      ^ this is implemented by an iterator. iterrows returns a sequence of pairs
#    ^ After each iteration *both" index and row are updated
    print(index, row["Name"])
input("Press enter to continue")