#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import goods


#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>revise</title>
</head>
<body>
""")

form = cgi.FieldStorage()
pid=form.getvalue('pid')

records = goods.getId(pid)

old_name = records[0][1]
old_price = records[0][2]
old_number = records[0][3]

allName=form.getvalue('allName')
allPrice=form.getvalue('allPrice')
allNum=form.getvalue('allNum')

#沒有輸入的話則維持原資訊
if allName == None:
    allName = old_name
if allPrice == None:
    allPrice = old_price
if allNum == None:
    allNum = old_number

goods.revise(pid,allName,allPrice,allNum)
print("商品已修改!")

print("<br><a href='manage.py'>回庫存清單</a>")
print("</body></html>")

