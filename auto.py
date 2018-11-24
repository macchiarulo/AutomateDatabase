# AutomateDatabase
# Automate Database to AWS S3 Bucket (Python, MySQL, PHP)
import pymysql

conn = pymysql.connect(host= '[host]',user='[username]',password='[password]',db='[database_name]')
a = conn.cursor()

sql = 'SELECT * from [table_name]'
a.execute(sql)

data = a.fetchone()
print(data)

data_folder = "[php_local_host_path]"
file_to_open = data_folder + "[text_file_name_saved_in_php_localhost_to_refresh]"
f = open(file_to_open, 'w')
f.write(str(data))
f.close()

