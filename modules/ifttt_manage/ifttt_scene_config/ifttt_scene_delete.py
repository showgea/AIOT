import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_scene_delete(sceneId, sceneRule=None):
    url_ = url + "/app/v1.0/lumi/ifttt/scene/delete"
    json_ = {
        "sceneId": sceneId,
        "sceneRule": sceneRule
    }
    list_ = ["sceneId", "sceneRule"]
    num = 0
    for i in (sceneId, sceneRule):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_scene_delete("AL.621010790524870656")
    print(result_main.text)
