import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_device_assign(dids, positionId, layout=None):
    url_ = url + "/app/v1.0/lumi/position/device/assign"
    json_ = {
        "dids": [dids],
        "positionId": positionId,
        "layout": layout
    }
    list_ = ["dids", "positionId", "layout"]
    num = 0
    for i in (dids, positionId, layout):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_device_assign("lumi.158d00031aedcd,lumi.158d0001f9bc42", "real1.611173955715129344")
    print(result_main.text)
