import requests
import json
from config import readcfg

header = readcfg.header
url = readcfg.url


def user_check_isreg(account):
    url_ = url + "/app/v1.0/lumi/user/check/isreg"
    json_ = {
        "account": account
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_check_isreg("18682246872")
    s = json.loads(result_main.text)["result"]["isreg"]
    print(s)
