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
    return r


if __name__ == '__main__':
    # 123456 e10adc3949ba59abbe56e057f20f883e
    # 654321 c33367701511b4f6020ec61ded352059
    result_main = user_password_reset("e10adc3949ba59abbe56e057f20f883e", "e10adc3949ba59abbe56e057f20f883e")
    print(result_main.text)
