import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_password_new(account, password, authCode):
    url_ = url + "/app/v1.0/lumi/user/password/new"
    json_ = {
        "account": account,
        "password": password,
        "authCode": authCode
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    # 123456 e10adc3949ba59abbe56e057f20f883e
    # 654321 c33367701511b4f6020ec61ded352059
    result_main = user_password_new("18682246872", "e10adc3949ba59abbe56e057f20f883e", "123456")
    print(result_main.text)
    # print("18682246872".replace("2", "3"))
