import requests
from common.get_result_db import get_share_id
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def share_remove(share_id):
    url_ = url + "/app/v1.0/lumi/position/share/remove"
    json_ = {
        "shareId": share_id
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


def share_remove_jenny(share_id):
    url_ = url + "/app/v1.0/lumi/position/share/remove"
    json_ = {
        "shareId": share_id
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Jenny, proxies=proxies, verify=False)
    return r


def share_remove_jenny_reply(share_id):
    """
    1. 调用回复接口，使用Jenny用户回复
    2. 回复后再调用remove接口
    """
    url_reply = url + "/app/v1.0/lumi/position/share/invite/reply"
    json_reply = {
        "shareId": share_id,
        "result": 1
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_reply)
    requests.post(url=url_reply, json=json_reply, headers=header_Jenny, proxies=proxies, verify=False)

    url_ = url + "/app/v1.0/lumi/position/share/remove"
    json_ = {
        "shareId": share_id
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Jenny, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = share_remove_jenny("share01615847954474037248")
    print(result_main.text)
