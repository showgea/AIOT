import requests
import json
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_scene_delete_position(positionList, deleteLabel):
    url_ = url + "/app/v1.0/lumi/ifttt/scene/delete/position"
    json_ = {
        "positionList": positionList.split(","),
        "deleteLabel": deleteLabel
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_scene_delete_position("real1.615945282405605376", "both")
    print(result_main.text)
