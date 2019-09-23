import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url
headers = {
            "Appid": "1f1615ba596299024d73efc6",
            "Sign": "",
            "Userid": "38715a6d7c0608f7.606065919364653057",
            "Token": "5882be9c0054904df30a06b0e79dabdf51e8",
            "Lang": "zh",
            "Content-Type": "application/json"
        }


def app_dev_bind_query(dids):
    url_ = url + "/app/v1.0/lumi/app/dev/bind/query"
    params_ = {
        "dids": "%s" % dids.split(",")
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    print("请求地址：%s，请求参数：%s" % (url_, params_))
    r = requests.get(url=url_, params=params_, headers=headers, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_dev_bind_query("lumi.158d0003930b2a,lumi.158d000317a108,lumi.158d000317a118")
    print(result_main.text)
