import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def service_attribute_history_query(serviceId, startTime=None, endTime=None, startIndex=None, size=None):
    url_ = url + "/app/v1.0/lumi/service/attribute/history/query"
    json_ = {
        "serviceId": serviceId,
        "startTime": startTime,
        "endTime": endTime,
        "startIndex": startIndex,
        "size": size
    }
    list_ = ["serviceId", "startTime", "endTime", "startIndex", "size"]
    num = 0
    for i in (serviceId, startTime, endTime, startIndex, size):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = service_attribute_history_query("lumi.158d0003930b2a", "1562169600000", "1567137600000", 0, 100)
    print(result_main.text)
