def connectToMyDatabase():
    import pymysql as sq
    mycon = sq.connect(host='', user='root', password='', database='classdb')
    return mycon

def showAllData():

    cn = connectToMyDatabase()
    cr = cn.cursor()
    cr.execute('Select * from classtb')
    print(cr.fetchall())
    cn.close()

def searchStudent(roll):

    cn = connectToMyDatabase()
    cr = cn.cursor()
    q = 'Select name from classtb where Roll = %s' % roll
    cr.execute(q)
    allResults = cr.fetchall()
    return allResults[0][0]

def insertData(roll, name):
    
    cn = connectToMyDatabase()
    cr = cn.cursor()
    #q = 'Insert into classtb (roll, name) values (' + roll +","+name+")"
    q = 'Insert into classtb (roll, name) values(%s, "%s")' % (roll, name)
    print(q)
    cr.execute(q)
    
    cn.commit() # ctrl + s
    cn.close()

