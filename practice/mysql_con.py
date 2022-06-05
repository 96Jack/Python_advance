import pymysql

kwargs = {
    'db'          :'djtest',
    'user'        :'root',
    'passwd'      :'123456',
    'host'        :'xx.xx.xx.xx',
    'port'        : 3306,
    'charset'     :'utf8'
}

db = pymysql.connect(**kwargs)
cursor = db.cursor()
cursor.execute("select version();")
data = cursor.fetchone()
print(" Database Version:%s" % data)
