#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
import codecs,sys
import cgi
import goods
import shoppingcart

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

text="" #儲存現有產品的pid
data = goods.getList()
msg = ""
#把所有商品顯示出來
for (pid,allName, allPrice, allNum) in data:
    if (shoppingcart.check(allPrice) == 1):
        msg = msg + f"<tr style='background-color:red' align='center'><td>{pid}</td><td>{allName}</td><td>${allPrice}</td><td>{allNum}個</td></tr>"
    if (shoppingcart.check(allPrice) == 2):
        msg = msg + f"<tr style='background-color:blue' align='center'><td>{pid}</td><td>{allName}</td><td>${allPrice}</td><td>{allNum}個</td></tr>"
    if (shoppingcart.check(allPrice) == 3):
        msg = msg + f"<tr style='background-color:green' align='center'><td>{pid}</td><td>{allName}</td><td>${allPrice}</td><td>{allNum}個</td></tr>"
    text = text + f"<option>{pid}</option>"


with open("showGood.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"text",text.encode())
    st = st.replace(b"msg",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()