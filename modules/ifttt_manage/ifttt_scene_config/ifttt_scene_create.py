import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_scene_create(positionId, name, subjectId):
    url_ = url + "/app/v1.0/lumi/ifttt/scene/create"
    json_ = {
        "positionId": positionId,
        "name": name,
        "content": [
            {
                "subjectId": subjectId,
                "subjectModel": "lumi.gateway.aqhm01",
                "actionDefinitionId": "AD.lumi.gateway.music",
                "delayType": "0",
                "delayTimeUnit": "0",
                "serialNum": 0,
                "params": [
                        {
                            "paramId": "PD.vol",
                            "value": "5"
                        },
                        {
                            "paramId": "PD.musicIndex",
                            "value": "23"
                        }
                    ]
                }
            ],
        "iconId": "test"
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_scene_create("real1.615940701625851904", "testScene", "lumi.158d0003930b2a")
    print(result_main.text)
