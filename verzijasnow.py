import snowflake.connector

ctx = snowflake.connector.connect(

    user='databar',
    password='Databar1!',
    account='mta30327.us-east-1'
    #warehouse='COMPUTE-WH'
    #database='DRAGANA',
    #schema='PUBLIC'
    )

cs = ctx.cursor()
sql = "USE role ACCOUNTADMIN"
cs.execute(sql)
sql = "SELECT CURRENT_ROLE()"
cs.execute(sql)
sql = "SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM UTIL_DB.INFORMATION_SCHEMA.COLUMNS"
cs.execute(sql)
df = cs.fetch_pandas_all()
print(df)
df.to_csv(r'C:\Users\Nenad\Desktop\Snowflake_databases\UTIL_DB\Util_db_information.csv')