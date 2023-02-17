import requests
import json
import time
from China_ip import GetChinaIp
from removeip import RemoveIp

class GetAwsCftIp(object):
    def __init__(self,output_file,is_proxy=False,ip_type='ipv4'):
        self.output_file = output_file
        self.hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'}
        self.is_proxy = is_proxy
        if self.is_proxy:
            self.proxy=proxy = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}
        else:
            self.proxy = {}
        self.url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
        self.ip_type = ip_type #ipv4 or ipv6
        self.ip_list = []
        self.china_ip = GetChinaIp('China_ip.txt').get_cn_ip()
    
    # 获取aws cft ip
    def get_awscft_ip(self):
        r=requests.get(self.url,headers=self.hearders,proxies=self.proxy)
        ip_list = []
        if self.ip_type == 'ipv4':
            for i in r.json()['prefixes']:
                if i['service'] == 'CLOUDFRONT':
                    ip_list.append(i['ip_prefix'])
        elif self.ip_type == 'ipv6':
            for i in r.json()['ipv6_prefixes']:
                if i['service'] == 'CLOUDFRONT':
                    ip_list.append(i['ipv6_prefix'])
        print('awscft:共获取到{}个IP段'.format(len(ip_list)))
        return ip_list
    # 将aws cft ip写入文件
    def write_file(self):
        with open(self.output_file, 'w') as f:
            for i in self.ip_list:
                f.write(str(i) + '\n')
    # 主函数
    def main(self):
        self.ip_list = self.get_awscft_ip()
        self.Removeip=RemoveIp('aws_cft_ip.txt','China_ip.txt','aws_cft_ip.txt')
        aws_ip = self.Removeip.ip_to_ipaddress(self.ip_list)
        china_ip = self.Removeip.ip_to_ipaddress(self.china_ip)
        self.ip_list = self.Removeip.check_ip(aws_ip, china_ip)
        self.write_file()

if __name__ == '__main__':
    start_time = time.time()
    GetAwsCftIp('aws_cft_ip.txt').main()
    print('ip以写入到aws_cft_ip.txt文件中')
    end_time = time.time()
    print('运行时间：',end_time - start_time)


# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'}
# need_proxy = False
# if need_proxy:
#     proxy = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}
# else:
#     proxy = {}
# #获取aws cft ip
# def get_awscft_ip():
#     url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
#     r = requests.get(url, headers=headers,proxies=proxy)
#     ip_list = []
#     for i in r.json()['prefixes']:
#         if i['service'] == 'CLOUDFRONT':
#             ip_list.append(i['ip_prefix'])
#     return ip_list


