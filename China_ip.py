import requests
import ipaddress
import math

class GetChinaIp(object):
    def __init__(self, output_file):
        self.output_file = output_file
        self.url='http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
    
    #获取中国的ip段
    def get_cn_ip(self):
        #如果delegated-apnic-latest.txt文件不存在，则下载
        try:
            with open('delegated-apnic-latest.txt', 'r') as f:
                pass
        except:
            r = requests.get(self.url)
            with open('delegated-apnic-latest.txt', 'w') as f:
                f.write(r.text)
        #读取文件
        with open('delegated-apnic-latest.txt', 'r') as f:
            ip_list = []
            for i in f.readlines():
                if i.startswith('apnic|CN|ipv4'):
                    ip, count = i.split('|')[3:5]
                    #计算CIDR
                    net = ipaddress.ip_network(f'{ip}/{32-int(math.log(int(count), 2))}', strict=False)
                    ip_list.append(str(net))
        print('China:共获取到{}个ip段'.format(len(ip_list)))
        return ip_list

# #获取中国的ip段
# def get_cn_ip():
#     #如果delegated-apnic-latest.txt文件不存在，则下载
#     try:
#         with open('delegated-apnic-latest.txt', 'r') as f:
#             pass
#     except:
#         url = 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
#         r = requests.get(url)
#         with open('delegated-apnic-latest.txt', 'w') as f:
#             f.write(r.text)
#     #读取文件
#     with open('delegated-apnic-latest.txt', 'r') as f:
#         ip_list = []
#         for i in f.readlines():
#             if i.startswith('apnic|CN|ipv4'):
#                 ip, count = i.split('|')[3:5]
#                 #计算CIDR
#                 net = ipaddress.ip_network(f'{ip}/{32-int(math.log(int(count), 2))}', strict=False)
#                 ip_list.append(str(net))
#     return ip_list
# if __name__ == '__main__':
#     with open('China_ip.txt', 'w') as f:
#         for i in get_cn_ip():
#             f.write(i + '\n')
#     print('中国ip段已经写入China_ip.txt文件')



# import ipaddress
# import math
# if __name__ == '__main__':
#     data = 'apnic|CN|ipv4|1.0.2.0|512|20110414|allocated'
#     ip, count = data.split('|')[3:5]
#     net = ipaddress.ip_network(f'{ip}/{32-int(math.log(int(count), 2))}', strict=False)
#     print(f'网段范围：{net.network_address} - {net.broadcast_address}')
#     print(f'CIDR：{net.with_prefixlen}')







#     import ipaddress

# # 定义起始地址和末尾地址
# start = "116.52.0.0"
# end = "116.55.255.255"

# # 把起始地址和末尾地址转换成整数
# start_int = int(ipaddress.IPv4Address(start))
# end_int = int(ipaddress.IPv4Address(end))

# # 计算 IP 段包含的地址数量
# value = end_int - start_int + 1

# # 创建一个 IPv4 网络对象，用起始地址和地址数量作为参数
# network = ipaddress.IPv4Network((start, value), strict=False)

# # 打印出网络对象的 CIDR 表示法
# print(network)
# 输出结果是：

# 116.52.0.0/16



# import ipaddress

# # 定义起始地址和地址数量
# start = "116.52.0.0"
# value = 262144

# # 把起始地址转换成整数
# start_int = int(ipaddress.IPv4Address(start))

# # 计算末尾地址的整数值，即起始地址加上地址数量减一
# end_int = start_int + value - 1

# # 把末尾地址的整数值转换成 IPv4 地址对象
# end = ipaddress.IPv4Address(end_int)

# # 打印出末尾地址的字符串形式
# print(end)
# 输出结果是：

# 116.55.255.255