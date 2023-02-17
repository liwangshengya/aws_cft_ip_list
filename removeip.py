import ipaddress
from tqdm import tqdm
class RemoveIp(object):
    def __init__(self, aws_ip_file, china_ip_file, output_file):
        self.aws_ip_file = aws_ip_file
        self.china_ip_file = china_ip_file
        self.output_file = output_file
    #读取文件
    def read_file(self, file):
        with open(file) as f:
            data = f.read()
        data = data.split('\n')
        # 去除空行
        data = [i for i in data if i != '']
        return data
    #将ip段转换成ipaddress对象
    def ip_to_ipaddress(self, ip_list):
        ip = []
        for i in ip_list:
            ip.append(ipaddress.ip_network(i))
        return ip
    #判断aws_cft的ip段是否在中国ip段内
    def check_ip(self, aws_ip, china_ip):
        count = 0
        new_aws_ip = aws_ip.copy()
        for i in tqdm(aws_ip):
            for j in china_ip:
                if j.supernet_of(i):
                    count += 1
                    new_aws_ip.remove(i)
                    break
        print("共有{}个ip段在中国ip段内".format(count))
        return new_aws_ip
    #将aws_cft的ip段写入文件
    def write_file(self, aws_ip):
        with open(self.output_file, 'w') as f:
            for i in aws_ip:
                f.write(str(i) + '\n')
    #主函数
    def main(self):
        aws_ip = self.read_file(self.aws_ip_file)
        china_ip = self.read_file(self.china_ip_file)
        aws_ip = self.ip_to_ipaddress(aws_ip)
        china_ip = self.ip_to_ipaddress(china_ip)
        aws_ip = self.check_ip(aws_ip, china_ip)
        self.write_file(aws_ip)
