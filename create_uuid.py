import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='formbot', passwd='formbot', db='formbot')
cursor = db.cursor()
with open('coupon.txt','r') as f:
    lines = f.readlines()
for line in lines:
    sql = "INSERT INTO `fb_coupon` (`id`, `uuid`, `ctime`, `used`, `uid`) VALUES (NULL, '{0}', NULL, 0, NULL );".format(line)
    print(sql)
    cursor.execute(sql)
    # data = cursor.fetchone()
    # print ("Database version : %s " % data)
db.close()