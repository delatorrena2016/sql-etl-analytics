#Copying an entire local DuckDB database To MotherDuck
import duckdb
# We make the connection
con = duckdb.connect('md:')
# One could otherwise manipulate local from md
#con.sql("ATTACH 'C:\\Users\\delat\\sql-etl-analytics\\src\\data\\adidas.duckdb'")
# **RUN ONCE** to create remote database from local as a copy
con.sql("CREATE DATABASE cloud_adidas FROM 'C:\\Users\\delat\\sql-etl-analytics\\src\\data\\adidas.duckdb'")
# We reckon remote db
con.sql("SHOW DATABASES").show()
# All manipulations go through as this
con.sql("SELECT Discount FROM cloud_adidas.data_adidasvsnike")