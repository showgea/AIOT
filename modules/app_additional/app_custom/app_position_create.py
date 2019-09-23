import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_position_create(positionName, parentPositionId=None, timeZone=None, isDefault=None, options=None):
    url_ = url + "/app/v1.0/lumi/app/position/create"
    json_ = {
        "positionName": positionName,
        "parentPositionId": parentPositionId,
        "timeZone": timeZone,
        "isDefault": isDefault,
        "options": options
    }
    list_ = ["positionName", "parentPositionId", "timeZone", "isDefault", "options"]
    num = 0
    for i in (positionName, parentPositionId, timeZone, isDefault, options):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


def app_position_create_jenny(positionName, parentPositionId=None, timeZone=None, isDefault=None, options=None):
    url_ = url + "/app/v1.0/lumi/app/position/create"
    json_ = {
        "positionName": positionName,
        "parentPositionId": parentPositionId,
        "timeZone": timeZone,
        "isDefault": isDefault,
        "options": options
    }
    list_ = ["positionName", "parentPositionId", "timeZone", "isDefault", "options"]
    num = 0
    for i in (positionName, parentPositionId, timeZone, isDefault, options):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_position_create("测试位置1", "real1.595330038958653440")
    print(result_main.text)
