import requests
from config import readcfg

header_Gary = readcfg.header_Gary_subscribe
header_Jenny = readcfg.header_Jenny_subscribe
url = readcfg.url


def res_unsubscribe(subjectId, attrs):
    url_ = url + "/app/v1.0/lumi/res/unsubscribe"
    json_ = {
        "data": [
            {
                "subjectId": subjectId,
                "attrs": attrs.split(",")
            }
        ]
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = res_unsubscribe("lumi.158d0003930b2a", "corridor_light_status")
    print(result_main.text)
