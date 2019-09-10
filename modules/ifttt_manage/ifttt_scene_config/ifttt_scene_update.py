import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_scene_update(name):
    url_ = url + "/app/v1.0/lumi/ifttt/scene/update"
    json_ = {
        "sceneId": "AL.615944318139310080",
        "name": name,
        "content": [
            {
                "delayTimeUnit": "0",
                "beginTimeBand": "",
                "serialNum": 0,
                "actionDefinitionId": "AD.lumi.gateway.open_corridor_light",
                "subjectType": 1,
                "subjectId": "lumi.158d0003930b2a",
                "subjectModel": "lumi.gateway.aqhm01",
                "delayType": "0",
                "actionId": "A01615944318658895872",
                "endTimeBand": "",
                "delayTime": "0",
                "actionName": "开夜灯",
                "subjectName": "Aqara Hub-0975",
                "status": 1
            }
        ],
        "createDate": "2019-08-27"
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_scene_update("开夜灯5")
    print(result_main.text)
