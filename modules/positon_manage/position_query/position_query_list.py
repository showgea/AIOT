import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_query_list(positionId=None, positionType=None, size=None, startIndex=None):
    url_ = url + "/app/v1.0/lumi/position/query/list"
    params_ = {
        "positionId": positionId,
        "positionType": positionType,
        "size": size,
        "startIndex": startIndex
    }
    list_ = ["positionId", "positionType", "size", "startIndex"]
    num = 0
    for i in (positionId, positionType, size, startIndex):
        if i is None:
            params_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_query_list("real1.611173955715129344", 1, 100)
    print(result_main.text)
