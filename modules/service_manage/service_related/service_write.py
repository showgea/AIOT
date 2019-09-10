import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def service_write(serviceId, data):
    url_ = url + "/app/v1.0/lumi/service/write"
    json_ = {
        "serviceId": serviceId,
        "data": data
    }

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = service_write("S01615944652489261056", {"cube_status": "shake_air"})
    print(result_main.text)
