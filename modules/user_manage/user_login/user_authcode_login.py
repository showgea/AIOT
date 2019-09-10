import requests
from config import readcfg

header = readcfg.header
url = readcfg.url


def user_authcode_login(account, authCode, isClearRedis):
    url_ = url + "/app/v1.0/lumi/user/authcode/login"
    json_ = {
        "account": account,
        "authCode": authCode,
        "isClearRedis": isClearRedis
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_authcode_login("18682246872", "123456", "true")
    print(result_main.text)
