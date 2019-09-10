import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_scene_try():
    url_ = url + "/app/v1.0/lumi/ifttt/scene/try"
    json_ = {
        "positionId": "real1.615940701625851904",
        "name": "testScene",
        "content": [
            {
                "subjectId": "lumi.158d0003930b2a",
                "subjectModel": "lumi.gateway.aqhm01",
                "actionDefinitionId": "AD.lumi.gateway.music",
                "delayType": "0",
                "delayTimeUnit": "0",
                "serialNum": 0,
                "params": [
                        {
                            "paramId": "PD.vol",
                            "value": "6"
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
    result_main = ifttt_scene_try()
    print(result_main.text)
