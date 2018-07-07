
__author__ = "Taeyoung Her(herty0826@naver.com)"
__version__ = "1.0.0"

import pyping
import sys
import threading
import os

def checkDesktop(hostname):
    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
      print hostname, 'is up!'
    else:
      print hostname, 'is down!'

def ipcheck(ip):
    result = False
    # ip를 .을 기준으로 나누고 ipC에 담음
    ipC= ip.split('.')

    if len(ipC) == 4:
        try:
            int(''.join(ipC))
            count = 0
            for x in ipC:
                if int(x) >-1 and int(x) <256:
                    count = count + 1
            if count == 4:
                result = True
                    
        except:
            pass
    else:
        pass

    return result


def main(ip1,ip2):
    # ip1, ip2를 입력받고 이 두개 ip의 유효성 체크를 한다.
    if ipcheck(ip1) == True and ipcheck(ip2) == True:
        # ip1 , ip2를 .을 기준으로 나눠서 각각 변수에 담음
        m = ip1.split('.')
        n = ip2.split('.')
        th_list = []
        print int(n[3])-int(m[3])+2
        # 두 ip주소의 앞 3자리가 같은지, 4번째 값의 대소가 올바른지 확인
        if '.'.join(m[:3]) == '.'.join(n[:3]) and int(m[3]) <= int(n[3]):
            # ip의 범위만큼 for문을 돌린다. 
            for x in range(int(m[3]),int(n[3])+1):
                # 범위내의 ip주소지정
                b = m[0] + '.' + m[1] + '.' + m[2] + '.' + str(x)
                #k = checkDesktop(b)


                #thread객체 생성 
                t = threading.Thread(target=checkDesktop, args=(b))
                # thread 시작 
                t.start()

                #리스트에 객체를 집어넣음 
                th_list.append(t)


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
