import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_bind(account, authCode, countryCode=None):
    url_ = url + "/app/v1.0/lumi/user/bind"
    json_ = {
        "account": account,
        "authCode": authCode,
        "countryCode": countryCode
    }
    list_ = ["account", "authCode", "countryCode"]
    num = 0
    for i in (account, authCode, countryCode):
        if "@" in account:
            json_ = {"account": account, "authCode": authCode}
        else:
            if i is None:
                json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_bind("18682246872", "123456")
    print(result_main.text)
