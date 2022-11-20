#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import shoppingcart
import goods

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>del</title>
</head>
<body>
""")
records = []
money,records = shoppingcart.buy()
goods.reduce(records)
print("總共是",money,"元")
print(f"結帳完成!")

print("<br><a href='showGood.py'>回到產品資訊</a>")
print("<br><a href='showCart.py'>回到購物車</a>")
print("</body></html>")

