import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_service_query(positionId, serviceTypes=None, size=None, startIndex=None, subjectModels=None, labels=None, access=None):
    url_ = url + "/app/v1.0/lumi/position/service/query"
    json_ = {
        "positionId": positionId,
        "serviceTypes": serviceTypes,
        "size": size,
        "startIndex": startIndex,
        "subjectModels": subjectModels,
        "labels": labels,
        "access": access
    }
    list_ = ["positionId", "serviceTypes", "size", "startIndex", "subjectModels", "labels", "access"]
    num = 0
    for i in (positionId, serviceTypes, size, startIndex, subjectModels, labels, access):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_service_query("real1.611208606918021120", size=None, startIndex=None)
    print(result_main.text)
