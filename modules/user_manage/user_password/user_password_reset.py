import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_password_reset(password, newPassword):
    url_ = url + "/app/v1.0/lumi/user/password/reset"
    json_ = {
          "password": password,
          "newPassword": newPassword
    }
    r = requests.post(url=url_, json=json_, headers=header_Gary)
    if '"message":"密码错误"' in r.text:
        url_2 = url + "/app/v1.0/lumi/user/password/reset"
        json_2 = {
            "password": "c33367701511b4f6020ec61ded352059",
            "newPassword": "e10adc3949ba59abbe56e057f20f883e"
        }
        r = requests.post(url=url_2, json=json_2, headers=header_Gary)
        return r
    return r


def user_password_reset_wrong(password, newPassword):
    url_ = url + "/app/v1.0/lumi/user/password/reset"
    json_ = {
          "password": password,
          "newPassword": newPassword
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    # 123456 e10adc3949ba59abbe56e057f20f883e
    # 654321 c33367701511b4f6020ec61ded352059
    result_main = user_password_reset("e10adc3949ba59abbe56e057f20f883e", "e10adc3949ba59abbe56e057f20f883e")
    print(result_main.text)
