# Simple file access
# Adapted from a previous semester example
# Original from -- https://github.com/boragungoren-portakalteknoloji/METU-BA4318-Spring2019/

# There are *several* little details in file access
# Please take some time to read the following article after our class -- https://realpython.com/read-write-files-python/

import sys
import os

# Understanding which directory your program is working on is important
# We expect to see it as the same directory as the .py file, but it might be different
# based on how we invoke the program
cwd=os.getcwd()
print("Current working directry:",cwd)
# os.chdir("/home/bora") # this would change the CWD effectively

print("Trying to identify coffee addicts in the office using a small sample over a short period.")
# The file name is for a file in the same folder
print("Populating data structure from file")
fname = cwd+"/"+"coffee.txt"

if os.path.exists(fname)==False:
    print("Error. The file path does not point to a file.")
    sys.exit(1)

def read_from_file(filename):
    infile=None # file handle representing our connection to the file
    # ^ by convention anyone who sees "in" understands this is a handle for input only (read-only)
    parsed_data=None # variable for the data structure
    try:
        infile = open(filename,"r") # when created, infile will have some meta-data
        # r for reading, w for writing, a for appending, b is buffered
        data_set = {} # scratch variable, when done will be assigned onto parsed_data
        if infile.readable: # .readable is a meta-data. it is not a function. 
            header_line = infile.readline().strip()
            #                     ^ reads a complete line, and returns as a string
            #                               ^ strip() will clear spaces on both ends, also invisible characters for line ending
            #                                  CR -> carriage return (get to the next line for editing
            #                                  LF/EOL -> linefeed (get to the next line)
            #                                  if you see a file of single line which was supposed to be multiple, it is line ending mismatch.
            column_names = header_line.split(";")
                            # gives us a list of separate strings
            print("Column names:", column_names)
            # parsing the data file
            data_lines = infile.readlines()
                        #       ^ reads ALL remaining lines at once, creates a list of strings holding each line as a separate item
                        # we can now iterate over the list of strings. 
            for data_line in data_lines:
                data_line=data_line.strip()
                columns = data_line.split(";")
                # ^ list of strings. if there are any numbers, they appear like "1" but not 1
                # print(columns)
                consumer_name = columns[0]
                consumption_date = columns[1]
                consumption_amount = int(columns[2])
                consumption_occasion = (consumption_date, consumption_amount)
                                        # ^ tuple holding date and amount
                # use the dictionary to map name -> consumption history
                # then I can pick each name and calculate total cofee consumption from each separate history
                # to represent the history I need an "entry" to hold the date and the amount.
                # So each tuple is an "entry" and a list of tuples is the history.
                # mapping names (string) onto a history (list) of entries (tuples of string and integer)
                # names are keys in the key-value pair of dictionary
                if consumer_name in data_set:
                    # There is already an entry for this name
                    data_set[consumer_name].append(consumption_occasion)
                    # ^ I know that there is a list that I can access through the key, because consumer_name was in the data_set
                else:
                    # This is the first time we see this name
                    # create empty list
                    data_set[consumer_name] = []
                    # Now there is an entry for this name. The name works as a key to access the empty list above.
                    data_set[consumer_name].append(consumption_occasion)
            # for loop done = all lines are now in the data set.
            parsed_data=data_set
        else:
            print ("Problem reading file")
            parsed_data=None
    except IOError as error:
        print('Can not open file due to error:', str(error))
        sys.exit(1)
    finally:
        infile.close()
    # Return the contents of the file read and parsed into the variable
    return parsed_data


# dictionary mapping name -> list of consumption occasions. Each occasion has date and amount. 
consumption_data=read_from_file(filename=fname)
if consumption_data == None:
    print("No consumption data available. ")
    sys.exit(1)

# We have the data. We just need to process it.

def get_personal_stats(data_dictionary, consumer_name):
    # Extract list
    occasions=data_dictionary[consumer_name]
                # get the value in key-value pair
    number_of_days=len(occasions)
            # Assumption (we know to fail) is that there is no repeating entries for a single day.
            # Creates a small bug. Challenge yourselves to solve this. 
    total_consumption=0
    for occasion in occasions:
        # Each occasion is a tuple
        total_consumption=total_consumption+occasion[1]
    # total_consumption calculated
    return (number_of_days, total_consumption)
#           ^ return a tuple

input("Press enter to continue")
for name in consumption_data:
    result=get_personal_stats(data_dictionary=consumption_data, consumer_name=name)
    #       ^ returns tuple
    print("Consumer ", name, "has consumed", result[1], "cups of coffee in", result[0], "days")

