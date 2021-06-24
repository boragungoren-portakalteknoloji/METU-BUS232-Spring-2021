import sqlite3, sys
# for every database there is a different library prepared by the producers of that db
# for oracle, for mysql, for postgresql, for db2, and for sqlite3.
# there is a more advanced way to connect called object relational mapping (ORM)
import pandas as pd

def sqlite_select_query(conn, query):
    try:
        cursor=conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        # ^ records is assigned all the results
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records: # records i iterable
            print(row)
        cursor.close() # removes the resources assigned to hold the results in memory
        # ^ this is important.
    except sqlite3.Error as error:
        print(str(error))
        # DB errors contain error codes.
    # we did not close the connection because it was passed as a parameter
    # the owner (i.e. who created the connection is out of this scope)
    # the owner can still close the connection after the function call is over. 
    return
    

# SQLite uses files as the data source
# So it is very easy to move the database
try:
    sqlite_file="coffee.sqlite" # another convention is to end up with .db in the file name
    conn = sqlite3.connect(sqlite_file)
    #               ^ If the file does not exist, then connect() will create the file

    # 1- create a test database named testDB
    cur = conn.cursor()
    # More advanced databases have parameters to create tyes of cursors with different abilities.

    # 2- create 2 tables
    # person_table : pid, name, phone number
    # consumption_table : cid, pid, date, number of cups
    # ANSI created a common base for database languages: Structural Query Language (SQL - pronounced as sequel)
    # Every database has a dialect of ANSI SQL
    print("Creating tables.")
    cur.execute("CREATE TABLE IF NOT EXISTS PERSON_TABLE (rowid INTEGER PRIMARY KEY, name TEXT NOT NULL, personnel_ID INTEGER NOT NULL UNIQUE, phone_number TEXT NOT NULL)")
    #              ^ Actual command + parameters (vary on what the command is)
    #                           ^ so if we are creating the database from nothing (i.e. file not existing beforehand), we create the table
    #                             if the database exists, and the table exists, we do nothing.
    #                                         ^ table's name ( ...  )
    #                                                           ^ the columns of the database and the type of data each column has and any parameters
    #                                                               NOT NULL -> there has to be some data, can not be left empty (important when inserting)
    #                                                               UNIQUE -> in the whole table, there can be only one row with this value (importand when inserting)
    cur.execute("CREATE TABLE IF NOT EXISTS CONSUMPTION_TABLE (rowid INTEGER PRIMARY KEY, personnel_ID INTEGER NOT NULL, date DATE NOT NULL, cups INTEGER NOT NULL, FOREIGN KEY (personnel_ID) REFERENCES PERSON_TABLE (personnel_ID) )")
    #                                                            ^ rowid is the index variable used by SQLite. It will get created no matter what.
    #                                                                          ^ We search in this table based on the value of the field/fields designated as PRIMARY KEY
    #                                                                                                                                                                   ^ This is a key in another table.
    #                                                                                                                                                                   We use it to quickly reference a row in that particular table
    
    # There should be some work to create an optimal database. Usually analysts create a picture of business processes and engineers translate those into DB structure
    # This work takes TIME
    # Once it is done, we take the structure and its efficiency for granted. 
    
    # print the names of created tables
    print("Names of tables in DB.")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #               ^ this command is a query that ends up with data returned.
    #                 part of it could be about the DB itself
    #                 select field from table_name where conditions
    #                 select * from .... -> select everything
    #                           sqlite_master table holds data about the DB itself
    # the cursor points to the result (which is in memory)
    print(cur.fetchall())
    #         ^ fetches the results pointed to
    
    # 3- populate tables from CSV files
    # normally some other application should populate the DB.
    # https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.to_sql.html
    print("Populating tables.")
    person_phone = pd.read_csv("user_phone.csv",sep=",")
    # ^ this is a data frame
    person_phone.to_sql("PERSON_TABLE", conn, if_exists="append", index = True, index_label="rowid")
    #                    ^ table name,   ^ connection to use         ^ if you cannot  map the pandas index, then just set this to False
    #                                                                and do not use the index_label parameter as well.
    # Insert the values from the csv file into the table "PERSON_TABLE" 
    coffee_consumption = pd.read_csv("coffee_consumption.csv",sep=",")
    coffee_consumption.to_sql("CONSUMPTION_TABLE", conn, if_exists="append", index = True, index_label="rowid")
    # Insert the values from the csv file into the table "CONSUMPTION_TABLE"
    
#     # 4- Test some queries
    print("Testing data in tables.")
    print("All data in PERSON_TABLE; method 1")
    select_all_names ="SELECT * from PERSON_TABLE"
    sqlite_select_query(conn,select_all_names)
    
    print("All data in CONSUMPTION_TABLE; method 1")
    select_all_consumption ="SELECT * from CONSUMPTION_TABLE"
    sqlite_select_query(conn,select_all_consumption)
    
    # cur.close() #
    conn.commit() # Tell the DB we are done. This also means commit all changes due to my actions to the file.
    # This is important
except sqlite3.Error as error:
    print("We have an error:", str(error))
    sys.exit(1)
finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed.")
print("We are done.")