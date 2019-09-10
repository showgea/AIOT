import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def res_write(subjectId, data):
    url_ = url + "/app/v1.0/lumi/res/write"
    json_ = {
        "subjectId": subjectId,
        "data": data
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = res_write("lumi.158d0003930b2a", {"corridor_light_status": 2, "brightness_level": 25})
    print(result_main.text)
