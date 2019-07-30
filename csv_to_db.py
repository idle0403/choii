import csv
import pymysql

csv_to_db_list = ['application_app', 'application_web', 'dbms_db2', 'dbms_mariadb', 'dbms_mssql', 'dbms_mysql', 'dbms_oracle', 'dbms_postgres', 'dbms_sybaseiq', 'device', 'middleware_apache', 'middleware_iis', 'middleware_jetty', 'middleware_jrun', 'middleware_nginx', 'middleware_tomcat', 'middleware_websphere', 'network_wire', 'network_wireless', 'security_system', 'server_linux', 'server_windows']

def application_app():
    # csv파일 경로 지정
    f = open('D:\\csv_to_db\\risk_plan\\'+'application_app.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    # 각 테이블 별로 query를 통하여 DB 적재
    sql_insert = "insert into "+"application_app"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"application_app "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[0] + " : success")

def application_web():
    f = open('D:\\csv_to_db\\risk_plan\\'+'application_web.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"application_web"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"application_web "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[1] + " : success")

def dbms_db2():
    f = open('D:\\csv_to_db\\risk_plan\\'+'dbms_db2.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"dbms_db2"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"dbms_db2 "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[2] + " : success")

def dbms_mariadb():
    f = open('D:\\csv_to_db\\risk_plan\\'+'dbms_mariadb.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"dbms_mariadb"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"dbms_mariadb "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[3] + " : success")

def dbms_mssql():
    f = open('D:\\csv_to_db\\risk_plan\\'+'dbms_mssql.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into dbms_mssql(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update dbms_mssql set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0, len(csv_list)):
        for j in range(0, 13):
            csv_list[i][j] = (csv_list[i][j]).replace("'", "")
        try:
            curs.execute(sql_insert % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()
        except:
            curs.execute(sql_update % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()
    f.close()
    db.close()
    print(csv_to_db_list[4] + " : success")

def dbms_mysql():
    f = open('D:\\csv_to_db\\risk_plan\\'+'dbms_mysql.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"dbms_mysql"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"dbms_mysql "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[5] + " : success")

def dbms_oracle():
    f = open('D:\\csv_to_db\\risk_plan\\'+'dbms_oracle.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"dbms_oracle"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"dbms_oracle "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[6] + " : success")

def dbms_postgres():
    f = open('D:\\csv_to_db\\risk_plan\\'+'dbms_postgres.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"dbms_postgres"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"dbms_postgres"+" set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[7] + " : success")

def dbms_sybaseiq():
    f = open('D:\\csv_to_db\\risk_plan\\'+'dbms_sybaseiq.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"dbms_sybaseiq"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"dbms_sybaseiq "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[8] + " : success")

def device():
    f = open('D:\\csv_to_db\\risk_plan\\'+'device.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into device(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update device set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0, len(csv_list)):
        for j in range(0, 13):
            csv_list[i][j] = (csv_list[i][j]).replace("'", "")
        try:
            curs.execute(sql_insert % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()
        except:
            curs.execute(sql_update % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[9] + " : success")

def middleware_apache():
    f = open('D:\\csv_to_db\\risk_plan\\'+'middleware_apache.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"middleware_apache"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"middleware_apache "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[10] + " : success")

def middleware_iis():
    f = open('D:\\csv_to_db\\risk_plan\\'+'middleware_iis.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into middleware_iis(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update middleware_iis set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[11] + " : success")

def middleware_jetty():
    f = open('D:\\csv_to_db\\risk_plan\\' + 'middleware_jetty.csv', 'r', encoding='ANSI')

    rdr = csv.reader(f)
    csv_list = []

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host="10.1.2.59", user="root", passwd="secmon0802!", db="csv")
    curs = db.cursor()

    sql_insert = "insert into middleware_jetty(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update middleware_jetty set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0, len(csv_list)):
        for j in range(0, 13):
            csv_list[i][j] = (csv_list[i][j]).replace("'", "")
        try:
            curs.execute(sql_insert % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()
        except:
            curs.execute(sql_update % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[12] + " : success")

def middleware_jrun():
    f = open('D:\\csv_to_db\\risk_plan\\'+'middleware_jrun.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"middleware_jrun"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"middleware_jrun "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[13] + " : success")

def middleware_nginx():
    f = open('D:\\csv_to_db\\risk_plan\\'+'middleware_nginx.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"middleware_nginx"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"middleware_nginx "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[14] + " : success")

def middleware_tomcat():
    f = open('D:\\csv_to_db\\risk_plan\\'+'middleware_tomcat.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"middleware_tomcat"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"middleware_tomcat "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[15] + " : success")

def middleware_websphere():
    f = open('D:\\csv_to_db\\risk_plan\\'+'middleware_websphere.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"middleware_websphere"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"middleware_websphere "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[16] + " : success")

def network_wire():
    f = open('D:\\csv_to_db\\risk_plan\\'+'network_wire.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"network_wire"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"network_wire "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[17] + " : success")

def network_wireless():
    f = open('D:\\csv_to_db\\risk_plan\\'+'network_wireless.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"network_wireless"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"network_wireless "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[18] + " : success")

def security_system():
    f = open('D:\\csv_to_db\\risk_plan\\'+'security_system.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into "+"security_system"+"(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update "+"security_system "+"set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0,len(csv_list)):
         for j in range(0,13):
            csv_list[i][j] = (csv_list[i][j]).replace("'","")
            try :
                curs.execute(sql_insert % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()
            except :
                curs.execute(sql_update % ((csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]), (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]), (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0]+csv_list[i][3]))
                db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[19] + " : success")

def server_linux():
    f = open('D:\\csv_to_db\\risk_plan\\'+'server_linux.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()
    sql_insert = "insert into server_linux(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update server_linux set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0, len(csv_list)):
        for j in range(0, 13):
            csv_list[i][j] = (csv_list[i][j]).replace("'", "")

        try:
            curs.execute(sql_insert % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()
        except:
            curs.execute(sql_update % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[20] + " : success")

def server_windows():
    f = open('D:\\csv_to_db\\risk_plan\\'+'server_windows.csv', 'r', encoding='ANSI')

    csv_list = []
    rdr = csv.reader(f)

    for line in rdr:
        csv_list.append(line)

    csv_list = csv_list[4:]

    db = pymysql.connect(host = "10.1.2.59", user = "root", passwd = "secmon0802!", db = "csv")
    curs = db.cursor()

    sql_insert = "insert into server_windows(device_code, device_name, division, code, subject, importance, test_result, status, measures, action_date, department, manager, action_result, remarks, decode_pk) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    sql_update = "update server_windows set device_code = '%s', device_name = '%s', division = '%s', code = '%s', subject = '%s', importance = '%s', test_result = '%s', status = '%s', measures = '%s', action_date = '%s', department = '%s', manager = '%s', action_result = '%s', remarks = '%s' where decode_pk ='%s'"

    for i in range(0, len(csv_list)):
        for j in range(0, 13):
            csv_list[i][j] = (csv_list[i][j]).replace("'", "")
        try:
            curs.execute(sql_insert % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()
        except:
            curs.execute(sql_update % (
            (csv_list[i][0]), (csv_list[i][1]), (csv_list[i][2]), (csv_list[i][3]), (csv_list[i][4]), (csv_list[i][5]),
            (csv_list[i][6]), (csv_list[i][7]), (csv_list[i][8]), (csv_list[i][9]), (csv_list[i][10]),
            (csv_list[i][11]), (csv_list[i][12]), (csv_list[i][13]), csv_list[i][0] + csv_list[i][3]))
            db.commit()

    f.close()
    db.close()
    print(csv_to_db_list[21] + " : success")

#csv to db
application_app()
application_web()
dbms_db2()
dbms_mariadb()
dbms_mssql()
dbms_mysql()
dbms_oracle()
dbms_postgres()
dbms_sybaseiq()
device()
middleware_apache()
middleware_iis()
middleware_jetty()
middleware_jrun()
middleware_nginx()
middleware_tomcat()
middleware_websphere()
network_wire()
network_wireless()
security_system()
server_linux()
server_windows()