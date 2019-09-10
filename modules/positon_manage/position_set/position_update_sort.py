import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_update_sort(list_):
    url_ = url + "/app/v1.0/lumi/position/update/sort"
    json_ = {
        "list": list_
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_update_sort([{"positionId": "real2.611173955740295168", "ss": "1"},
                                        {"positionId": "real2.611209272520511488", "sortNo": "2"},
                                        {"positionId": "real2.611223399695552512", "sortNo": "3"}])
    print(result_main.text)
