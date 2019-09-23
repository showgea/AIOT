import requests
from config import readcfg

header_Gary = readcfg.header_Gary_subscribe
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_additional_report_clientid(deviceToken):
    url_ = url + "/app/v1.0/lumi/app/additional/report/clientid"
    params_ = {
        "deviceToken": deviceToken
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_additional_report_clientid("123")
    print(result_main.text)
