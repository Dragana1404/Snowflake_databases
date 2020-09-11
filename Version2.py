import snowflake.connector

ctx = snowflake.connector.connect(
    user='<username>',
    password='<password>',
    account='<account>'
    )

cs = ctx.cursor()
sql = "USE role ACCOUNTADMIN"
cs.execute(sql)
sql = "SELECT CURRENT_ROLE()"
cs.execute(sql)
sql="SELECT DATABASE_NAME FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES"
cs.execute(sql)
array=[]
array=cs.fetchall()
print("All databases:")
print(array)
sql = "SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM SNOWFLAKE_SAMPLE_DATA.INFORMATION_SCHEMA.COLUMNS"
cs.execute(sql)
df = cs.fetch_pandas_all()
print('\n')
print("Database: SNOWFLAKE_SAMPLE_DATA")
print('\n')
print(df)
df.to_csv(r'C:\Users\Nenad\Desktop\Snowflake_databases\SNOWFLAKE_SAMPLE_DATA_DB\Snowflake_sample_data_db_from_array.csv')
