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
<title>add_cart</title>
</head>
<body>
""")
form = cgi.FieldStorage()
pid=form.getvalue('select_name')
shoppingcart.addcart(pid)
print("新增產品成功!")
print("<br><a href='showGood.py'>繼續購買</a>")
print("<br><a href='showCart.py'>查看購物車</a>")
print("</body></html>") 