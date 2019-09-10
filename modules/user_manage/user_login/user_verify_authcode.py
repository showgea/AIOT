import requests
from config import readcfg

header = readcfg.header
url = readcfg.url


def user_verify_authcode(account, authCode, isClearRedis, countryCode=None, authCodeType=None):

    url_ = url + "/app/v1.0/lumi/user/verify/authcode"
    json_ = {
        "account": account,
        "authCode": authCode,
        "isClearRedis": isClearRedis,
        "countryCode": countryCode,
        "authCodeType": authCodeType
    }
    list_ = ["account", "authCode", "isClearRedis", "countryCode", "authCodeType"]
    num = 0
    for i in (account, authCode, isClearRedis, countryCode, authCodeType):
        if "@" in account:
            json_ = {"account": account,"authCode": authCode,"isClearRedis": isClearRedis, "authCodeType": authCodeType}
        else:
            if i is None:
                json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_verify_authcode("18682246872", "123456", "1", "+86", 1)
    print(result_main.text)
