import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_scene_run(sceneId):
    url_ = url + "/app/v1.0/lumi/ifttt/scene/run"
    json_ = {
        "sceneId": sceneId
        }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_scene_run("AL.615944318139310080")
    print(result_main.text)
