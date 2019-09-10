import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_account_replace(password, oldAuthCode, account, newAuthCode, countryCode=None):
    url_ = url + "/app/v1.0/lumi/user/account/replace"
    json_ = {
        "password": password,
        "oldAuthCode": oldAuthCode,
        "countryCode": countryCode,
        "account": account,
        "newAuthCode": newAuthCode
    }
    list_ = ["password", "oldAuthCode", "countryCode", "account"]
    num = 0
    for i in (password, oldAuthCode, account, newAuthCode, countryCode):
        if "@" in account:
            json_ = {"password": password, "oldAuthCode": oldAuthCode, "account": account, "newAuthCode": newAuthCode}
        else:
            if i is None:
                json_.pop(list_[num])
        num += 1

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary)
    return r


if __name__ == '__main__':
    result_main = user_account_replace("18682246872", "123456")
    print(result_main.text)
