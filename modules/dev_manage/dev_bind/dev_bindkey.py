import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def dev_bindkey(positionId):
    url_ = url + "/app/v1.0/lumi/dev/bindkey"
    json_ = {
        "positionId": positionId
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    print("请求参数：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = dev_bindkey("real1.615940701625851904")
    print(result_main.text)
