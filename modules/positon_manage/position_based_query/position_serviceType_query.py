import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_serviceType_query(positionId, size=None, startIndex=None):
    url_ = url + "/app/v1.0/lumi/position/service_type/query"
    params_ = {
        "positionId": positionId,
        "size": size,
        "startIndex": startIndex
    }
    list_ = ["positionId", "size", "startIndex"]
    num = 0
    for i in (positionId, size, startIndex):
        if i is None:
            params_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_serviceType_query("real1.611208606918021120", size=None, startIndex=None)
    print(result_main.text)
