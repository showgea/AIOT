import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_create(name, positionId):
    url_ = url + "/app/v1.0/lumi/ifttt/create"
    json_ = {
        "name": name,
        "positionId": positionId,
        "conditions":
            {
                "relation": 0,
                "content":
                    [
                        {
                            "subjectId": "lumi.158d00026e9e32",
                            "subjectModel": "lumi.sensor_cube.aqgl01",
                            "triggerDefinitionId": "TD.lumi.sensor_cube.flip90",
                            "params": []
                        }
                    ]
            },
        "actions":
            {
                "content":
                    [
                        {
                            "subjectId": "lumi.158d0003930b2a",
                            "subjectModel": "lumi.gateway.aqhm01",
                            "actionDefinitionId": "AD.lumi.gateway.music",
                            "params":
                                [
                                    {
                                        "paramId": "PD.musicIndex",
                                        "value": "1"
                                    },
                                    {
                                        "paramId": "PD.vol",
                                        "value": "5"
                                    }
                                ]
                        }
                    ]
            }
    }
    # list_ = ["subjectModel", "subjectId"]
    # num = 0
    # for i in (subjectModel, subjectId):
    #     if i is None:
    #         json_.pop(list_[num])
    #     num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_create()
    print(result_main.text)
