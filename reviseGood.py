#!C:\Users\admin\AppData\Local\Programs\Python\Python37-32\python.exe
import codecs,sys
import cgi
import goods

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

form = cgi.FieldStorage()
pid=form.getvalue('select_name2')
records = goods.getId(pid)


pid = str(pid)
allName = str(records[0][1])
allPrice = str(records[0][2])
allNum = str(records[0][3])


with open("reviseGood.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###pid###",pid.encode())
    st = st.replace(b"###name###",allName.encode())
    st = st.replace(b"###price###",allPrice.encode())
    st = st.replace(b"###number###",allNum.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()
