import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def ota_query_firmware(positionId=None, did=None):
    url_ = url + "/app/v1.0/lumi/ota/query/firmware"
    params_ = {
        "positionId": positionId,
        "did": did
    }
    list_ = ["positionId", "did"]
    num = 0
    for i in (positionId, did):
        if i is None:
            params_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求参数：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ota_query_firmware(positionId=None, did="lumi.158d0003930b2a")
    print(result_main.text)
