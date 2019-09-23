import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def res_history_aggr_query_new(subjectId, attrs, dimensionType, startTime, endTime, startIndex=None, size=None, aggrType=None):
    url_ = url + "/app/v1.0/lumi/res/history/aggr/query/new"
    json_ = {
        "subjectId": subjectId,
        "attrs": attrs.split(","),
        "dimensionType": dimensionType,
        "startTime": startTime,
        "endTime": endTime,
        "startIndex": startIndex,
        "size": size,
        "aggrType": aggrType
    }
    list_ = ["subjectId", "attrs", "dimensionType", "startTime", "endTime", "startIndex", "size", "aggrType"]
    num = 0
    for i in (subjectId, attrs, dimensionType, startTime, endTime, startIndex, size, aggrType):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = res_history_aggr_query_new("lumi.158d0003930b2a", "argb_value, abc", "hour", "", "1567137600000", 0, 100, "max")
    print(result_main.text)
