import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_notice_query_list(messageTypes=None, state=None, startTime=None, endTime=None, size=None, startIndex=None):
    url_ = url + "/app/v1.0/lumi/user/notice/query/list"
    json_ = {
        "messageTypes": messageTypes,
        "state": state,
        "startTime": startTime,
        "endTime": endTime,
        "size": size,
        "startIndex": startIndex
    }
    list_ = ["messageTypes", "state", "startTime", "endTime", "size", "startIndex"]
    num = 0
    for i in (messageTypes, state, startTime, endTime, size, startIndex):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_notice_query_list()
    print(result_main.text)
