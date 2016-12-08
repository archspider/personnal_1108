import MySQLdb

def conn_mysql():
    conn = MySQLdb.connect(host='10.49.15.218', user = 'archer', passwd='archer',db='dc_ploan', port = 3306)
    cur = conn.cursor()
    sql_tt1 = "SELECT * FROM usersid_test"
    sql_tt2 = "SELECT * FROM bank_detail_test"
    sql_tn2 = "SELECT * FROM bank_detail_train"
    sql_tt3 = "SELECT * FROM browse_history_test"
    cur.execute(sql_tt1)
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data

if __name__ == '__main__':
    data = conn_mysql()
    print (data)
    
