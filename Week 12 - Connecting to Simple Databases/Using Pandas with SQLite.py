import sqlite3, sys
import pandas as pd

# SQLite uses files as the data source
# So it is very easy to move the database
try:
    sqlite_file="coffee.sqlite"
    conn = sqlite3.connect(sqlite_file)
    #               ^ If the file does not exist, then connect() will create the file
    
    select_all_persons ="SELECT * from PERSON_TABLE"
    df_persons = pd.read_sql_query(select_all_persons, conn, index_col="rowid")
    print(df_persons)
    
except Error as error:
    print(str(error))
    sys.exit(1)
finally:
    conn.close()
    # We should always close the connection.