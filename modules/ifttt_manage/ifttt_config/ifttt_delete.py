import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_delete(linkageId, linkageRule=None):
    url_ = url + "/app/v1.0/lumi/ifttt/delete"
    json_ = {
        "linkageId": linkageId,
        "linkageRule": linkageRule
        }
    list_ = ["subjectModel", "linkageRule"]
    num = 0
    for i in (linkageId, linkageRule):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_delete("L.620684744405655552")
    print(result_main.text)
