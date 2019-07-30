import pymysql                          #mysql python 연동
import re                               #정규화
import codecs                           #파일 인코딩
import datetime                         #날짜
import time
from datetime import date

#날짜
dt = datetime.datetime.now()
nowdate = dt.strftime('%Y-%m-%d')
# threemonthsago = date.fromtimestamp(time.time()-60*60*24*92)
yesterday = date.fromtimestamp(time.time() - 60*60*24)
yesterday_date = yesterday.strftime("%Y-%m-%d")

#vpn파일 불러오기
# openvpn = codecs.open("vpn_auth_2018-11-27",'r', encoding='utf8') #인코딩
openvpn = codecs.open("C:\\Users\\infosecu\\AppData\\Local\\visualsyslog\\vpn_auth_"+nowdate,'r', encoding='utf8')
vpn = openvpn.read()
openvpn.close()

#패턴 정규화
pattern = re.compile(r"([a-z,A-Z,0-9]{1,}[\\]?[.]?[_]?[a-z,A-Z,0-9]{1,}?[(])")
patternfind = pattern.findall(vpn)  #패턴 찾기
replece_vpn = str(patternfind).replace("(","").replace("'","").replace("[","").replace("]","") #문자열 정리
relist = replece_vpn.split() #재 리스트화

#중복제거
dic = {}
for list in relist :
    count = dic.get(list, 0)
    dic[list] = count + 1
dic_list = dic.keys()

#딕셔너리 키값 리스트화
key = str(dic_list)
rep = key.replace("dict_keys([","").replace("'","").replace(",","").replace("])","") #문자열 정리
relist2 = rep.split()
print(relist2)

#db연결
db = pymysql.connect(host = "localhost", user = "root", passwd = "secmon0802!", db = "jh_test")
curs = db.cursor()

#쿼리문
sql_insert = "insert into vpn(ad, auth_date) values ('%s', '%s')"
sql_update = "update vpn set auth_date = '%s' where ad = '%s'"

#insert 하고, 에러나면 update (예외처리)
for i in relist2 :
    try :
        curs.execute(sql_insert % (i, yesterday_date))
        db.commit()
    except :
        curs.execute(sql_update % (yesterday_date,i))
        db.commit()

db.close()