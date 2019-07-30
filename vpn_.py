import datetime
import time
from datetime import date
import re
import smtplib
from email.mime.text import MIMEText

# 시간정보
dt = datetime.datetime.now()
nowdate = dt.strftime('%Y-%m-%d')
yesterday = date.fromtimestamp(time.time() - 60*60*24)
year = yesterday.strftime("%Y")
month = yesterday.strftime("%m")
Yday = yesterday.strftime("%d")

def sendmail() :

    # log데이터 불러오기
    # log = "/var/log/tmon/10.1.96.7/" + year + month + "/10.1.96.7_" + day + ".log"
    log = "file.txt"
    f = open(log, 'r')
    sentence = f.read()
    f.close()
    # 아이디 패턴값
    pat = re.compile(r"(\w{1,}[(]?\w{1,}[(]\w{1,}[-]?\w{1,}?[)][)]?)")
    patfind = pat.findall(sentence)
    # 중복 제거 및 횟수
    dic = {}
    for list in patfind:
        count = dic.get(list, 0)
        dic[list] = count + 1
    dic_list = dic.keys()

    #print(dic)

    # fail 합계
    total = 0
    for words in dic.values():
        total += words

    # ','로 줄구분 및 정리
    replace = str(dic).replace("," , "\n").replace("'" , " ").replace("{", " ").replace("}", " ").replace(":", ": \t")
    print(replace)
    lalist = replace.splitlines()
    lalist.sort(key = lambda s : len(s)) #글자 길이별 정렬
    stringlalist = "\n".join(lalist) #리스트 문자열 변환

    # SMTP body
    body = ("===== " + year + "-" + month + "-" + Yday+ " SSLVPN fail report =====\n") + ("\t\tID \t    "+"  count\n\n") + stringlalist +("\n\n\ttotal \t: \t") + str(total)
    # print(body)

    # SMTP 메일 보내기
    #HOST = 'tmcas.tmoncorp.com'
    #mail_from = 'sslvpn_fail@tmon.co.kr'
    #mail_to = 'pio02@tmon.co.kr'
    # mail_to = '@.com,@.com'

    #msg = MIMEText(body, _charset='euc_kr')
    #msg['Subject'] = 'sslvpn today report'
    #msg['From'] = mail_from
    #msg['to'] = mail_to

    #s = smtplib.SMTP(HOST)
    #s.sendmail(mail_from, mail_to.split(","), msg.as_string())
    #s.quit()

sendmail()
