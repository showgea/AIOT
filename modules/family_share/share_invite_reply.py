from common.get_result_db import get_share_id
import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def invite_reply(share_id, result):
    url_ = url + "/app/v1.0/lumi/position/share/invite/reply"
    json_ = {
        "shareId": share_id,
        "result": result
    }
    r = requests.post(url=url_, json=json_, headers=header_Jenny)
    # print(r.text, 1111)
    # 2204：邀请已经回复
    if '"code":2204' or '"code":2203' in r.text:
        url_remove = url + "/app/v1.0/lumi/position/share/remove"
        json_remove = {
            "shareId": share_id
        }
        proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

        print("请求数据：%s" % json_remove)
        requests.post(url=url_remove, json=json_remove, headers=header_Jenny, proxies=proxies, verify=False)
        share_id_2 = get_share_id()
        json_2 = {
            "shareId": share_id_2,
            "result": result
        }
        proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

        print("请求数据：%s" % json_2)
        r = requests.post(url=url_, json=json_2, headers=header_Jenny, proxies=proxies, verify=False)
        # print(r.text, 222)
        return r
    return r


def invite_reply_same(share_id, result):
    url_ = url + "/app/v1.0/lumi/position/share/invite/reply"
    json_ = {
        "shareId": share_id,
        "result": result
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = invite_reply("share01611967747240960000", 1)
    print(result_main.text)
    # share_id_main = get_share_id()
    # res1 = invite_reply(share_id_main, 1)
    # print(res1.text)

