import sqlite3, sys
import pandas as pd

def sqlite_select_query(conn, query):
    try:
        cursor=conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
        cursor.close()
    except sqlite3.Error as error:
        print(str(error))
    return
    

# SQLite uses files as the data source
# So it is very easy to move the database
try:
    sqlite_file="coffee.sqlite"
    conn = sqlite3.connect(sqlite_file)
    #               ^ If the file does not exist, then connect() will create the file

    # 1- create a test database named testDB
    cur = conn.cursor()

    # 2- create 2 tables
    # person_table : pid, name, phone number
    # consumption_table : cid, pid, date, number of cups
    print("Creating tables.")
    cur.execute("CREATE TABLE IF NOT EXISTS PERSON_TABLE (rowid INTEGER PRIMARY KEY, name TEXT NOT NULL, personnel_ID INTEGER NOT NULL UNIQUE, phone_number TEXT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS CONSUMPTION_TABLE (rowid INTEGER PRIMARY KEY, personnel_ID INTEGER NOT NULL, date DATE NOT NULL, cups INTEGER NOT NULL, FOREIGN KEY (personnel_ID) REFERENCES PERSON_TABLE (personnel_ID) )")
    
    # print the names of created tables
    print("Names of tables in DB.")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())
    
    # 3- populate tables from CSV files
    # normally some other application should populate the DB.
    # https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.to_sql.html
    print("Populating tables.")
    person_phone = pd.read_csv("user_phone.csv",sep=",")
    person_phone.to_sql("PERSON_TABLE", conn, if_exists="append", index = True, index_label="rowid")
    #                                                              ^ if you cannot  map the pandas index, then just set this to False
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
    
    conn.commit()
except sqlite3.Error as error:
    print("We have an error:", str(error))
    sys.exit(1)
finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed.")

# 3- populate tables