import snowflake.connector
#This is an example of how to determine how many rows to display. This example is useful when there are a large number of rows
ctx = snowflake.connector.connect( #This function connects Python and Snowflake using user data
    user='<user>',
    password='<password>',
    account='<account>'
    )


cs = ctx.cursor() #Making a constructor for creating a Cursor object, to use data from Snowflake
sql = "USE role ACCOUNTADMIN" #Function1 which selects a role account
cs.execute(sql) #Executing SQL query

sql = "SELECT CURRENT_ROLE()" #Function2 which sets a role from Function1 to be current
cs.execute(sql) #Executing SQL query

sql="SELECT * FROM DRAGANA.INFORMATION_SCHEMA.COLUMNS LIMIT 2" #This query displays information about columns with a specified number of rows in the output
cs.execute(sql) #Executing SQL query

df = cs.fetch_pandas_all() #This function puts the result of the previous query in the DataFrame
print(df)