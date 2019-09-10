import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime, startIndex=None, size=None, aggrType=None):
    url_ = url + "/app/v1.0/lumi/service/attribute/history/aggr/query"
    json_ = {
        "serviceId": serviceId,
        "dimensionType": dimensionType,
        "startTime": startTime,
        "endTime": endTime,
        "startIndex": startIndex,
        "size": size,
        "aggrType": aggrType
    }
    list_ = ["serviceId", "dimensionType", "startTime", "endTime", "startIndex", "size", "aggrType"]
    num = 0
    for i in (serviceId, dimensionType, startTime, endTime, startIndex, size, aggrType):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = service_attribute_history_aggr_query("S01615944652489261056", "hour", "1564804800000", "1567137600000")
    print(result_main.text)
