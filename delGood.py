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
<title>del_cart</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
pid=form.getvalue('select_name')
if goods.delgoods(pid):
    print(f"{pid}號商品已刪除!")
else:
    print("delete failed!")
print("<br><a href='manage.py'>回庫存</a>")
print("</body></html>")

