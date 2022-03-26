import mysql.connector.pooling
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
    sql="INSERT INTO t_dept(deptno,dname,loc)VALUES(%s,%s,%s)"
    data=[[100,"PART A","BeiJing"],[110,"PART B","ShangHai"]]
    cursor.executemany(sql,data)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)