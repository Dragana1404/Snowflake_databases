import snowflake.connector
#Snowflake connector for Python
#This is an example of displaying TABLE_SCHEMA, COLUMN_NAME and DATA_TYPE from a specific database

ctx = snowflake.connector.connect(#This function connects Python and Snowflake using user data
    user='<username>',
    password='<password>',
    account='<account>'
    )

cs = ctx.cursor() #Making a constructor for creating a Cursor object, to use data from Snowflake
sql = "USE role ACCOUNTADMIN" #Function1 which selects a role account
cs.execute(sql) #Executing SQL query

sql = "SELECT CURRENT_ROLE()" #Function2 which sets a role from Function1 to be current
cs.execute(sql) #Executing SQL query

sql = "SELECT TABLE_SCHEMA, COLUMN_NAME, DATA_TYPE FROM UTIL_DB.INFORMATION_SCHEMA.COLUMNS"  #This query displays information about a specific database( in this case it is a database UTIL_DB)
cs.execute(sql) #Executing SQL query

df = cs.fetch_pandas_all() #This function puts the result of the previous query in the DataFrame
print(df)
df.to_csv(r'C:\Users\Nenad\Desktop\Snowflake_databases\UTIL_DB\Util_db.csv') #This way the DataFrame is exported to a CSV file





