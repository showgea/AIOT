import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def res_history_delete(subjectIds):
    url_ = url + "/app/v1.0/lumi/res/history/delete"
    json_ = {
        "subjectIds": subjectIds.split(",")
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = res_history_delete("lumi.158d0003930b2a, 1567137600000")
    print(result_main.text)
