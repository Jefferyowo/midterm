#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
import codecs,sys
import cgi
import shoppingcart

print("Content-Type: text/html; charset=utf-8\n")
sys.stdout.flush()

data = shoppingcart.getList()
msg = ""
text = ""#儲存購物車裡面有哪些商品的pid
money = shoppingcart.checkSum()
for (pid,goodName, goodPrice, num) in data:
    msg = msg + f"<tr align='center'><td>{pid}</td><td>{goodName}</td><td>${goodPrice}</td> <td>{num}</td></tr>"
    text = text + f"<option>{pid}</option>"
msg += f"<p align='center' >The total price is ${money} dollars!</p>" #money = 購物車裡的總金額

with open("showCart.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"text",text.encode())
    st = st.replace(b"cart_msg",msg.encode())
sys.stdout.buffer.write(st)