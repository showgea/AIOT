import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_linkage_copy(linkageId, name=None):
    url_ = url + "/app/v1.0/lumi/ifttt/linkage/copy"
    json_ = {
        "linkageId": linkageId,
        "name": name
        }
    list_ = ["subjectModel", "name"]
    num = 0
    for i in (linkageId, name):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_linkage_copy("L.619498025691082752")
    print(result_main.text)
