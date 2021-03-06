import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_block_remove(panelId, serviceIds):
    url_ = url + "/app/v1.0/lumi/app/block/remove"
    json_ = {
        "panelId": panelId,
        "serviceIds": serviceIds.split(",")
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_block_remove("real1.615940701625851904", "S01604404595468013568")
    print(result_main.text)
