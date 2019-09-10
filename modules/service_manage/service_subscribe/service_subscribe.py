import requests
from config import readcfg

header_Gary_sub = readcfg.header_Gary_subscribe
header_Jenny_subscribe = readcfg.header_Jenny_subscribe
url = readcfg.url


def service_subscribe(serviceIds):
    url_ = url + "/app/v1.0/lumi/service/subscribe"
    json_ = {
        "serviceIds": serviceIds.split(",")
    }

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary_sub, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = service_subscribe("S01615944318404558848,S01615944318404558848")
    print(result_main.text)
