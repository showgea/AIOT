import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_customaction_set():
    url_ = url + "/app/v1.0/lumi/app/customaction/set"
    json_ = {
        "customActionId": "123",
        "userDeviceId": "lumi.158d0003930b2a",
        "deviceModel": "lumi.gateway.aqhm01",
        "actionId": "scene_mode",
        "customName": "test1",
        "value": "{\"argb_value\":\"469696595\", \"brightness_level\":\"10\"}",
        "icon": "2",
        "actionType": "1"
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_customaction_set()
    print(result_main.text)
