import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def relation_remark(account, remark):
    url_ = url + "/app/v1.0/lumi/user/relation/remark"
    json_ = {
        "account": account,
        "remark": remark
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = relation_remark("18682246872", "remark555")
    print(result_main.text)
