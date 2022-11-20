#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
import codecs,sys
import cgi
import goods
from dbConfig import conn, cur

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

sql="select pid, allName,allPrice, allNum from alllist order by pid asc;"
cur.execute(sql)
goodsList = records = cur.fetchall()
text = ""#儲存現有庫存產品
msg = ""
for (pid,allName, allPrice, allNum) in goodsList:
    msg = msg + f"<tr align='center'><td>{pid}</td><td>{allName}</td><td>${allPrice}</td><td>{allNum}個</td></tr>"
    text = text + f"<option>{pid}</option>"

with open("manage.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"text",text.encode())
    st = st.replace(b"text2",text.encode())
    st = st.replace(b"msg",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()