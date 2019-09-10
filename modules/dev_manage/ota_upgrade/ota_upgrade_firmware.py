import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def ota_upgrade_firmware(dids):
    url_ = url + "/app/v1.0/lumi/ota/upgrade/firmware"
    json_ = {
        "dids": dids.split(",")
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求参数：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ota_upgrade_firmware("lumi.158d0003930b2a,lumi.158d0003930b2a")
    print(result_main.text)
