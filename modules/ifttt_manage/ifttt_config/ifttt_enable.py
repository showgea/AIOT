import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_enable(linkageId, enable):
    url_ = url + "/app/v1.0/lumi/ifttt/enable"
    json_ = {
        "linkageId": linkageId,
        "enable": enable
        }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_enable("L.619498025691082752", "1")
    print(result_main.text)
