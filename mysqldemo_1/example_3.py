import  mysql.connector
try:
    con=mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="mysql",
        database="test"
    )
    con.start_transaction()
    cursor=con.cursor()
    sql="INSERT INTO t_emp(empno,ename,job,mgr,hiredate,sal,comm,deptno)"\
         "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(9600,"lilbox","SALESMAN",None,"1985-9-1",2500,None,10))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()