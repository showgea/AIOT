import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def dev_query_detail(dids):
    url_ = url + "/app/v1.0/lumi/dev/query/detail"
    params_ = {
        "dids": dids.split(",")
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求参数：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = dev_query_detail("virtual.69665604233767,lumi.158d0002c3ab98,lumi.158d0003930b2a")
    print(result_main.text)
