import snowflake.connector
#This script uses the Snowflake connector for Python to extract information about all databases from the Snowflake database, which it places in a array when Role Account Admin is selected, and then extracts information about a specific database and places it in DataFrame which exports to a CSV file.

ctx = snowflake.connector.connect( #This function connects Python and Snowflake using user data
    user='<username>',
    password='<password>',
    account='<account>'
    )

cs = ctx.cursor() #Making a constructor for creating a Cursor object, to use data from Snowflake
sql = "USE role ACCOUNTADMIN" #Function1 which selects a role account
cs.execute(sql) #Executing SQL query

sql = "SELECT CURRENT_ROLE()" #Function2 which sets a role from Function1 to be current
cs.execute(sql) #Executing SQL query

sql="SELECT DATABASE_NAME FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES" #Sql query that selects all databases..
cs.execute(sql) #Executing SQL query

array=[] #Making an array
array=cs.fetchall() #... and after executing the sql query the result is put in an array
print("All databases:")
print(array)

sql = "SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM SNOWFLAKE_SAMPLE_DATA.INFORMATION_SCHEMA.COLUMNS" #This query displays information about a specific database( in this case it is a database SNOWFLAKE_SAMPLE_DATA)
cs.execute(sql) #Executing SQL query

df = cs.fetch_pandas_all() #This function puts the result of the previous query in the DataFrame
print('\n')
print("Database: SNOWFLAKE_SAMPLE_DATA")
print('\n')
print(df)

df.to_csv(r'C:\Users\Nenad\Desktop\Snowflake_databases\SNOWFLAKE_SAMPLE_DATA_DB\Snowflake_sample_data_db_from_array.csv') #This way the DataFrame is exported to a CSV file
