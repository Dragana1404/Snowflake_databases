import snowflake.connector
#This script uses the Snowflake connector for Python to extract information on how many tables a particular Database has in a particular schema.

ctx = snowflake.connector.connect(#This function connects Python and Snowflake using user data
    user='<user>',
    password='<password>',
    account='<account>'
    )

cs = ctx.cursor() #Making a constructor for creating a Cursor object, to use data from Snowflake
sql = "USE role ACCOUNTADMIN" #Function1 which selects a role account
cs.execute(sql) #Executing SQL query

sql = "SELECT CURRENT_ROLE()" #Function2 which sets a role from Function1 to be current
cs.execute(sql) #Executing SQL query

sql="SELECT TABLE_NAME FROM DRAGANA.INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='PUBLIC'" #In this case, we want to show the tables in Database DRAGANA and the public schema
cs.execute(sql) #Executing SQL query

array=[] ##Making an array
array=cs.fetchall() #After executing the sql query the result is put in an array

print("In the DRAGANA Database and the public schema, the number of tables is:")
print(len(array)) #This function shows the length of the array, and in this case it is the number of tables that meet the above condition