import snowflake.connector
#This example shows how we can extract as many rows as possible from the Database so that the result is clear
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

sql = "SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES" #This query selects all tables from the Snowflake user Database
cs.execute(sql) #Executing SQL query

result=cs.fetchall() #Function that takes over the result of the query

for x in result: #The loop is used to display each row from the result
    print(x)
