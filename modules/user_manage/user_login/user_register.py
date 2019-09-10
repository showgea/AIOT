import requests
from config import readcfg

header = readcfg.header
url = readcfg.url


def user_register(account, password, authCode, nickName=None, gender=None, birthday=None, area=None):
    url_ = url + "/app/v1.0/lumi/user/register"
    json_ = {
        "account": account,
        "password": password,
        "authCode": authCode,
        "nickName": nickName,
        "gender": gender,
        "birthday": birthday,
        "area": area
    }
    list_ = ["account", "password", "authCode", "nickName", "gender", "birthday",  "area"]
    num = 0
    for i in (account, password, authCode, nickName, gender, birthday, area):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_register("18682246872", "123456", "123456", "nick", 0, "2018-01-01", "shenzhen")
    print(result_main.text)
