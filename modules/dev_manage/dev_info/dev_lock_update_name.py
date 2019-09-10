import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def dev_lock_update_name(deviceId, typeValue, typeName):
    url_ = url + "/app/v1.0/lumi/dev/lock/update/name"
    json_ = {
        "deviceId": deviceId,
        "typeValue": typeValue,
        "typeName": typeName
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求参数：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = dev_lock_update_name("lumi.158d0003930b2a", "123", "xxx")
    print(result_main.text)
