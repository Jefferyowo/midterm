#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import goods
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>add_goods</title>
</head>
<body>
""")
#取商品的資料
form = cgi.FieldStorage()
allName=form.getvalue('allName')
allPrice=form.getvalue('allPrice')
allNum=form.getvalue('allNum')
#新增商品到庫存
goods.addgoods(allName,allPrice,allNum)
print("商品已加入!")
print("<br><a href='manage.py'>回庫存清單</a>")
print("</body></html>")

