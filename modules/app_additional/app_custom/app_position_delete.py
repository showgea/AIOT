import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url
position_list = ['real1.615940701625851904', 'real2.615940701667794944', 'real1.615945282405605376',
                 'real2.615945282455937024', "virtual.615960161418027008"]


def app_position_delete(positionId):
    url_ = url + "/app/v1.0/lumi/app/position/delete"
    json_ = {
        "positionId": positionId
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    if positionId in position_list:
        return '"code":0'
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r.text


if __name__ == '__main__':
    result_main = app_position_delete("virtual.615960161418027008")
    print(result_main)
