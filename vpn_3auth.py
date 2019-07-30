import datetime                         #날짜
import time
from datetime import date
import smtplib                          #메일전송
from email.mime.text import MIMEText
import pymysql
import pickle

dt = datetime.datetime.now()
nowdate = dt.strftime('%Y-%m-%d')
threemonthsago = date.fromtimestamp(time.time() - 60 * 60 * 24 * 92)
threemonthsago_date = threemonthsago.strftime("%Y-%m-%d")
onemonthago = date.fromtimestamp(time.time() - 60 * 60 * 24 * 31)
onemonthago_date = onemonthago.strftime("%Y%m")

def save1():
    db = pymysql.connect(host = "localhost", user = "root", passwd = "secmon0802!", db = "jh_test")
    curs = db.cursor()

    # sql_select = "select * from vpn where %s = %s"
    sql_select = "select ad from vpn where auth_date < '%s'"
    curs.execute(sql_select % (threemonthsago_date))
    # curs.execute(sql_select % ("2019-04-08"))
    rows = curs.fetchall()
    rep = str(rows).replace("),",")\n").replace("((","(").replace(")))","))").replace(" ","").replace(",(",", (").replace(" (","\t(").replace(",","").replace("))",")").replace("(","").replace(")","").replace("'","")

    replist = rep.splitlines() #rep 리스트변환
    # print(replist)
    # test_list = ['andante','bae','pio02']
    # with open(("201904"),'wb') as fp :
    #     pickle.dump(test_list,fp)
    #list 월별 저장
    with open (dt.strftime("%Y%m"),'wb') as fp:
        pickle.dump(replist, fp)
    with open(dt.strftime("%Y%m"),'rb') as fp:
        a = pickle.load(fp)
    with open(onemonthago_date,'rb') as fp:
        b = pickle.load(fp)

    s = set(b)
    anne_list = [x for x in a if x not in s]
    print(anne_list)
    delete_list = [x for x in a if x in s]
    print(delete_list)

    sql_delete = "delete from jh_test.vpn where ad = '%s'"

    for i in delete_list :
        curs.execute(sql_delete % (i))
        db.commit()

    db.close()

    anne_add = str(anne_list)
    dele_add = str(delete_list)

    # SMTP body
    body = ("===  SSL VPN 3개월 이상 미접속자 AD (안내 대상)  ===\n\n") + anne_add + "\n\n\n===  SSL VPN 3개월 이상 미접속자 AD (삭제 대상)  ===\n" + dele_add

    # SMTP 메일 보내기
    HOST = 'tmcas.tmoncorp.com'
    mail_from = 'co_securityteam@tmon.co.kr'
    mail_to = 'pio02@tmon.co.kr,razor0227@tmon.co.kr'
              # 'razor0227@tmon.co.kr,kyumm306@tmon.co.kr'
    # mail_to = '@.com,@.com'

    msg = MIMEText(body, _charset='euc_kr')
    msg['Subject'] = 'sslvpn 3month authentication'
    msg['From'] = mail_from
    msg['to'] = mail_to

    s = smtplib.SMTP(HOST)
    s.sendmail(mail_from, mail_to.split(","), msg.as_string())
    s.quit()

save1()
