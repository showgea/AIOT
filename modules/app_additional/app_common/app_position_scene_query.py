import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_position_scene_query(positionId, startIndex=None, size=None):
    url_ = url + "/app/v1.0/lumi/app/position/scene/query"
    params_ = {
        "positionId": positionId,
        "startIndex": startIndex,
        "size": size
    }
    list_ = ["positionId", "startIndex", "size"]
    num = 0
    for i in (positionId, startIndex, size):
        if i is None:
            params_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_position_scene_query("real1.615940701625851904")
    print(result_main.text)
