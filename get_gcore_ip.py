# 获取gcore_cdn的ip
import requests
import json
# 获取gcore_cdn的ip
def get_gcore_ip():
    url='https://api.gcore.com/cdn/public-ip-list'
    r=requests.get(url)
    ip_list=json.loads(r.text)
    ip_v4=ip_list['addresses']
    ip_v6=ip_list['addresses_v6']
    return ip_v4,ip_v6
#将ip写入文件
def write_ip(ip_v4,ip_v6):
    with open('gcore_ipv4.txt','w') as f:
        for ip in ip_v4:
            f.write(ip+'\n')
    with open('gcore_ipv6.txt','w') as f:
        for ip in ip_v6:
            f.write(ip+'\n')
if __name__ == '__main__':
    ip_v4,ip_v6=get_gcore_ip()
    write_ip(ip_v4,ip_v6)
    