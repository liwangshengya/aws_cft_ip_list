import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'}
proxy = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}
#获取aws cft ip
def get_awscft_ip():
    url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
    r = requests.get(url, headers=headers,proxies=proxy)
    ip_list = []
    for i in r.json()['prefixes']:
        if i['service'] == 'CLOUDFRONT':
            ip_list.append(i['ip_prefix'])
    return ip_list
#检测每个ip端所属的国家
#去掉所属国家为CN的ip
#使用ipapi.co的api
def check_ip(ip_list):
    for i in ip_list:
        #取出ip段的第一个ip
        i_first = i.split('/')[0]
        #拼接url
        #url='https://ipapi.co/'+i+'/json/
        url = 'https://ipapi.co/' + i_first + '/json'
        r = requests.get(url, headers=headers, proxies=proxy)
        #判断是否为CN(country_code)
        if r.json()['country_code'] == 'CN':
            print(i,'   该ip为CN,需要删除')
            ip_list.remove(i)

    return ip_list
    
if __name__ == '__main__':
    ip_list = get_awscft_ip()
    print(ip_list)
    print(len(ip_list))
    #写入文件，每行一个ip
    with open('awscft_ip.txt', 'w') as f:
        for ip in ip_list:
            f.write(ip + '\n')
    #检测ip所属国家
    ip_list = check_ip(ip_list)
    print(ip_list)
    print(len(ip_list))
    #写入不是CN的ip
    with open('awscft_ip_not_cn.txt', 'w') as f:
        for ip in ip_list:
            f.write(ip + '\n')
            
    