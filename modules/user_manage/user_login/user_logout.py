import requests
from config import readcfg

header = readcfg.header
url = readcfg.url


def user_logout():
    url_ = url + "/app/v1.0/lumi/user/logout"
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    r = requests.post(url=url_, headers=header, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_logout()
    print(result_main.text)
