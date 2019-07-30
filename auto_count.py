import re

def count() :

    #파일 불러오기
    fw = "D:\\python\\auto_count\\internetFW.txt"
    f = open(fw,'r')
    sentence = f.read()
    f.close()

    #count 패턴 값 (전체 packet)
    pat = re.compile(r"\d?\d?\d?[,]?\d?\d?\d?[,]?\d?\d?\d?[,]\d\d\d") #ex)7,174,995
    patfind = pat.findall(sentence)
    total = "\n".join(patfind) #패킷 // 문자열로 저장
    replace = total.replace(",","") #문자열에서 , 표시를 제거
    lines1 = replace.splitlines() #줄별로 리스트화
    lines = [int(i) for i in lines1] #문자열을 다시 int형으로 형변환

    #+Packets
    line0 = patfind[0] + " Packets"
    line1 = patfind[1] + " Packets"
    line2 = patfind[2] + " Packets"
    line3 = patfind[3] + " Packets"
    line4 = patfind[4] + " Packets"
    line5 = patfind[5] + " Packets"
    line6 = patfind[6] + " Packets"
    line7 = patfind[7] + " Packets"
    line8 = patfind[8] + " Packets"
    line9 = patfind[9] + " Packets"

    #해외 패킷 합계 / 국내 패킷 합계
    oversea_total = lines[0] + lines[1] + lines[2]
    area_total = lines[3] + lines[4] + lines[5] + lines[6] + lines[7] + lines[8] + lines[9]

    #Packet ',' 붙히기
    oversea = (format(oversea_total, ","))
    area = (format(area_total, ","))

    # #Packet GB로 변환
    # oversea_GB = oversea_total * 0.0000005495
    # area_GB = area_total * 0.0000005495
    #                      * 0.0000008108
    #
    # #소수 2번째 자리까지 끊고 GB붙힘
    # oversea2 = "{0:.2f}".format(oversea_GB) + " GB"
    # area2 = "{0:.2f}".format(area_GB) + " GB"

    # #해외 접근 비율
    over_aceess = oversea_total / (oversea_total+area_total) * 100
    over_aceess2 = "{0:.1f}".format(over_aceess)

    # #해외/국내 GB body
    body = line0 + "\n" + line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 +  "\n" + line5 +  "\n" + line6 +  "\n" + line7 +  "\n" + line8 +  "\n" + line9 + "\n\n" + oversea + " Packets " + "\n" + area + " Packets" + "\n\n" + over_aceess2
    print(body)
    #result.txt 에 count 쓰기
    result = open('result.txt','w')
    result.write(body)
    result.close()

count()