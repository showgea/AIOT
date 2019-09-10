import requests
from common.get_result_db import get_share_id
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Gary
url = readcfg.url


def share_invite(position_id, account, permission, hint, remark):
    url_ = url + "/app/v1.0/lumi/position/share/invite"
    json_ = {
        "positionId": position_id,
        "account": account,
        "permission": permission,
        "hint": hint,
        "remark": remark
    }
    r = requests.post(url=url_, json=json_, headers=header_Gary)
    return r


def share_invite_after_remove(position_id, account, permission, hint, remark):
    url_ = url + "/app/v1.0/lumi/position/share/invite"
    json_ = {
        "positionId": position_id,
        "account": account,
        "permission": permission,
        "hint": hint,
        "remark": remark
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    # print(111)
    print("第一次返回数据%s" % r.text)
    # 如果位置已经分享，先调用remove接口，删除分享，再进行分享，保证一定可以分享成功
    if '"code":2206' in r.text:
        share_id2 = get_share_id()
        url_2 = url + "/app/v1.0/lumi/position/share/remove"
        json_2 = {
            "shareId": share_id2
        }
        proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

        print("请求数据：%s" % json_)
        requests.post(url=url_2, json=json_2, headers=header_Gary, proxies=proxies, verify=False)
        r = share_invite(position_id, account, permission, hint, remark)
        print("判断后返回数据%s" % r.text)
        # print(222)
    return r.text


if __name__ == '__main__':
    result_main = share_invite_after_remove("real1.611173955715129344", "13798371391", 3, "hint", "remark")
    # shareId = json.loads(r.text)["result"]["shareId"]
    print(result_main)
