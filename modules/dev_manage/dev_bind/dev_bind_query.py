import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def dev_bind_query(bindKey):
    url_ = url + "/app/v1.0/lumi/dev/bind/query"
    params_ = {
        "bindKey": bindKey
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    print("请求参数：%s" % params_)
    r = requests.get(url=url_, params=params_, proxies=proxies, verify=False, headers=header_Gary)
    return r


if __name__ == '__main__':
    result_main = dev_bind_query("lumiEPvHM1oii9Jx")
    print(result_main.text)
