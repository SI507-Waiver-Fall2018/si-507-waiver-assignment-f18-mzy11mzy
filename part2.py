#name: Zhiyi Ma
#unique name: zhiyima
#umid: 48014433

import sys
import sqlite3

#conn = sqlite3.connect("/Users/mazhiyi/Documents/GitHub/si-507-waiver-assignment-f18-mzy11mzy/Northwind_small.sqlite")
conn = sqlite3.connect("Northwind_small.sqlite")
c = conn.cursor()

#  python3 part2.py customers
if sys.argv[1] == "customers":
	c.execute("SELECT Id, CompanyName FROM Customer")
	print("ID \t Customer Name")
	for a,b in c.fetchall():
		print(a + "\t" + b)
	c.close()
	conn.close()

#  python3 part2.py employees
if sys.argv[1] == "employees":
	c.execute("SELECT ID, FirstName, LastName FROM Employee")
	print("ID \t Employee Name")
	for a,b,c in c.fetchall():
		print(str(a) + "\t" + b + " " + c)

#  python3 part2.py orders cust=<customer id>
if sys.argv[1] == "orders" and sys.argv[2][:5] == "cust=":
	content = sys.argv[2][5:]
	c.execute("SELECT OrderDate FROM 'Order' WHERE CustomerID = ?", [content])
	print("Order dates")
	for a in c.fetchall():
		print(a[0])
	c.close()
	conn.close()

#  python3 part2.py orders emp=<employee last name>
if sys.argv[1] == "orders" and sys.argv[2][:4] == "emp=":
	name = sys.argv[2][4:]
	c.execute("SELECT OrderDate FROM 'Order' WHERE EmployeeID = (SELECT Id from Employee WHERE LastName = ?)", [name])
	print("Order dates")
	for a in c.fetchall():
		print(a[0])
	c.close()
	conn.close()