#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import shoppingcart
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
#找到該商品的編號
data = cgi.FieldStorage()
pid=data.getvalue('select_name')
if shoppingcart.delcart(pid):
    print(f"{pid}號商品已刪除!")
else:
    print("delete failed!")
print("<br><a href='showGood.py'>繼續購買</a>")
print("<br><a href='showCart.py'>返回購物車</a>")
print("</body></html>")