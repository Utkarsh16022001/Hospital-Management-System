#!C:\Users\hp\AppData\Local\Programs\Python\Python38-32\python.exe
import pymysql as ms
import cgi
print("Content-Type:text/html")
print("")
con=ms.connect("localhost","root","","kvk_hospitals")
msg=""
form=cgi.FieldStorage()
s1=form.getvalue("t1")
ss=form.getvalue("b1")
ss1=""
if(s1=="care1683"):
    if(ss=="ADMIN"):
        print("<script>open('login.py','_self')</script>")
if(s1!="care1683"):
    if(ss=="ADMIN"):
        msg="WRONG PASSWORD!!!"
print("<html><style> body{ background-image:url('https://www.sdglobaltech.com/wp-content/uploads/2017/01/The-Must-Have-modules-of-a-Hospital-Management-System-1200x675.jpg');background-repeat:no-repeat;background-size:100%;</style>")
print("<body> <h1 style='text-align:center'> WELCOME TO KVK HOSPITAL <br><br><br><br>")
print("<form method='post'>")
print("<table align='center'>")
print("<tr><td>PASSWORD:</td><td><input type='password' value='{0}' name='t1' required></td></tr>".format(ss1))
print("<tr><td></td><td><input type='submit' value='ADMIN' name='b1'></td></tr>")
print("<tr><td></td><td><font color='red'>{0}</font></td></tr>".format(msg))
print("</table></form><hr>")
print("</body></div></div></div></html>")
