import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_create(positionType, positionName, parentPositionId=None, timeZone=None, remark=None, options=None):
    url_ = url + "/app/v1.0/lumi/position/create"
    json_ = {
        "positionType": positionType,
        "positionName": positionName,
        "parentPositionId": parentPositionId,
        "timeZone": timeZone,
        "remark": remark,
        "options": options
    }
    list_ = ["positionType", "positionName", "parentPositionId", "timeZone", "remark", "options"]
    num = 0
    for i in (positionType, positionName, parentPositionId, timeZone, remark, options):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


def position_create_jenny(positionType, positionName, parentPositionId=None, timeZone=None, remark=None, options=None):
    url_ = url + "/app/v1.0/lumi/position/create"
    json_ = {
        "positionType": positionType,
        "positionName": positionName,
        "parentPositionId": parentPositionId,
        "timeZone": timeZone,
        "remark": remark,
        "options": options
    }
    list_ = ["positionType", "positionName", "parentPositionId", "timeZone", "remark", "options"]
    num = 0
    for i in (positionType, positionName, parentPositionId, timeZone, remark, options):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_create("1", "测试位置1", "real1.595330038958653440")
    print(result_main.text)
