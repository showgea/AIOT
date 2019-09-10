import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_update_info(positionId, positionName=None, remark=None):
    url_ = url + "/app/v1.0/lumi/position/update/info"
    json_ = {
        "positionId": positionId,
        "positionName": positionName,
        "remark": remark
    }
    list_ = ["positionId", "positionName", "remark"]
    num = 0
    for i in (positionId, positionName, remark):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_update_info("real2.611223399695552512", "testroom51", "testroom5")
    print(result_main.text)
