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
s3=form.getvalue("t3")
s4=form.getvalue("t4")
s5=form.getvalue("t5")
s6=form.getvalue("t6")
s7=form.getvalue("t7")
ss=form.getvalue("b1")
ss1=""
ss2=""
ss3=""
ss4=""
ss5=""
ss6=""
ss7=""
if(ss=="Save"):
	c=con.cursor()
	c.execute("Insert into doctor_details values(%s,%s,%s,%s,%s,%s,%s)",(s1,s2,s3,s4,s5,s6,s7))
	con.commit()
	msg="Data Saved Successfully"
if(ss=="Update"):
	c=con.cursor()
	c.execute("Update doctor_details set age=%s,address=%s,contact=%s,fees=%s,monthly_salary=%s where name=%s",(s3,s4,s5,s6,s7,s1))
	con.commit()
	msg="Data Updated Successfully"
if(ss=="Delete"):
	c=con.cursor()
	c.execute("Delete from doctor_details where name=%s",(s1))
	con.commit()
	msg="Data Deleted Successfully"
if(ss=="Search"):
	c=con.cursor()
	c.execute("Select * from doctor_details where name=%s",(s1))
	row=c.fetchone()
	if(row):
		ss1=row[0]
		ss2=row[1]
		ss3=row[2]
		ss4=row[3]
		ss5=row[4]
		ss6=row[5]
		ss7=row[6]
		msg="Data Found!!"
	else:
		msg="Data NOT Found!!!"
print("<html><style> body{ background-image:url('https://resources.stuff.co.nz/content/dam/images/1/k/o/y/l/n/image.related.StuffLandscapeSixteenByNine.620x349.1knujj.png/1501212139432.jpg');background-repeat:no-repeat;background-size:100%;</style>")
print("<body> <h1 style='text-align:center'> KVK HOSPITALS     Doctor Details<br><br><br><br>")
print("<table border='0' width='100%'><tr><td><a href='d4.py'>Doctor Details</a></td><td><a href='n1.py'>Nurse Details</a></td><td><a href='other_workers.py'>Workers Details</a></td><td><a href='patient.py'>Patient Details</a></td><td><a href='dpatients.py'>Discharge Patient Details</a></td><td><a href='ADMIN.py'>Logout</a></td></tr></table><hr>")
print("<form method='post'>")
print("<table align='center'>")

print("<tr><td>DOCTOR NAME:</td><td><input type='text' value='{0}' name='t1' required></td></tr>".format(ss1))
print("<tr><td>Specialisation:</td><td><input type='text' value='{0}'  name='t2'></td></tr>".format(ss2))
print("<tr><td>AGE:</td><td><input type='text' value='{0}'  name='t3'></td></tr>".format(ss3))
print("<tr><td>Address:</td><td><input type='text' value='{0}'  name='t4'></td></tr>".format(ss4))
print("<tr><td>Contact:</td><td><input type='text' value='{0}'  name='t5'></td></tr>".format(ss5))
print("<tr><td>FEES:</td><td><input type='text' value='{0}'  name='t6'></td></tr>".format(ss6))
print("<tr><td>Monthly Salary:</td><td><input type='text' value='{0}'  name='t7'></td></tr>".format(ss7))
print("<tr><td></td><td><input type='submit' value='Save' name='b1'><input type='submit' value='Search' name='b1'></td></tr>")
print("<tr><td></td><td><input type='submit' value='Update' name='b1'><input type='submit' value='Delete' name='b1'></td></tr>")
print("<tr><td></td><td><font color='red'>{0}</font></td></tr>".format(msg))
print("</table></form><hr>")
c=con.cursor()
c.execute("Select * from doctor_details")
rows=c.fetchall()
print("<table border='1 px solid black' border-spacing:5 px align='center'>")
print("<tr><td>Doctor Name</td><td>Specialisation</td><td>Age</td><td>Address</td><td>Mobile</td><td>Fees</td><td>Monthly Salary</td></tr>")
for i in range(len(rows)):
	print("<tr>")
	print("<td>{0}</td>".format(rows[i][0]))
	print("<td>{0}</td>".format(rows[i][1]))
	print("<td>{0}</td>".format(rows[i][2]))
	print("<td>{0}</td>".format(rows[i][3]))
	print("<td>{0}</td>".format(rows[i][4]))
	print("<td>{0}</td>".format(rows[i][5]))
	print("<td>{0}</td>".format(rows[i][6]))
	print("</tr>")
print("</table>")
print("</body></html>")
