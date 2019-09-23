import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def irdevice_area_query():
    url_ = url + "/app/v1.0/lumi/irdevice/area/query"
    json_ = {
        "areaType": "1",
        "areaId": "440000"
    }

    print("请求数据：%s" % json_)
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    r = requests.post(url=url_, json=json_, proxies=proxies, headers=header_Gary, verify=False)
    return r


if __name__ == '__main__':
    result_main = irdevice_area_query()
    print(result_main.text)
