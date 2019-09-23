import requests
from config import readcfg

url = readcfg.url


def account_transfer_query(transferNo):
    url_ = url + "/app/v1.0/lumi/account/transfer/query"
    params_ = {
        "transferNo": transferNo
    }

    print("请求数据：%s" % params_)
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    r = requests.post(url=url_, json=params_, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = account_transfer_query("123")
    print(result_main.text)
