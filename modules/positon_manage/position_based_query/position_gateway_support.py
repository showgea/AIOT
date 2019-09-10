import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_gateway_support(positionId, model, size=None, startIndex=None):
    url_ = url + "/app/v1.0/lumi/position/gateway/support"
    params_ = {
        "positionId": positionId,
        "model": model,
        "size": size,
        "startIndex": startIndex
    }
    list_ = ["positionId", "model", "size", "startIndex"]
    num = 0
    for i in (positionId, model, size, startIndex):
        if i is None:
            params_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_gateway_support("real1.611208606918021120", " lumi.light.aqcn02", size=10, startIndex=0)
    print(result_main.text)
