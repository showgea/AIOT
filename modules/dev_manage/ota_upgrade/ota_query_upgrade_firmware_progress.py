import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def ota_query_upgrade_firmware_progress(did):
    url_ = url + "/app/v1.0/lumi/ota/query/upgrade/firmware/progress"
    params_ = {
        "did": did
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求参数：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ota_query_upgrade_firmware_progress("lumi.158d0003930b2a")
    print(result_main.text)
