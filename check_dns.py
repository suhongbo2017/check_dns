# 检查反向代理是否正常。

import socket
import time
from datetime import datetime
'''
该代码用于检查 ip 与url是否已经反向代理解析，并生成日志保存。
'''

def check_server_dns(ip_address,url):
    try:
        hostname,a,b = socket.gethostbyaddr(ip_address)

        if hostname == url:
            return True ,f'解析地址为:{hostname},ip是:{b}'
        else:
            return False,f'解析地址为:{hostname},正确的地址为：{url}'
    except socket.herror as e:
        return False , f"Reverse DNS lookup failed: {e}"
ip = '61.142.37.222'
url = 'mail.sz-jhs.com'


while True:

    result,message = check_server_dns(ip_address=ip,url=url)
    check_time = datetime.now()
    log_filename = datetime.now().date().strftime('%Y-%m-%d') + '.log'
    # print(log_filename)
    with open(f'./{log_filename}','a',encoding='utf-8')as log:
        log.write(str(check_time) + ' - ')
        log.write(message + '\n')    
    time.sleep(60)

