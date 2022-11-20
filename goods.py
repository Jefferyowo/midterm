#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
# 連線DB
from dbConfig import conn, cur
#找所有還有庫存的產品
def getList():
    #查詢
    sql="select pid, allName,allPrice, allNum from alllist where allNum>0 order by allPrice desc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

#把該個產品全部資料刪掉
def delgoods(pid):
    sql="delete from alllist where pid=%s;"
    cur.execute(sql,(pid,))
    conn.commit()
    return True

#新增產品資訊
def addgoods(name,price,allNum):
    sql="insert into alllist (allName,allPrice,allNum) values (%s,%s,%s);"
    cur.execute(sql,(name,price,allNum))
    conn.commit()
    return True

def getId(pid):
    sql="select pid, allName,allPrice, allNum from alllist where pid = %s"
    cur.execute(sql,(pid,))
    records = cur.fetchall()
    return records

#修改商品資訊
def revise(pid,name,price,number):
    sql = "update alllist set allName=%s,allPrice=%s,allNum=%s where pid=%s;"
    cur.execute(sql,(name,price,number,pid))
    conn.commit()
    return True

# 結帳後庫存減少
def reduce(records):
    for record in records:
        sql = "update alllist set allNum= allNum - %s where pid = %s;"
        cur.execute(sql,(record[1],record[0]))
        conn.commit()