import  mysql.connector.pooling
config={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"mysql",
    "database":"test"
}
try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con=pool.get_connection()
    con.start_transaction()
    cursor=con.cursor()
    sql="DROP TABLE t_emp_new"
    cursor.execute(sql)
    sql="CREATE TABLE t_emp_new LIKE t_emp"#like 抓取表结构
    cursor.execute(sql)
    sql="SELECT AVG(sal) AS avg FROM t_emp"
    cursor.execute(sql)
    temp=cursor.fetchone()#当sql语句运行后只有一个结果，要用fetchone函数
    avg=temp[0]#公司平均底薪
    sql="SELECT deptno FROM t_emp GROUP BY deptno HAVING AVG(sal)>=%s"
    cursor.execute(sql,[avg])#当sql语句运行后有多个结果时，可以用循环，也可以用fetchall
    # for one in cursor:
    #     print(one[0])
    temp=cursor.fetchall()
    # print(temp)
    sql="INSERT INTO t_emp_new SELECT * FROM  t_emp WHERE deptno IN ("
    for index in range(len(temp)):
        one=temp[index][0]
        if index<len(temp)-1:#因为in语句的语法是（20，10），元素与元素之间会有逗号
            sql+=str(one)+","
        else:
             sql+=str(one)
    sql+=")"
    # print(sql)  INSERT INTO t_emp_new SELECT * FROM  t_emp WHERE deptno IN (20,10)
    cursor.execute(sql)
    sql="DELETE FROM t_emp WHERE deptno IN ("
    for index in range(len(temp)):
        one=temp[index][0]
        if index<len(temp)-1:
            sql+=str(one)+","
        else:
            sql+=str(one)
    sql+=")"
    cursor.execute(sql)
    sql="SELECT deptno FROM t_dept WHERE dname =%s"
    cursor.execute(sql,["SALES"])#是中括号 不是小括号
    deptno=cursor.fetchone()[0]
    sql="UPDATE t_emp_new SET deptno=%s"
    cursor.execute(sql, [deptno])
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)