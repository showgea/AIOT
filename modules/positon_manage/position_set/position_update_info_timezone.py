import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_update_info_timezone(positionId, timeZone, timeZoneCity=None):
    url_ = url + "/app/v1.0/lumi/position/update/info/timezone"
    json_ = {
        "positionId": positionId,
        "timeZone": timeZone,
        "timeZoneCity": timeZoneCity
    }
    list_ = ["positionId", "timeZone", "timeZoneCity"]
    num = 0
    for i in (positionId, timeZone, timeZoneCity):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_update_info_timezone("real1.613795261451169792", "+5", "tz_dublin")
    print(result_main.text)
