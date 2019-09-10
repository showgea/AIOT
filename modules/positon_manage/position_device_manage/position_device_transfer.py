import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_device_transfer(deviceId, positionId):
    url_ = url + "/app/v1.0/lumi/position/device/transfer"
    json_ = {
        "deviceId": deviceId,
        "positionId": positionId
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_device_transfer("lumi.158d0003930b2a", "real1.611173955715129344")
    print(result_main.text)
