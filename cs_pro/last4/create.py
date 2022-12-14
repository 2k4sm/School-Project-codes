import mariadb as md

con = md.connect(host = 'localhost',user ='root',passwd = 'heaven',database = 'sm2k4')
curs = con.cursor()

