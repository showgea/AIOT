import requests
from config import readcfg

url = readcfg.url


def account_auth(projectId):
    url_ = url + "/app/v1.0/lumi/account/auth"
    json_ = {
        "projectId": projectId
    }

    print("请求数据：%s" % json_)
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    r = requests.post(url=url_, json=json_, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = account_auth("123")
    print(result_main.text)
