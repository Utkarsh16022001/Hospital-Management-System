#!C:\Users\hp\AppData\Local\Programs\Python\Python38-32\python.exe
import pymysql as ms
import cgi
print("Content-Type:text/html")
print("")
con=ms.connect("localhost","root","","kvk_hospitals")
form=cgi.FieldStorage()
msg=""
s1=form.getvalue("t1")
s2=form.getvalue("t2")
ss=form.getvalue("b1")
ss1=""
ss2=""
if(ss=="REGISTER"):
    c=con.cursor()
    c.execute("Insert into user_data values(%s,%s)",(s1,s2))
    con.commit()
    msg="REGISTRATION SUCCESSFUL"
if(ss=="LOGIN"):
    c=con.cursor()
    c.execute("Select * from user_data where username=%s and password=%s",(s1,s2))
    row=c.fetchone()
    if(row):
        print("<script>open('first.py','_self')</script>")
    else:
        msg="First Register Yourself!!"

print("<html><style> body{ background-image:url('https://t3.ftcdn.net/jpg/03/55/60/70/360_F_355607062_zYMS8jaz4SfoykpWz5oViRVKL32IabTP.jpg');background-repeat:no-repeat;background-size:100%;</style>")
print("<body> <div class='container'><image src='https://www.fit2work.com.au/assets/img/avatars/LoginIconAppl.png' class='avatar'><div class='login-box'><div class='row'><div class='col-md-6 login-left'></div>")
print("<form method='post'>")
print("<table align='center'>")
print("<tr><td>USER NAME:</td><td><input type='text' value='{0}' name='t1' required></td></tr>".format(ss1))
print("<tr><td>PASSWORD:</td><td><input type='password' value='{0}' name='t2' required></td></tr>".format(ss2))
print("<tr><td></td><td><input type='submit' value='REGISTER' name='b1'><input type='submit' value='LOGIN' name='b1'></td></tr>")
print("<tr><td></td><td><font color='red'>{0}</font></td></tr>".format(msg))
print("</table></form><hr>")
print("</body></div></div></div></html>")
