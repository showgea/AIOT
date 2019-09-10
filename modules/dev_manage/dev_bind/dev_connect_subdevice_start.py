import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def dev_connect_subdevice_start(did, effectTime=None, installCode=None):
    url_ = url + "/app/v1.0/lumi/dev/connect/subdevice/start"
    json_ = {
        "did": did,
        "effectTime": effectTime,
        "installCode": installCode
    }
    list_ = ["did", "effectTime", "installCode"]
    num = 0
    for i in (did, effectTime, installCode):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    print("请求参数：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = dev_connect_subdevice_start("lumi.158d0003930b2a", effectTime=None, installCode=None)
    print(result_main.text)
