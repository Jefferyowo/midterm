#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
# 連線DB
from dbConfig import conn, cur
#找到所有有庫存的產品
def getList():
    #查詢
    sql="select pid, goodName,goodPrice, num from shoppingcart where num>0 ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

#將不要的產品刪掉
def delcart(pid):
    sql="update shoppingcart set num=0 where pid=%s;"
    cur.execute(sql,(pid,))
    conn.commit()
    return True

# 判斷貨品是否已在購物車 不在的話就要添加
def exist(pid):
    sql = "select pid,goodPrice from shoppingcart where pid = %s;"
    cur.execute(sql,(pid,))
    records = cur.fetchall()
    return records

def addcart(pid):
    #看購物車裡是不是已經有這項產品的pid
    if exist(pid) == []:
        sql = "select pid,allName,allPrice from alllist where pid = %s;"
        cur.execute(sql,(pid,))
        records = cur.fetchall()
        i = records[0][0] #pid
        name = records[0][1] # allName
        price = records[0][2] # allPrice
        sql2="insert into shoppingcart (pid,goodName,goodPrice,num) values (%s,%s,%s,1);"
        cur.execute(sql2,(i,name,price))
        conn.commit()
    # 有的話 數量+1
    else:
        sql="update shoppingcart set num=num+1 where pid=%s;"
        cur.execute(sql,(pid,))
        conn.commit()
    return True

#結帳
def buy():
    money = 0
    records = []
    sql = "select pid, goodName,goodPrice, num from shoppingcart where num>0;"
    cur.execute(sql)
    lists = cur.fetchall()
    for list in lists:
        tmp = []
        money = money + list[2] * list[3] #每樣商品:goodPrice*num
        tmp.append(list[0])
        tmp.append(list[3])
        records.append(tmp)
    sql2 = "Delete from shoppingcart;" #清空購物車
    cur.execute(sql2)
    conn.commit()
    return money,records

#用來看還沒結帳前，當前購物車的總金額
def checkSum():
    money = 0
    records = []
    sql = "select pid, goodName,goodPrice, num from shoppingcart where num>0;"
    cur.execute(sql)
    lists = cur.fetchall()
    for list in lists:
        tmp = []
        money = money + list[2] * list[3]
        tmp.append(list[0])
        tmp.append(list[3])
        records.append(tmp)
    conn.commit()
    return money

def check(price):
    if (price >= 1000) :
        return 1
    elif (price < 1000 and price >= 501) :
        return 2
    else:
        return 3