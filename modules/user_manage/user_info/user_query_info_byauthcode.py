import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def user_query_info_byauthcode(account, authCode):
    url_ = url + "/app/v1.0/lumi/user/query/info/byauthcode"
    json_ = {
        "account": account,
        "authCode": authCode
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_query_info_byauthcode("18682246872", "123456")
    print(result_main.text)
